# take a bunch of model_0 model_1 etc files and merge them alphabetically

from settings import *



# for each file, load the file into one giant list
# call sort on the list
# write this output somewhere else

for timestep in range(START_IDX,NUM_TIMES):

  model = dict()

  #Add the full vocabulary to the dictionary
  fdict = open("./input_data/word_ids.dat","r")
  for line in fdict:
    pieces = (line.replace('\t',' ')).split(' ',1)
    key = (pieces[1].strip()).replace('\"','')
    value = ''
    for unused in range(LOCAL_TOPICS):
      value = value + '0 '
    value = value.strip() + '\n'
    model[key] = value
  fdict.close()

  #Replace words that actually appear
  for num in range(PLDA_CHUNKS):
    infile = open("./partial_results/time-"+str(timestep)+"-model_"+str(num),"r")
    for line in infile:
      pieces = (line.replace('\t',' ')).split(' ',1)
      model[pieces[0]] = pieces[1]
    infile.close()

  outmodel = sorted(model) # gives sorted list of keys

  outfile = open("./local_models/time-"+str(timestep)+".model","w")

  for key in outmodel:
    outfile.write(key + " " + model[key])

  outfile.close()
