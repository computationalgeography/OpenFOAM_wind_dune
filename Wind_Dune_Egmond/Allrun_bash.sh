#!/bin/sh
#  cd ${0%/*} || exit 1    # Run from this directory





module load UCC/1.0.0-GCCcore-11.3.0   #    USS/2020 
#   module load slurm
module load GCC/11.3.0                 #gcc/7.3.0
module load OpenMPI/4.1.4-GCC-11.3.0       #openmpi/3.1.3
module load OpenFOAM/10-foss-2022a     #openfoam-org/10.0


source /opt/easybuild/foss2022a/software/OpenFOAM/10-foss-2022a/OpenFOAM-10/etc/bashrc



: <<'END'
# Source tutorial run functions
. $WM_PROJECT_DIR/bin/tools/RunFunctions

# Copy motorbike surface from resources directory
cp $FOAM_TUTORIALS/resources/geometry/motorBike.obj.gz constant/geometry/
runApplication surfaceFeatures

runApplication blockMesh

runApplication decomposePar -copyZero
runParallel snappyHexMesh -overwrite

runParallel patchSummary
runParallel potentialFoam
runParallel $(getApplication)

runApplication reconstructParMesh -constant
runApplication reconstructPar -latestTime

END

# Source tutorial run functions
. $WM_PROJECT_DIR/bin/tools/RunFunctions

# Copy motorbike surface from resources directory
# cp $FOAM_TUTORIALS/resources/geometry/motorBike.obj.gz constant/geometry/
# runApplication surfaceFeatures

#runApplication blockMesh

runApplication decomposePar -copyZero
# runParallel snappyHexMesh -overwrite

# runParallel patchSummary
runParallel potentialFoam
runParallel $(getApplication)

# runApplication reconstructParMesh -constant
runApplication reconstructPar     # runApplication reconstructPar -latestTime


#------------------------------------------------------------------------------
