#!/bin/bash
mkdir -p results
cd prepared_data/

for f in *.pdbqt; do
	b=`basename $f .pdbqt`
	echo Processing ligand $b
	mkdir -p ../results/$b
	vina --config ../conf.txt --ligand $f --out ../results/${b}/${b}_res.pdbqt --log ../results/${b}/${b}_log.txt
	echo "./"${b}"/"${b}"_res.pdbqt" >> ../results/results_list.txt
done
