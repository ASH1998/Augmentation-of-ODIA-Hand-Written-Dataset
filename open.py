

import sys
import cv2
import numpy as np
from keras.models import load_model
from keras import backend as K

from sklearn.preprocessing import LabelEncoder

from subprocess import call
font = cv2.FONT_HERSHEY_SIMPLEX

cp = cv2.VideoCapture(0)
cp.set(3, 5*128)
cp.set(4, 5*128)
SIZE = 96
img_rows, img_cols = 96, 96
'''
if K.image_data_format() == 'channels_first':
    input_shape = (1, img_rows, img_cols)
    first_dim = 0
    second_dim = 1
else:
    input_shape = (img_rows, img_cols, 1)
    first_dim = 0
    second_dim = 3
'''
input_shape = (1, img_rows, img_cols)
first_dim = 0
second_dim = 1



def annotate(frame, label, location = (20,30)):
    #writes label on image#

    cv2.putText(frame, label, location, font,
                fontScale = 0.5,
                color = (255, 255, 0),
                thickness =  1,
                lineType =  cv2.LINE_AA)


def extract_digit(frame, rect, pad = 10):
    x, y, w, h = rect
    cropped_digit = final_img[y-pad:y+h+pad, x-pad:x+w+pad]
    cropped_digit = cropped_digit/255

    #only look at images that are somewhat big:
    if cropped_digit.shape[0] >= 48 and cropped_digit.shape[1] >= 48:
        cropped_digit = cv2.resize(cropped_digit, (SIZE, SIZE))
    else:
        return
    return cropped_digit


def img_to_mnist(frame, tresh = 90):
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    #adaptive here does better with variable lighting:
    
    gray_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY_INV, blockSize = 127, C = 2)
    
    #gray_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
    #                                 cv2.THRESH_BINARY_INV, blockSize = 127, C = 2)
    return gray_img


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("loading model")
model = load_model("542019.h5")

labelz = dict(enumerate([ "one", "two", "three", "four",
                         "five", "six", "seven", "eight", "nine", "zero"]))


for i in range(1000):
    ret, frame = cp.read(0)

    final_img = img_to_mnist(frame)
    image_shown = frame
    contours, _ = cv2.findContours(final_img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    rects = [cv2.boundingRect(contour) for contour in contours]
    rects = [rect for rect in rects if rect[2] >= 2 and rect[3] >= 8]

    #draw rectangles and predict:
    for rect in rects:

        x, y, w, h = rect

        if i >= 0:

            mnist_frame = extract_digit(frame, rect, pad = 0)

            if mnist_frame is not None: #and i % 25 == 0:
                mnist_frame = np.expand_dims(mnist_frame, first_dim) #needed for keras
                mnist_frame = np.expand_dims(mnist_frame, second_dim) #needed for keras
                #print(mnist_frame.shape)
                class_prediction = model.predict_classes(mnist_frame, verbose = False)[0]
                #print(model.predict_proba(mnist_frame))
                prediction = np.around(np.max(model.predict(mnist_frame, verbose = False)), 2)
                label = str(prediction) # if you want probabilities
                #print(label)

                cv2.rectangle(image_shown, (x - 15, y - 15), (x + 15 + w, y + 15 + h),
                              color = (255, 255, 0))

                label = labelz[class_prediction]

                #print(label)

                annotate(image_shown, label, location = (rect[0], rect[1]))

    cv2.imshow('frame', image_shown)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break