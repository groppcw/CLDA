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

times = []

for i in range(START_IDX,NUM_TIMES):
  #open file for that timestep
  inferfile = open("mixtures/time-"+str(i)+".local","r")
  docs = []
  for line in inferfile:
    content = line.strip().split()
    buckets = [0] * GLOBAL_TOPICS
    for index,val in enumerate(content):
      #fill buckets
      address = membership[str(index)]
      buckets[int(address)] += float(val)
    #append bucketed values to list
    docs.append(buckets[:]) #need to deep copy because python hates scopes for some reason
  #append document pile to list
  times.append(docs[:])

  inferfile.close()

# STEP 3:
# Emit the output (timestep * document * subjects)

for i in range(START_IDX,NUM_TIMES):
  outfile = open("mixtures/time-"+str(i)+".global","w")
  for doc in times[i]:
    for item in doc:
      outfile.write(str(item) + ' ')
    outfile.write("\n")

  outfile.close()
