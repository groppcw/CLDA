#Need to read the start and end numbers from a file at some point.

source settings.py

cd partial_results

for i in $(eval echo {${START_IDX}..${END_IDX}})
do

  echo "#!/bin/bash

    #PBS -N PLDA_chunk
    #PBS -l select=1:ncpus=${PLDA_CPUS}:mem=16gb:interconnect=mx
    #PBS -l walltime=4:00:00
    #PBS -j oe

    module add gcc
    module add mpich2

    mpiexec -n ${PLDA_CPUS} ${PLDA_LOC} \
        --num_pw ${PLDA_CHUNKS} \
        --num_topics ${LOCAL_TOPICS} \
        --alpha 0.1 \
        --beta 0.01 \
        --training_data_file ${HERE}/subcorpora/time-${i}.dat \
        --model_file ${HERE}/partial_results/time-${i}-model \
        --total_iterations ${PLDA_ITERS}" > ./qwindow${i}.sh
  qsub ./qwindow${i}.sh
done
