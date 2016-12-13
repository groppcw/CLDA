infile = open("./local_models/time-all.normalized","r")
outfile = open("./clustering/initial.dat","w")

listoflists = []

for line in infile:
  listoflists.append(line.strip().split())

numtopics = len(listoflists[0])-1
numwords = len(listoflists)

for topic in range(1,numtopics+1): #fancy indexing because words are still there
  outfile.write(str(topic)+' ')
  for word in range(numwords):
    outfile.write(listoflists[word][topic]+' ')
  outfile.write('\n')

infile.close()
outfile.close()
