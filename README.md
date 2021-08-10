# OGD_collab_project
## Introduction
* This repository mainly applies HPE (**H**eterogeneous **P**reference **E**mbedding) to [ogbl-collab](https://ogb.stanford.edu/docs/linkprop/#ogbl-collab) dataset whose task is to predict the future author collaboration relationships given the past collaborations.
* More information about HPE can refer to the following paper : 
[Query-based Music Recommendations via Preference Embedding](https://dl.acm.org/doi/10.1145/2959100.2959169)
## Requirements
* Python3
* SMORe
* OGB
## Download
```
git clone --recursive https://github.com/brucenccu/OGB_collab_project
```
## SMORe Compilation
```
cd OGB_collab_project/smore
make
```
## Usage
### 1. Input data format:
```
nodeA nodeB 1
nodeB nodeC 3
nodeA nodeD 2
nodeB nodeE 1
nodeD nodeE 2
```
### 2. Get the HPE file
```
./smore/cli/hpe -train <input_file> -save <embed_file>
```
You can get more usages from [SMORe](https://github.com/cnclabs/smore).

### 3. Make prediction to obtain the Hit@50 result.
#### Run:
```
python3 predict.py --embed <embed_file> --input_dim <dimensions>
```
#### Parameters:
```
Options Description:
    --embed <string>
        the path of input embedding file
    --dimension <int>
        the dimensions of the input embedding file
```
## Example script
Here, you can use the `run.sh` to run through the whole predict task.
#### Run:
```
./run.sh <input_file_path> <dimension>
```
#### Parameters:
```
Options Description:
    <input_file_path> <string>
        the path of input input file
    <dimension> <int>
        the dimensions of the output embedding file by SMORe
```
