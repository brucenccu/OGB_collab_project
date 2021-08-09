import argparse
from tqdm import tqdm
import numpy as np
import scipy.sparse as ssp
import torch
from torch.utils.data import DataLoader
from torch_geometric.data import Data, Dataset, DataLoader
from ogb.linkproppred import PygLinkPropPredDataset, Evaluator
from torch_geometric.utils import to_undirected

def CN(A, edge_index, batch_size=100000):
	# The Common Neighbor heuristic score.
    link_loader = DataLoader(range(edge_index.size(1)), batch_size)
    scores = []
    for ind in tqdm(link_loader):
        src, dst = edge_index[0, ind], edge_index[1, ind]
        cur_scores = np.array(np.sum(A[src].multiply(A[dst]),1)).flatten()
        scores.append(cur_scores)
    return torch.FloatTensor(np.concatenate(scores, 0))

def AA(A, edge_index, batch_size=100000):
    # The Adamic-Adar heuristic score.
    multiplier = 1 / np.log(A.sum(axis=0))
    multiplier[np.isinf(multiplier)] = 0
    A_ = A.multiply(multiplier).tocsr()
    link_loader = DataLoader(range(edge_index.size(1)), batch_size)
    scores = []
    for ind in tqdm(link_loader):
        src, dst = edge_index[0, ind], edge_index[1, ind]
        cur_scores = np.array(np.sum(A[src].multiply(A_[dst]), 1)).flatten()
        scores.append(cur_scores)
    scores = np.concatenate(scores, 0)
    return torch.FloatTensor(scores)

parser = argparse.ArgumentParser()
parser.add_argument('--method',type = str,default = "CN",help ="CN or AA")
args = parser.parse_args()

dataset = PygLinkPropPredDataset(name="ogbl-collab")
split_edge = dataset.get_edge_split()
data = dataset[0]

num_nodes = data.num_nodes #the num of nodes in the dataset
if 'edge_weight' in data:
    edge_weight = data.edge_weight.view(-1)
else:
    edge_weight = torch.ones(data.edge_index.size(1),dtype = int)


val_edge_index = split_edge['valid']['edge'].t()
val_edge_src = torch.cat((val_edge_index[0],val_edge_index[1]),0)
val_edge_dest = torch.cat((val_edge_index[1],val_edge_index[0]),0)
val_edge = torch.stack((val_edge_src,val_edge_dest),0)
val_edge_weight = torch.ones(val_edge.size(1),dtype = int)

train_val_edge = torch.cat((data.edge_index,val_edge),1)
train_val_weight = torch.cat((edge_weight,val_edge_weight),0)
'''print(edge_weight)
print(val_edge_weight)
print(train_val_weight)'''

#A: Graph composed of nodes in training data
#B: Graph composed of nodes in training data and validation data
A = ssp.csr_matrix((edge_weight,(data.edge_index[0],data.edge_index[1])),shape = (num_nodes,num_nodes))
B = ssp.csr_matrix((train_val_weight,(train_val_edge[0],train_val_edge[1])),shape = (num_nodes,num_nodes))


val_pos_edge = split_edge['valid']['edge'].t()
val_neg_edge = split_edge['valid']['edge_neg'].t()
test_pos_edge = split_edge['test']['edge'].t()
test_neg_edge = split_edge['test']['edge_neg'].t()

#get CN/AA scores of given edges
val_pos_pred = eval(args.method)(A, val_pos_edge)
val_neg_pred = eval(args.method)(A, val_neg_edge)
test_pos_pred = eval(args.method)(B, test_pos_edge)
test_neg_pred = eval(args.method)(B, test_neg_edge)


#evaluate
evaluator = Evaluator(name = 'ogbl-collab')
val_input_dict = {"y_pred_neg":np.array(val_neg_pred),"y_pred_pos":np.array(val_pos_pred)}
val_result = evaluator.eval(val_input_dict)
print("Method: ",args.method)
print("Valid_Hit:")
print("\thits@50 : ",val_result['hits@50'])
test_input_dict = {"y_pred_neg":np.array(test_neg_pred),"y_pred_pos":np.array(test_pos_pred)}
test_result = evaluator.eval(test_input_dict)
print("Test_Hit:")
print("\thits@50 : ",test_result['hits@50'])
