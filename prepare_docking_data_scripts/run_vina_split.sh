#!/bin/bash
# splits the multi model files in separated files to prepare the models for vina autodock
# split multi model files will be deleted

mkdir "prepared_data"

cd data/

for f in *pdbqt; do
	cp $f ../prepared_data/$f
done

cd ..
cd ./prepared_data/

for f in *pdbqt; do
	b=`basename $f .pdbqt`

	echo Processing ligand $b
	../vina_split --input $f

	echo cleaning up...folder $b --- file $f
	rm $f
done

cd ..
