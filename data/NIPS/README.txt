This data contains a processed form of the Neural Information Processing Systems (NIPS) conference proceedings from the years 1987-2003. We took the data described in:

A. Globerson, G. Chechik, F. Pereira, and N. Tishby. Euclidean Embedding of Co-occurrence Data. The Journal of Machine Learning Research, 8:2265-2295, 2007.

and accessible from:

http://ai.stanford.edu/~gal/data.html

and further processed it using MATLAB, removing infrequent words, discarding the author information, and mapping documents to what years they were published.

This format is the one used by the Blei et al implementation of Dynamic Topic Models (DTM), which we convert in the preprocessing stage of CLDA; it is provided here in this form for ease of comparison.

data-mult.dat contains wordcount information, where each line is a document. Within each line, the first value is the number of unique words, followed by a series of ID:Count pairs. These documents are ordered as described in data-seq.dat.
data-seq.dat contains segmentation information. The first value is the number of segments, followed by how many documents are in each segment.
word_ids.dat contains a dictionary mapping each word's ID to the word itself.
