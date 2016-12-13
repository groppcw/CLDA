source settings.py

cd ${HERE}/partial_results #should dump the logfiles into partial_results
module add gcc

for i in $(eval echo {${START_IDX}..${END_IDX}})
do

  infile="${HERE}/subcorpora/time-${i}.dat"
  if ((HOLDOUT_MOD > 0)); then
    infile="${HERE}/subcorpora/time-${i}-holdout.dat"
  fi

  ${PLDA_INFER_LOC} \
        --alpha 0.1 \
        --beta 0.01 \
        --inference_data_file ${infile} \
        --inference_result_file $HERE/mixtures/time-${i}.withCentroids \
        --model_file ${HERE}/local_models/time-${i}.bigCentroids \
        --total_iterations ${PLDA_INFER_ITERS} \
        --burn_in_iterations ${PLDA_INFER_BURN_IN}
done
