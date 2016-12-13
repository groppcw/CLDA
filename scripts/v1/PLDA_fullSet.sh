#Need to read the start and end numbers from a file at some point.

source settings.py

rm ./subcorpora/time-all.dat

for i in $(eval echo {${START_IDX}..${END_IDX}})
do
  cat ./subcorpora/time-${i}.dat >> ./subcorpora/time-all.dat
done

cd partial_results

  echo "#!/bin/bash

    #PBS -N PLDA_chunk
    #PBS -l select=1:ncpus=${PLDA_CPUS}:mem=16gb:interconnect=mx
    #PBS -l walltime=4:00:00
    #PBS -j oe

    module add gcc
    module add mpich2

    mpiexec -n ${PLDA_CPUS} ${PLDA_LOC} \
        --num_pw ${PLDA_CHUNKS} \
        --num_topics ${GLOBAL_TOPICS} \
        --alpha 0.1 \
        --beta 0.01 \
        --training_data_file ${HERE}/subcorpora/time-all.dat \
        --model_file ${HERE}/partial_results/time-all-model \
        --total_iterations ${PLDA_ITERS}" > ./qall.sh
  qsub ./qall.sh
