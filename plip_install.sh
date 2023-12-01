#!/bin/bash
TMP=$PWD/tmp_plipInstall
mkdir tmp_plipInstall
echo "$TMP"
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install swig -y
sudo apt-get install python3-pip -y
sudo apt-get install -y rapidjson-dev
sudo apt-get install openbabel -y
sudo apt install unzip
cp plip-2.2.2.zip $TMP/plip-2.2.2.zip
cd $TMP
wget https://github.com/openbabel/openbabel/archive/refs/tags/openbabel-3-1-1.tar.gz
sudo tar -zxvf openbabel-3-1-1.tar.gz 
TMP1=$TMP/openbabel-openbabel-3-1-1
echo "$TMP1"
cd $TMP1
sudo apt-get install build-essential -y
TMP2=$TMP1/build
mkdir $TMP2
sudo apt install cmake -y
#sudo apt-get install python-dev -y
echo "$TMP2"
cd $TMP2
sudo cmake -DRUN_SWIG=ON $TMP1
sudo make -j6 install 
pip install openbabel
sudo apt-get install pymol -y
cd $TMP
#sudo git clone https://github.com/pharmai/plip.git
sudo git clone https://github.com/MarcoSchaeferT/plip.git
TMP3=$TMP/plip
#sudo unzip plip-2.2.2.zip
#TMP3=$TMP/plip-2.2.2
echo "$TMP3"
cd $TMP3
sudo python3 setup.py install
sudo pip install plip
cd ..

