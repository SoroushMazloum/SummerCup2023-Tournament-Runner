#!/bin/bash

cd HoleAnalyzer/data/
rm *.rc* -v
cp ../../Logs/*.rcl* . -v
./LogExtractor.sh
cd ..
echo -e "\n"
python main.py
echo -e "\n"
