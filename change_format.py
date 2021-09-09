import argparse
parser = argparse.ArgumentParser(description = 'Argument Parser')
parser.add_argument('--path')
args = parser.parse_args()
#print(args.path)
new_data = []
with open(args.path,'r') as f:
    for line in f:
        tmp = line.split(' ')
        new_data.append('s_'+tmp[0]+" d_"+tmp[1]+" "+tmp[2])
        new_data.append('s_'+tmp[1]+" d_"+tmp[0]+" "+tmp[2])
print(len(new_data))
with open('./bpr_'+args.path,'w') as f:
    for line in new_data:
        f.write(line)

