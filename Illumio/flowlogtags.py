import csv

#Create Dictionary with port and protocol tuple as key and tag as value using the lookup table 
#Create protocol dictionary
protocols={'1':'icmp','6':'tcp','17':'udp'}
lookup={}
unTagged=0
with open('lookup_tags.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        # print(row[0],row[1],row[2])
        if len(row)!=0 and row[0]!='dstport':
            lookup[(row[0],row[1])]=[row[2],0]

f=open('log.txt','r')
textReader=f.readlines()
for line in textReader:
    temp=line.split(" ")
    if len(temp)>1:
        # print(temp[7],temp[8])
        if (temp[7],protocols[temp[8]]) in lookup.keys():
            lookup[(temp[7],protocols[temp[8]])][1]+=1
        else:
            unTagged+=1
f.close()
#Create another dictionary with tag as key and its count as values using lookup
tagCount={}
for i in lookup.keys():
    if lookup[i][0] not in tagCount:
        tagCount[lookup[i][0]]=lookup[i][1]
    else:
        tagCount[lookup[i][0]]+=lookup[i][1]
f2=open('output.txt','w')
f2.write("Tag Counts\n")
f2.write("Tag, Count\n")
for tag in tagCount:
    tempTags=tag+', '+str(tagCount[tag])+"\n"
    f2.write(tempTags)
noTag='Untagged, '+str(unTagged)+"\n\n"
f2.write(noTag)
f2.write("Port/Protocol Combination Counts: \n")
f2.write("Port , Protocol , Count \n")
for port in lookup:
    tempPort=port[0]+', '+port[1]+', '+str(lookup[port][1])+"\n"
    f2.write(tempPort)
f2.close()