from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os
#from tqdm import trange

datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=False,
        fill_mode='nearest',)

SaveDIR = "E:\Python Coding\ODIA DATASET\\AugmentedData"
DataDIR = "E:\Python Coding\ODIA DATASET\\NewData"

sub_dir = os.listdir(DataDIR)

for k in range(len(sub_dir)):
    
    images_loc = os.listdir(DataDIR + '\\' + sub_dir[k])
    os.makedirs(SaveDIR + '\\' + sub_dir[k])

    for j in range(len(images_loc)):

        img = load_img(DataDIR + '\\' + sub_dir[k] +'\\' + images_loc[j])  # this is a PIL image
        x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
        x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

        # the .flow() command below generates batches of randomly transformed images
        # and saves the results to the `preview/` directory
        i = 0
        for batch in datagen.flow(x, batch_size=1,save_to_dir=SaveDIR+"\\"+sub_dir[k], save_prefix=sub_dir[k],):
            i += 1
            if i > 20:
                break
    print(sub_dir[k], 'is over...')