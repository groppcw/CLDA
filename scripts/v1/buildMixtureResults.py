from settings import *

# STEP 1:
# Build a dictionary of source topics to final centroids

membership = dict()

memfile = open("clustering/membership.dat","r")
for line in memfile:
  content = line.strip().split()
  membership[content[0]] = content[1]

memfile.close()

# STEP 2:
# For each timestep, for each document, for each topic, add value to corresponding bucket

outfile = open("results/mixtures.result","w")

outfile.write("TIME GLOBAL_ID LOCAL_ID VALUE\n")

for i in range(START_IDX,NUM_TIMES):
  #open file for that timestep
  inferfile = open("mixtures/time-"+str(i)+".local","r")

  buckets = [0.0] * LOCAL_TOPICS
  for line in inferfile:
    content = line.strip().split()
    for index,val in enumerate(content):
      #fill buckets
      #address = membership[str(index)]
      buckets[index] += float(val)

  inferfile.close()

  #normalize bucket sum to 1
  bucketsum = 0.0
  for item in buckets:
    bucketsum += item
  for index,item in enumerate(buckets):
    newval = item / bucketsum
    buckets[index] = newval

# STEP 3:
# Emit the output (timestep * document * subjects)

  for index,topic in enumerate(buckets):
    address = membership[str(int(index)+i*LOCAL_TOPICS)]
    outfile.write(str(i) + ' ')
    outfile.write(str(address) + ' ')
    outfile.write(str(int(index)+i*LOCAL_TOPICS) + ' ')
    outfile.write(str(topic))
    outfile.write("\n")

outfile.close()
