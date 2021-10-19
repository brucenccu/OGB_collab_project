import torch

val_scores = []
test_scores = []
with open('score.txt','r') as f:
    for line in f:
        val_scores.append(float(line.strip('\n').split(' ')[0]))
        test_scores.append(float(line.strip('\n').split(' ')[1]))

print("Valid Hit: \n\thits@50 : {:.4f} ± {:.4f}".format(float(torch.mean(torch.tensor(val_scores))),float(torch.std(torch.tensor(val_scores)))))
print("Test Hit: \n\thits@50 : {:.4f}  ±{:.4f}".format(float(torch.mean(torch.tensor(test_scores))),float(torch.std(torch.tensor(test_scores)))))
