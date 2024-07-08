# Script to install nwchem and modify PYTHONPATH when loading environment so
# that custom python functions can be used in nwchem calculations.

# conda is assumed to be installed. Please modify $condabin variable with the
# location to the conda executable. 
# Also, It is assumed that $HOME/Downloads/nwchem-v7.2.2-release.tar.gz exists

condabin=$HOME/anaconda3/bin/conda

# Install NWCHEM in conda environment
eval "$($condabin shell.bash hook)"
if conda info --envs | grep -q chemstarx; then
    echo "Environment exists"
else
    conda create -n chemstarx -y
fi
conda activate chemstarx
conda install -c conda-forge nwchem matplotlib ase -y

# Add Nwchem contrib/python to PYTHONPATH
if [[ ! -f $CONDA_PREFIX/etc/conda/activate.d/nwchem_pythonpath.sh ]]; then
    mkdir $CONDA_PREFIX/share/nwchem_source
    tar -xvf $HOME/Downloads/nwchem-v7.2.2-release.tar.gz -C $CONDA_PREFIX/share/nwchem_source
    echo 'export PYTHONPATH=$CONDA_PREFIX/share/nwchem_source/nwchem-7.2.2-release/contrib/python:$PYTHON_PATH' > $CONDA_PREFIX/etc/conda/activate.d/nwchem_pythonpath.sh
fi
