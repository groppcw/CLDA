from settings import *

#takes a collected model file and spits out the TOP_X words in each topic

for i in range(START_IDX,NUM_TIMES):

  infile = open("local_models/time-"+str(i)+".normalized","r")
  outfile = open("top_words/time-"+str(i)+"-top20.local.txt","w")
  rawfile = open("top_words/time-"+str(i)+"-top20.local.raw","w")

  # load the file into a list of lists
  # for each data column, sort by that column and output the word column for the top 20 entries

  # build the list of lists
  listoflists = []

  for line in infile:
    thisline = line.split()
    listoflists.append(thisline)
    numcols = len(thisline)

  for topic in range(numcols - 1):
    listoflists.sort(key=lambda x: float(x[topic + 1]),reverse=True)
    outfile.write("Topic "+str(topic)+"\n\n")
    for i in range(TOP_X):
      outfile.write(listoflists[i][0]+"\t"+listoflists[i][topic+1]+"\n")
      rawfile.write(listoflists[i][0]+" ")
    outfile.write("\n")
    rawfile.write("\n")

  infile.close()
  outfile.close()
  rawfile.close()
