import io
from PIL import Image
import requests
import streamlit as st
from model import Model
from json import load
import requests
import webbrowser
import os

class Utils():
    def __init__(self, error_file="Cannot Upload File. Please try again !"):
        self.error_file = error_file

    def loadImageFile(self, img):
        try:
            return Image.open(img)
        except Exception:
            st.error(self.error_file)
            return None
    
    def getPrediction(self, img):
        try:
            model = Model()
            prediction, probabilitas = model.predict(img)
            return prediction, probabilitas
        except:
            return None
