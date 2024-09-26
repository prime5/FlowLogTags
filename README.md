# FlowLogTags
FlowLogTags takes flow logs as per  https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html  and generates tag counts using a lookup.

Assumptions:
- Input log file strictly follows order given in 'Available Fields' section https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html for version 2 only
- Protocol Dictionary can be enhanced to have all exhaustive list of protocol numbers and their respective values used in lookup csv

Based on https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html we have log format of tab separated values of following in this order:
<version>, <account-id>, <interface-id>, <srcaddr>, <dstaddr>, <srcport>, <dstport>, <protocol>, <packets>, <bytes>, <start>, <end>, <action>, <log-status>
So dstport is 7th value and protocol is 8th value. If we put these value in array or list they are at 6th and 7th index respectively. We have to increase index count by 1 as we are reading file starting with space.

For reading log file we have lookup csv of tags with dstport, protocol and tag. Here tag value can be repeated but dstport, protocol combination is unique. We can make use of unique combination of dstport and protocol tag as tuple which can be used as key in a dictionary called lookup. The dictionary values are not only consisting of tags but their respective counts too. These counts are used for Port/Protocol Combination Counts. Counts are updated when we parse input log file. While parsing log file we need to make use of another dictionary for protocols that will help to match protocol text values with numbers in log files

To get tag counts we need to create another dictionary called tagcount. We loop over all key and values of lookup to get counts for each tag.

To run this use python interpreter on given directory structure. Simply run 'python3 flowlogtags.py' by having same directory structure
