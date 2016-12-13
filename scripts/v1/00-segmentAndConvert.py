fdict = open("./input_data/word_ids.dat","r")
dictionary = dict()
for line in fdict:
     pieces = line.split()
     dictionary[pieces[0]] = (pieces[1].strip()).replace('\"','')

fdict.close()


fseq = open("./input_data/data-seq.dat","r")
#segment first, then convert
start = 0
total = 0
for tstep, line in enumerate(fseq):
  if tstep > 0: #skip the extraneous number of timesteps entry
     timestep = tstep - 1
     print "converting timestep", timestep
     numDocsThisStep = int(line)
     #segment
     fthis = open("./partial_results/dtm-chunk-" + str(timestep) + ".remove","w")
     fmult = open("./input_data/data-mult.dat","r")
     for doc, line3 in enumerate(fmult):
         if doc >= start and doc < start + numDocsThisStep:
              fthis.write(line3.partition(' ')[2]) # rips out the extraneous uniqueness count
     fthis.close()
     fmult.close()
     fthis = open("./partial_results/dtm-chunk-" + str(timestep) + ".remove","r")
     fthisout = open("./subcorpora/time-" + str(timestep) + ".dat","w")
     for line2 in fthis:
          #convert
          counts = line2.split()
          for i, item in enumerate(counts):
               chunks = item.split(":")
               wordid = dictionary[chunks[0]]
               wordcount = chunks[1]
               total = total + int(chunks[1])
               fthisout.write(wordid + " " + wordcount + " ");
          fthisout.write("\n")
     fthis.close()
     start += numDocsThisStep

fseq.close()

ftotal = open("./results/num_tokens.dat","w")
ftotal.write(str(total))
ftotal.close()
ftotal = open("./perplexity/num_tokens.dat","w")
ftotal.write(str(total))
ftotal.close()
