#!/bin/sh
# Author: Shravan
# Runs the C file on a ROOT file to fetch MCParticle and PixelCharge data

echo "Run folder name: "
read RUNFOLDER
echo "ROOT file name: "
read RUNFILE
echo "Data file name: "
read DATAFILE
CERNBOX="/eos/user/s/spyavka"
ROOTFILE="$CERNBOX/$RUNFOLDER/$RUNFILE"
SOURCEFILE="/cvmfs/clicdp.cern.ch/software/allpix-squared/3.0.3/x86_64-el9-gcc12-opt/setup.sh"
source $SOURCEFILE
root -b -l $ROOTFILE <<EOF
.L /cvmfs/clicdp.cern.ch/software/allpix-squared/3.0.3/x86_64-el9-gcc12-opt/lib/libAllpixObjects.so
.L processData.C
writeChargeData(_file0, "dut", "$DATAFILE")
EOF
# Assumes that all the .ROOT files in a folder are part of the analysis
