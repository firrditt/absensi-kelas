from PIL import Image
import streamlit as st
from model import Model
import pandas as pd

class Utils():
    def __init__(self, class_names, excel_path='datasets/data_absensi.xlsx'):
        self.class_names = class_names
        self.excel_path = excel_path

    def loadImageFile(self, img):
        try:
            return Image.open(img)
        except Exception:
            st.error('Tidak bisa menampilkan gambar')
            return None
    
    def getPrediction(self, img):
        try:
            model = Model(class_names=self.class_names)
            prediction, probabilitas = model.predict(img)
            return prediction, probabilitas
        except:
            return None
        
    def getData(self):
        return pd.read_excel(self.excel_path)
    
    def postAbsen(self, data):
        df = self.getData()
        new_df = pd.DataFrame([data])
        combined_df = pd.concat([df, new_df], ignore_index=True)
        combined_df.to_excel(self.excel_path, sheet_name='Sheet1', index=False)
        return combined_df
    
    def fillnaAbsen(self, data):
        df = self.getData()
        new_df = pd.DataFrame([data])
    