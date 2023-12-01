#!/bin/bash
sudo apt-get update 
sudo apt-get upgrade -y
sudo apt-get install wget
wget https://github.com/ccsb-scripps/AutoDock-Vina/releases/download/v1.1.2-boost-new/vina_1.1.2-boost-new_linux_x86_64
wget https://github.com/ccsb-scripps/AutoDock-Vina/releases/download/v1.2.4/vina_split_1.2.4_linux_x86_64
mv vina_1.1.2-boost-new_linux_x86_64 vina
mv vina_split_1.2.4_linux_x86_64 vina_split