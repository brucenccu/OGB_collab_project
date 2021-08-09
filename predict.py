import sys, argparse
import numpy as np
from tqdm import tqdm
from ogb.linkproppred import Evaluator


def get_cos_score(edge_path,embed_dict,average):
     src = []
     dest = []
     with open(edge_path,'r') as f:
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
     return scores

parser = argparse.ArgumentParser(description='Argument Parser')
parser.add_argument('--embed', help='embedding file')
#parser.add_argument('--mode', help='valid/test')
args = parser.parse_args()

val_pos_path = "./valid/valid_pos_edge.txt"
val_neg_path = "./valid/valid_neg_edge.txt"
test_pos_path = "./test/test_pos_edge.txt"
test_neg_path = "./test/test_neg_edge.txt"

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


val_scores = get_cos_score(val_pos_path,embed_dict,average)
val_neg_scores = get_cos_score(val_neg_path,embed_dict,average)

test_scores = get_cos_score(test_pos_path,embed_dict,average)
test_neg_scores = get_cos_score(test_neg_path,embed_dict,average)
#evaluate
evaluator = Evaluator(name = 'ogbl-collab')
val_input_dict = {"y_pred_neg":np.array(val_neg_scores),"y_pred_pos":np.array(val_scores)}
val_result = evaluator.eval(val_input_dict)
print("Valid_Hit:")
print("\thits@50 : ",val_result['hits@50'])
test_input_dict = {"y_pred_neg":np.array(test_neg_scores),"y_pred_pos":np.array(test_scores)}
test_result = evaluator.eval(test_input_dict)
print("Test_Hit:")
print("\thits@50 : ",test_result['hits@50'])
