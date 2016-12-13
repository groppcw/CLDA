This data is a collection of abstracts from computer science publications in journals spanning 1996-2012. This data was acquired from Elsevier through Clemson University's partnership with LexisNexis. If you have questions about the details of this data, please contact Dr. Amy Apon at Clemson University.

The data-mult.dat file in this collection is too large for github; please contact Dr. Amy Apon at CLemson University for access until a more suitable host is found.

This format is the one used by the Blei et al implementation of Dynamic Topic Models (DTM), which we convert in the preprocessing stage of CLDA; it is provided here in this form for ease of comparison.

data-mult.dat contains wordcount information, where each line is a document. Within each line, the first value is the number of unique words, followed by a series of ID:Count pairs. These documents are ordered as described in data-seq.dat.
data-seq.dat contains segmentation information. The first value is the number of segments, followed by how many documents are in each segment.
word_ids.dat contains a dictionary mapping each word's ID to the word itself.
