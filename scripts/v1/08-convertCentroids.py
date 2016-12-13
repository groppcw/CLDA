infile = open("clustering/centroids.raw","r")
dictfile = open("input_data/word_ids.dat","r")
outfile = open("clustering/centroids.dat","w")

listoflists = []

for line in dictfile:
  pieces = line.split()
  listoflists.append([pieces[1].strip().replace('\"','')])
  # ^ that's a list containing just the word in the dictionary

for linenum, line in enumerate(infile):
  back = (line.split(' ',1))[1].strip() # rip off the leading index
  pieces = back.split()
  for pnum, piece in enumerate(pieces):
    listoflists[pnum].append(piece)

for line in listoflists:
  for value in line:
    outfile.write(value+' ')
  outfile.write('\n')

infile.close()
dictfile.close()
outfile.close()
