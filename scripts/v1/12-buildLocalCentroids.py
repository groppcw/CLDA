from settings import *

memberfile = open("clustering/membership.dat","r")
members = dict()
for line in memberfile:
  key = line.strip().split()[0]
  val = line.strip().split()[1]
  members[int(key)]=int(val)

memberfile.close()

for time in range(START_IDX,NUM_TIMES):
  infile = open("local_models/time-"+str(time)+".normalized","r")
  outfile = open("local_models/time-"+str(time)+".centroids","w")
  for line in infile:
    sums = [0.0]*GLOBAL_TOPICS
    normalizer = [0]*GLOBAL_TOPICS
    for nval,val in enumerate(line.strip().split()):
      if nval == 0:
        outfile.write(val) #vocab
      else:
        sums[members[nval-1 + LOCAL_TOPICS*time]] += float(val)
        normalizer[members[nval-1 + LOCAL_TOPICS*time]] += 1
    for index in range(GLOBAL_TOPICS):
      sums[index] = sums[index]/max(float(normalizer[index]),1) #don't divide by zero
    for element in sums:
      outfile.write(" "+str(element))
    outfile.write("\n")
  infile.close()
  outfile.close()
