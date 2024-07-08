# Script to install avogadro and all the required dependencies.

# Important: This script needs to be run as root user as `sudo bash 02_avogadro_root.sh`
# This is required as qt4 needs to be installed via the apt repositories.
# Please note that this script was tested in "Ubuntu 22.04.03 jammy" and may
# not work in other versions of Ubuntu or operating systems.

# It is assumed that the following files exists:
# - $HOME/Downloads/eigen-3.2.10.tar.gz
# - $HOME/Downloads/openbabel-openbabel-2-4-1.zip
# - $HOME/Downloads/avogadro-master.zip

# Directory where compilation will be done
cdir=/tmp/install-chemstarx
mkdir -p $cdir
cd $cdir

# Prerequisites
apt install git pkg-config -y

## Cmake
apt install cmake -y

# Qt4
add-apt-repository ppa:rock-core/qt4 -y
sed -i 's/jammy/focal/g' /etc/apt/sources.list.d/rock-core-ubuntu-qt4-jammy.list
apt update -y
apt install qt4-dev-tools libqt4-dev libqtcore4 libqtgui4 -y

# Eigen
if [[ ! -d /usr/local/include/eigen3 ]]; then
    fname=eigen-3.2.10
    cp $HOME/Downloads/${fname}.tar.gz ./
    tar -xvf ${fname}.tar.gz
    cd ${fname}
    mkdir -p build && cd build
    cmake ..
    make install
    cd $cdir
fi

# openbabel
if [[ ! -d /usr/local/include/openbabel-2.0 ]]; then
    fname=openbabel-openbabel-2-4-1
    cp $HOME/Downloads/${fname}.zip ./
    unzip ${fname}.zip
    cd ${fname}
    mkdir -p build && cd build
    cmake ..
    make -j4
    make install
    cd $cdir
fi

# Avogadro
if [[ ! -d /usr/local/include/avogadro ]]; then
    fname=avogadro-master
    cp $HOME/iiserb/Downloads/${fname}.zip ./
    unzip ${fname}.zip
    cd ${fname}
    mkdir -p build && cd build
    cmake ..
    make -j4
    make install
    cd $cdir
fi
