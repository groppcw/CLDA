source settings.py

#once I redo things so that it's actually running LDA too, add as an argument -c <location of that file>

${KMEANS_LOC} -o -n ${GLOBAL_TOPICS} -i ${HERE}/clustering/input.dat -t ${KMEANS_THRESHOLD} -c ${HERE}/clustering/initial.dat

mv ${HERE}/clustering/input.dat.membership ${HERE}/clustering/membership.dat
mv ${HERE}/clustering/input.dat.cluster_centres ${HERE}/clustering/centroids.raw

#~/dtm/kmeans/parallel-kmeans/seq_main -o -n 20 -i ~/dtm/plda+/scripts/final/dtm-clustering-input.normalized.dat -c ~/dtm/plda+/scripts/final/lda-comparison/lda.normalized.dat -t 0.000001
