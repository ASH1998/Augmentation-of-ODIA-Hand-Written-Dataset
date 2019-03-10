from PIL import Image, ImageOps
import os
from tqdm import trange

'''
DIR_NAME = "D:\Downloads\ODIA DATASET\\1"
SAVE_DIR = "D:\Downloads\ODIA DATASET\SAVED_1"
SIZE = 96
ListImages = os.listdir(DIR_NAME)

for i in trange(len(ListImages)):
    current_add  = DIR_NAME+ "\\" + ListImages[i]
    img = Image.open(current_add).convert('L')
    #img.resize((SIZE, SIZE), Image.ANTIALIAS)
    new_img = ImageOps.fit(img, (SIZE, SIZE), Image.ANTIALIAS)
    to_save = SAVE_DIR + '\\'+ str(i) +'.jpg'
    new_img.save(to_save)
#img = img.resize((SIZE, SIZE), Image.ANTIALIAS)
#img.save("output.jpg")
'''

DataDIR = "E:\Python Coding\ODIA DATASET\Data"
SaveDIR = "E:\Python Coding\ODIA DATASET\\NewData"
SIZE = 96

subdirs = os.listdir(DataDIR)

#curr_dir = DataDIR+"\\"+subdirs[2]
#j = os.listdir(curr_dir)
#print(j)

for i in range(len(subdirs)):
    curr_dir = DataDIR + '\\' + subdirs[i]
    os.makedirs(SaveDIR + "\\" + subdirs[i])
    image_names = os.listdir(curr_dir)
    for j in trange(len(image_names)):
        image_loc = curr_dir + '\\' + image_names[i]
        img = Image.open(image_loc).convert('L')
        new_img = ImageOps.fit(img, (SIZE, SIZE), Image.ANTIALIAS)
        save_dir = SaveDIR + "\\" + subdirs[i] + '\\' + subdirs[i] + '_' + str(j) + '.jpg'
        new_img.save(save_dir)
    
    print(subdirs[i], "Over...")
