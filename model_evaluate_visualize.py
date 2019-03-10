from keras.models import load_model
from keras import backend as k
k.set_image_dim_ordering('th')

from matplotlib import pyplot as plt
from keras.preprocessing.image import img_to_array, load_img
SIZE = 96
img_path = r"E:\Python Coding\ODIA DATASET\NewData\9\9_22.jpg"
path2 = r"E:\Python Coding\ODIA DATASET\NewData\3\3_56.jpg"


model = load_model('second_99accuracymodel.h5')
print("MODEL loaded")
img = load_img(img_path, color_mode='grayscale', target_size=(SIZE, SIZE))
x = img_to_array(img)
x = x.reshape((1,) + x.shape)
print(x.shape)
print(model.predict_classes(x))
plt.imshow(img)
plt.show()

