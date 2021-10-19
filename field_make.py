import argparse
import tqdm
parser = argparse.ArgumentParser(description = 'Argument Parser')
parser.add_argument('--path')
args = parser.parse_args()
#print(args.path)
new_data = []
field_data = {}
with open(args.path,'r') as f:
    for line in f:
        tmp = line.split(' ')
        if tmp[0] not in field_data.keys():
            field_data[tmp[0]] = 1
        if tmp[1] not in field_data.keys():
            field_data[tmp[1]] = 1
        new_data.append('s_'+tmp[0]+" d_"+tmp[1]+" "+tmp[2])
        new_data.append('s_'+tmp[1]+" d_"+tmp[0]+" "+tmp[2])
#print(len(new_data))
with open('./field.txt','w') as f:
    for key,value in field_data.items():
        f.write(str(key)+" s\n")
