# Script to download all required source codes to Downloads folder in $HOME

# This script needs to be run before running any other scripts. Ensure that all
# four source codes are downloaded before running any of the other scripts.

cd $HOME/Downloads

# Nwchem
wget https://github.com/nwchemgit/nwchem/archive/refs/tags/v7.2.2-release.tar.gz -O nwchem-v7.2.2-release.tar.gz
# eigen
wget https://gitlab.com/libeigen/eigen/-/archive/3.2.10/eigen-3.2.10.tar.gz
# openbabel
wget https://github.com/openbabel/openbabel/archive/refs/tags/openbabel-2-4-1.zip -O openbabel-openbabel-2-4-1.zip
# avogadro
wget https://github.com/cryos/avogadro/archive/refs/heads/master.zip -O avogadro-master.zip
