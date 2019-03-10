import numpy as np
from PIL import Image
import os
import random
from tqdm import trange

'''
img = Image.open(r'E:\Python Coding\ODIA DATASET\AugmentedData\1\1_0_40.png')
arr = np.asarray(img)

print(arr[3])
'''

DataDir = "E:\Python Coding\ODIA DATASET\ShuffledData"

sub_dir = os.listdir(DataDir)
random.shuffle(sub_dir)

train_data = []
labels = []

#print(sub_dir)
#['1', '10', '2', '3', '4', '5', '6', '7', '8', '9']
'''
for i in range(len(sub_dir)):
    cur_loc = DataDir + '\\' + sub_dir[i]
    images = os.listdir(cur_loc)
    for j in range(len(images)):
        img = Image.open(cur_loc + '\\' + images[j])
        arr = np.asarray(img)
        train_data.append(arr)
        labels.append(int(sub_dir[i]))
    print(sub_dir[i], ' over...')

np.save()
'''

for i in trange(len(sub_dir)):
    cur_loc = DataDir + '\\' + sub_dir[i]
    img = Image.open(cur_loc).convert('L')
    arr = np.asarray(img)
    train_data.append(arr)
    label = sub_dir[i].split('_')[0]
    labels.append(int(label))

np.save('train.npy', train_data)
np.save('labels.npy', labels)