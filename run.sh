#!/bin/bash

FILE1=$1
FILE2='./data/embed'

echo -e "Training HPE embedding..."
./smore/cli/hpe -train $FILE1 -save $FILE2 -dimension $2

echo -e "Start to predict..."
python3 ./predict.py --embed $FILE2
