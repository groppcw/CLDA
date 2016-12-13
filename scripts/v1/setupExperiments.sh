for i in {0..4}
do
  dirname="EXPERIMENT-heldout-${i}"
  mkdir $dirname
  cp *.py $dirname
  cp *.sh $dirname
  mkdir ${dirname}/clustering
  mkdir ${dirname}/input_data
  mkdir ${dirname}/local_models
  mkdir ${dirname}/mixtures
  mkdir ${dirname}/partial_results
  mkdir ${dirname}/perplexity
  mkdir ${dirname}/results
  mkdir ${dirname}/subcorpora
  mkdir ${dirname}/top_words
  cp input_data/* ${dirname}/input_data

done
