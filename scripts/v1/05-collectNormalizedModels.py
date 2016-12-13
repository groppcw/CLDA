#takes dtm-chunk-#.model.normalized files and creates a dtm-chunk-all.model file

from settings import *

outfile = open("./local_models/all.normalized","w")

dictionary = open("./input_data/word_ids.dat","r")

listoflists = []

for line in dictionary:
  pieces = (line.replace('\t',' ')).split(' ',1)
  word = (pieces[1].strip()).replace('\"','')
  listoflists.append([word])

dictionary.close()

for index in range(NUM_TIMES):
  infile = open("./local_models/time-"+str(index)+".normalized","r")
  for linenum,line in enumerate(infile):
    back = line.split(' ',1) #gets rid of leading word
    pieces = back[1].split()
    for item in pieces:
      listoflists[linenum].append(item)
  infile.close()


for item in listoflists:
  for chunk in item:
     outfile.write(chunk+' ')
  outfile.write('\n')

outfile.close()
