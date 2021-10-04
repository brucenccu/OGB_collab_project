#!/bin/bash

DIM=64
SAMPLETIME=10
THREADS=1
UNDIRECTED=1

i=1;
j=$#;
c=$(($j%2))
echo $c
if [ $(($j%2)) != 0 ]; then    
    echo "the arguments are not correct!"
    exit 1;
fi

while [ $i -le $j ] 
do
    #echo "$i: $1";
    case "$1" in
        "-train")
            shift 1
            TRAINFILE=$1
            #echo "$i: $1"; 
            #echo "train argument"
        ;;
        "-save")
            shift 1
            SAVEFILE=$1
            #echo "$i: $1"; 
            #echo "save argument"
        ;;
        "-field") 
            shift 1
            FIELDFILE=$1
            #echo "$i: $1"; 
            #echo "field argument"
        ;;
        "-dim")
            shift 1
            DIM=$1
            #echo "$i: $1"; 
            #echo "dim argument"
        ;;
        "-sample_times") 
            shift 1
            SAMPLETIME=$1
            #echo "$i: $1"; 
            #echo "sample_times argument"
        ;;
        "-model")
            shift 1
            MODEL=$1
            #echo "$i: $1"; 
            #echo "model argument"
        ;;
        "-embed")
            shift 1;
            EMBED=$1
            #echo "$i: $1"
            #echo "embed argument"
        ;;
        "-threads")
            shift 1;
            THREADS=$1
            #echo "$i : $1"
            #echo "thread argument"
        ;;
        "-undirected")
            shift 1;
            UNDIRECTED=$1
            #echo "$i : $1"
            #echo "undirected argument"
        ;;
        *) echo "error"
           exit 1;
        ;;
    esac
    i=$((i + 2));
    shift 1;
done

#echo $TRAINFILE
#echo $SAVEFILE
#echo $FIELDFILE
#echo $DIM
#echo $SAMPLETIME
#echo $MODEL

if [ $MODEL = "HOPREC" ] && [ -z $FIELDFILE ];
then
    echo -e "You should give a field file for HOP-REC model!"
    exit 1
fi

if [ $MODEL = "HPE" ]
then
    echo -e "Training HPE embedding ..."
    ./smore/cli/hpe -train $TRAINFILE -save $SAVEFILE -dimensions $DIM -sample_times $SAMPLETIME -threads $THREADS
    echo -e "Start to predict ...."
    python3 ./predict.py --embed $SAVEFILE --input_dim $DIM --undirected $UNDIRECTED 
fi

if [ $MODEL = "BPR" ]
then
    echo -e "Training BPR embedding ..."
    ./smore/cli/bpr -train $TRAINFILE -save $SAVEFILE -dimensions $DIM -sample_times $SAMPLETIME -threads $THREADS
    echo -e "Start to predict ...."
    python3 ./predict.py --embed $SAVEFILE --input_dim $DIM --undirected $UNDIRECTED
fi

if [ $MODEL = "WARP" ]
then
    echo -e "Training WARP embedding ..."
    ./smore/cli/warp -train $TRAINFILE -save $SAVEFILE -dimensions $DIM -sample_times $SAMPLETIME -threads $THREADS
    echo -e "Start to predict ...."
    python3 ./predict.py --embed $SAVEFILE --input_dim $DIM --undirected $UNDIRECTED 
fi


if [ $MODEL = "HOPREC" ]
then
    echo -e "Training HOP-REC embedding ..."
    ./smore/cli/hoprec -train $TRAINFILE -save $SAVEFILE -field $FIELDFILE -dimensions $DIM -sample_times $SAMPLETIME -threads $THREADS
    echo -e "Start to predict ...."
    python3 ./predict.py --embed $SAVEFILE --input_dim $DIM --undirected $UNDIRECTED 
fi
