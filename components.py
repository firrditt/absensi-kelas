import streamlit as st
from utils import Utils

class Components(Utils):

    def __init__(self, camera_input="Absen"):
        self.camera_input = camera_input
        

    def uploader(self):
        imgSt = st.camera_input(self.camera_input)
        img = self.loadImageFile(imgSt) if imgSt is not None else None
        
        return img, imgSt