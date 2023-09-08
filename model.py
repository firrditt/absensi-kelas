import os
from keras.models import load_model
from keras.preprocessing.image import img_to_array, smart_resize
import numpy as np
from tensorflow import image

class Model():
    def __init__(self, class_names, model_path=os.path.join(os.getcwd(), 'model', 'model_1.h5')):
        self.model_path = model_path
        self.class_names = class_names

    def predict(self, img):
        model = load_model(self.model_path)
        img = img_to_array(img)
        img = image.resize(img, (299, 299))
        img = np.expand_dims(img, axis=0) / 255.
        prediction = model.predict(img)
        predicted = np.argmax(prediction)
        probabilites = prediction[0][predicted]
        prediction = self.class_names[predicted]
        return prediction, probabilites