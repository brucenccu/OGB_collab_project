# OGB_collab_project
## Introduction
* This repository mainly applies **HPE** ,**BPR** ,**WARP**, **HOP-REC** to [ogbl-collab](https://ogb.stanford.edu/docs/linkprop/#ogbl-collab) dataset whose task is to predict the future author collaboration relationships given the past collaborations.
* More information about models can refer to these papers : 
1. **HPE** : [Query-based Music Recommendations via Preference Embedding](https://dl.acm.org/doi/10.1145/2959100.2959169)
2. **BPR** : [BPR: Bayesian personalized ranking from implicit feedback](https://dl.acm.org/doi/10.5555/1795114.1795167)
3. **WARP** : [WSABIE: Scaling Up To Large Vocabulary Image Annotation](https://dl.acm.org/doi/10.5555/2283696.2283856) , [Learning to Rank Recommendations with the k-Order Statistic Loss](https://dl.acm.org/doi/10.1145/2507157.2507210)
4. **HOP-REC** : [HOP-Rec: High-Order Proximity for Implicit Recommendation](https://dl.acm.org/doi/10.1145/3240323.3240381)
## Requirements
* Python3
* SMORe
* OGB
## Quick Start
1. Clone the repository
```
git clone --recursive https://github.com/brucenccu/OGB_collab_project
```
or you can execute following code
```
git clone https://github.com/brucenccu/OGB_collab_project
cd OGB_collab_project
git submodule init
git submodule update
```
2. Download the dataset and compile the SMORe
```
cd OGB_collab_project
./prepare.sh
```
3. If there isn't any error, you can use ```run.sh``` to get the prediction. (```field_make.py``` is just for ```HOPREC```)
```
python3 field_make.py --path ./data/train/train_valid_2010.txt 
./run.sh -model HOPREC -train ./data/train/train_valid_2010.txt -save ./data/train/embed -field ./data/train/field.txt -dim 128 -sample_times 500 -threads 8 -undirected 1
```
Note : You can get more usage below.
## Usage
### 1. Input data format:
- training data
```
nodeA nodeB 1
nodeB nodeC 3
nodeA nodeD 2
nodeB nodeE 1
nodeD nodeE 2
```
- field data (HOP-REC) : to assign the field of each vertex (user or item)
```
nodeA u
nodeB u
nodeC u
nodeD u 
nodeE u
```
### 2. Get the embedding file
#### a. Initial weights are random
```
./smore/cli/<model name> -train <input_file> -save <embed_file>

Usage: 
./smore/cli/hpe -train ./train.txt -save ./embed
```
#### b. Initial weights are given embedding of nodes. 
```
./smore/cli/<model_name>_node_embed -train <input_file> -save <embed_file> -embed <embed_file> -dimensions <dim>

Usage: 
./smore/cli/hpe_node_embed -train ./train.txt -save ./embed
```
#### Parameters:
```
Options Description:
    -train <string>
        the path of input file
    -save <string>
        Save the representation data
    -embed <string> (only for models whose initial weights are given embeddings of nodes)
        the path of embedding file
    -dimensions <int>
        the dimensions of the input embedding file
```
#### Pretrained embedding data format:
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
python3 predict.py --embed <embed_file> --input_dim <dimensions> --undirected <directions>
python3 logger.py
```
#### Parameters:
```
Options Description:
    --embed <string>
        the path of input embedding file
    --dimension <int>
        the dimensions of the input embedding file
    --undirected <int>
        whether the input graph is undirected or not (1/0)
```
## Example script
Here, you can use the `run.sh` to run through the whole predict task.
#### Run:
```
./run.sh -model <model_name> -train <input_file_path> -save <save_file_path> 
```
#### Parameters:
```
Options Description:
    -model 
        name of the model you want to use.(HPE/BPR/WARP/HOPREC/<model_name>_node_embed)
    -field (optional)
        the path of the field data (HOP-REC)
    -train
        the path of input file
    -save 
        the path od output embedding file
    -embed (optional)
        the path od pretrained node embedding file
    -dim 
        the dimensions of the vertex representation; default is 64
    -sample_times 
        number of training samples *Million; default is 10
    -threads
        number of training threads; default is 1
    -undirected
        whether the input graph is undirected or not; default is 1
```
## Experiment 
In addition to using the original dataset, we also filter out edges with a closer year to be the new dataset.The following descriptions are about different datasets.
- **train_all** : all edges until 2017
- **train_2015** : all edges from 2015 - 2017
- **train_valid_all** : all edges until 2018
- **train_valid_2010** : all edges from 2010 - 2018
- **train_valid_2015** : all edges from 2015 - 2018

### HOPREC for five different datasets

#### (sample_times = 500, dimensions = 128, alpha = 0.025)
|                  | Without Pretrained (valid/test) | with Pretrained (valid/test) |
|:----------------:|:-------------------------------:|:----------------------------:|
|    train_all     |         0.6588 / 0.5596         |       0.6639 / 0.5682        |
|    train_2015    |         0.6410 / 0.5426         |       0.6516 / 0.5551        |
| train_valid_all  |         1.000 / 0.6687          |       0.9995 / 0.6805        |
| train_valid_2015 |         1.000 / 0.6670          |        1.000 / 0.6741        |
| train_valid_2010 |         1.000 / 0.7005          |        1.000 / 0.7077        |

The result of other models can be referred to this [report](https://docs.google.com/document/d/1zPKYJFE1OJ6IcmO7ZirHIOZboVWQgbzMPGBNZxLSZKo/edit?usp=sharing).
