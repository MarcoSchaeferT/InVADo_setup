#!/bin/bash
sh ./install_autodock.sh
sh ./run_vina_split.sh

# single
#sh ./run_AutoDock_vina.sh

sudo apt-get install python3-pip -y
pip install joblib
# in parallel
python3 ./parallelAutoDock.py
cd results
python3 ../handleDuplicates.py

echo "all jobs finsihed!"