import os
from keras.models import load_model
from keras.preprocessing.image import img_to_array, smart_resize
import numpy as np
from tensorflow import reshape

class Model():
    def __init__(self, model_path=os.path.join(os.getcwd(), 'model', 'model.h5')):
        self.model_path = model_path
        self.class_names = ['adjie', 'andre', 'fikar', 'fuad', 'raudi', 'riyan', 'vio']

    def predict(self, image):
        model = load_model(self.model_path)
        img = img_to_array(image)
        img = smart_resize(img, (224, 224))
        img /= 255
        img = np.expand_dims(img, axis=0)
        images = np.vstack([img])
        prediction = model.predict(img)
        predicted = np.argmax(prediction)
        probabilites = prediction[0][predicted]
        prediction = self.class_names[predicted]
        return prediction, probabilites