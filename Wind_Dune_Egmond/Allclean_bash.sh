#!/bin/sh
#     cd ${0%/*} || exit 1    # Run from this directory


module load UCC/1.0.0-GCCcore-11.3.0   #    USS/2020 
#   module load slurm
module load GCC/11.3.0                 #gcc/7.3.0
module load OpenMPI/4.1.4-GCC-11.3.0       #openmpi/3.1.3
module load OpenFOAM/10-foss-2022a     #openfoam-org/10.0


source /opt/easybuild/foss2022a/software/OpenFOAM/10-foss-2022a/OpenFOAM-10/etc/bashrc




# Source tutorial clean functions
. $WM_PROJECT_DIR/bin/tools/CleanFunctions

# Remove surface and features
rm -f constant/geometry/motorBike.obj.gz

cleanCase
cleanExplicitFeatures

#------------------------------------------------------------------------------
