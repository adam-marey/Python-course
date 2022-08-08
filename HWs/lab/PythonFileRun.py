qbfile = open("qbdata.txt","r")

for aline in qbfile:
    values = aline.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )

qbfile.close()

infile = open("qbdata.txt","r")
outfile = open("qbnames.txt","w")

# note: I have rewrittent the code to iterate using a for loop instead of a while loop; it's much simpler that way!
# aline = infile.readline()
# while aline:
for aline in infile:
    items = aline.split()
    dataline = items[1] + ',' + items[0]
    outfile.write(dataline + '\n')
#    aline = infile.readline()

infile.close()
outfile.close()
