from settings import *
import random

if HOLDOUT_MOD == 0: #indicates we are not using holdouts and working with the whole set
  print "Not using holdouts."
  quit()

fdict = open("./input_data/word_ids.dat","r")
dictionary = dict()
for line in fdict:
     pieces = line.split()
     dictionary[pieces[0]] = (pieces[1].strip()).replace('\"','')

fdict.close()

for timestep in range(START_IDX,NUM_TIMES):
  biglist = []
  fthis = open("./partial_results/dtm-chunk-" + str(timestep) + ".remove","r")
  fthisout = open("./subcorpora/time-" + str(timestep) + ".dat","w") #note that this will overwrite the existing datafile
  fthisheldout = open("./subcorpora/time-" + str(timestep) + "-holdout.dat","w")
  for line in fthis:
    #convert
    counts = line.split()
    sublist = []
    for item in counts:
      chunks = item.split(":")
      sublist.append(chunks)

    biglist.append(sublist[:])

  random.seed(0) # forces all runs of this to generate the same shuffle
  random.shuffle(biglist) # that way, we divide rather than overlap our samples

  for num,line2 in enumerate(biglist):
    for item in line2:
      wordid = dictionary[item[0]]
      wordcount = item[1]
      if num % HOLDOUT_MOD != HOLDOUT_IDX:
        fthisout.write(wordid + " " + wordcount + " ");
      else:
        fthisheldout.write(wordid + " " + wordcount + " ");
    if num % HOLDOUT_MOD != HOLDOUT_IDX:
      fthisout.write("\n")
    else:
      fthisheldout.write("\n")
  fthis.close()
  fthisout.close()
  fthisheldout.close()
