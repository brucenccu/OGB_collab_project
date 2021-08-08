import sys, argparse
import random
import pickle
from collections import defaultdict
import numpy as np
from tqdm import tqdm
from sklearn import preprocessing
from ogb.linkproppred import Evaluator

parser = argparse.ArgumentParser(description='Argument Parser')
parser.add_argument('--embed', help='embedding file')
parser.add_argument('--mode', help='valid/test')
args = parser.parse_args()

if args.mode == "valid":
        pos_path = "./valid/valid_pos_edge.txt"
        neg_path = "./valid/valid_neg_edge.txt"
else:
        pos_path = "./test/test_pos_edge.txt"
        neg_path = "./test/test_neg_edge.txt"

embed_dict = {}
aver = {}
count = 0
with open(args.embed, 'r') as f:
     for line in f:
        if count !=0:
           entity_embed = line.rstrip('\n').split(' ')
           embed_dict[entity_embed[0]] = np.array(entity_embed[1:], dtype=float)
           aver[entity_embed[0]] = np.array(entity_embed[1:], dtype=float)
        else:
           count = 1

#average embedding
average = []
for key,value in aver.items():
	if len(average)==0:
		average = value
	else:
		average+=value
average = average/len(embed_dict)

#pos_edge
src = []
dest = []
with open(pos_path,'r') as f:
     for line in f:
        src.append(line.split(' ')[0])
        dest.append(line.split(' ')[1])
scores = []
for i in range(len(src)):
     try:
        scores.append(np.dot(embed_dict[src[i]],embed_dict[dest[i]]))
     except:
        if src[i] not in embed_dict.keys():
           embed_dict[src[i]] = average
        if dest[i] not in embed_dict.keys():
           embed_dict[dest[i]] = average
        scores.append(np.dot(embed_dict[src[i]],embed_dict[dest[i]]))

#neg_edge
neg_src = []
neg_dest = []
with open(neg_path,'r') as f:
     for line in f:
        neg_src.append(line.split(' ')[0])
        neg_dest.append(line.split(' ')[1])

neg_scores = []
count = 0
for i in range(len(neg_src)):
     try:
        neg_scores.append(np.dot(embed_dict[neg_src[i]],embed_dict[neg_dest[i]]))
     except:
        if neg_src[i] not in embed_dict.keys():
           embed_dict[neg_src[i]] = average
        if neg_dest[i] not in embed_dict.keys():
           embed_dict[neg_dest[i]] = average
        neg_scores.append(np.dot(embed_dict[neg_src[i]],embed_dict[neg_dest[i]]))

#evaluate
evaluator = Evaluator(name = 'ogbl-collab')
input_dict = {"y_pred_neg":np.array(neg_scores),"y_pred_pos":np.array(scores)}
result = evaluator.eval(input_dict)
print(args.mode)
print(result)
