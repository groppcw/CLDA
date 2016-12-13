import math
import copy

from settings import *

totallog = 0.0
numtokens = 0

outfile = open("perplexity/perplexity.training.log","w")

for time in range(START_IDX,NUM_TIMES):
  print "Beginning time ",time
  timelog = 0.0
  #build topics into a dictionary of "word,[topic proportions for that word]"
  topicfile = open("local_models/time-"+str(time)+".centroids","r")
  worddict = dict()
  for line in topicfile:
    word = line.split(" ")[0]
    stuff = line.strip().split(" ",1)[1]
    worddict[word] = stuff
  topicfile.close()

  #build normalized mixtures
  mixfile = open("mixtures/time-"+str(time)+".training.withCentroids","r")
  mixtures = list()
  for doc in mixfile:
    mix = doc.strip().split()
    mixsum = 0.0
    for element in mix:
      mixsum += float(element)
    normalmix = list()
    for element in mix:
      normalmix.append(float(element)/max(mixsum,1.0))
    mixtures.append(copy.deepcopy(normalmix)) # force a copy, because python doesn't understand how scope is supposed to work
  mixfile.close()

  docfile = open("subcorpora/time-"+str(time)+".dat","r")
  for n,doc in enumerate(docfile):
    if n % 1000 == 0:
      print "Processed ",n," documents"
    doclog = 0.0
    for offset,entry in enumerate(doc.strip().split()):
      if offset % 2 == 0:
        word = entry
      else:
        count = int(entry)
        numtokens += count
        topicvals = worddict[word] # remember that this is a list of strings still
        docmixture = mixtures[n]
        localprob = 0.0
        for tnum, topicval in enumerate(topicvals.split()):
          localprob += float(topicval)*docmixture[tnum]
        if localprob == 0:
          print "Local probability zero for word",word,"with count",count,"in document",n
        else:
          doclog += math.log(localprob)*float(count)
    timelog += doclog

  docfile.close()
  totallog += timelog
  outfile.write("log-likelihood from time "+str(time)+": "+str(timelog)+"\n")

outfile.write("total log-likelihood: "+str(totallog)+"\n")
outfile.write("total token count: "+str(numtokens)+"\n")
perplexity = math.exp(-1.0 * totallog / float(numtokens))
outfile.write("perplexity: "+str(perplexity)+"\n")

outfile.close()
