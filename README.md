# OGD_collab_project
## Introduction
* This repository mainly applies HPE (**H**eterogeneous **P**reference **E**mbedding) to [ogbl-collab](https://ogb.stanford.edu/docs/linkprop/#ogbl-collab) dataset whose task is to predict the future author collaboration relationships given the past collaborations.
* More information about HPE can refer to this paper : 
[Query-based Music Recommendations via Preference Embedding](https://dl.acm.org/doi/10.1145/2959100.2959169)
## Requirements
* Python3
* SMORe
* OGB
## Download
In the begining, you have to execute the following code.
```
git clone --recursive https://github.com/brucenccu/OGB_collab_project
cd OGB_collab_project
./download.sh
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
#### a. Initial weights are random
```
./smore/cli/hpe -train <input_file> -save <embed_file>
```
#### b. Initial weights are given embedding of nodes. 
```
./smore/cli/hpe_node_embed -train <input_file> -save <embed_file> -embed <embed_file> -dimensions <dim>
```
#### Parameters:
```
Options Description:
    -train <string>
        the path of input file
    -save <string>
        Save the representation data
    -embed <string> (only for hpe_node_embed)
        the path of embedding file
    -dimensions <int>
        the dimensions of the input embedding file
```
#### Embedding data format:
```
//the embedding of the node 0 (0 is the index of the node)
0.1 0.2 -0.4 0.1 0.4 ...
//the embedding of the node 1 
0.2 -0.3 -0.1 0.8 0.4 ...
//the embedding of the node 2 
0.9 0.2 -0.5 0.3 0.1 ...
...
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
