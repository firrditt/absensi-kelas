import streamlit as st
from utils import Utils
from components import Components
from PIL import Image
import pandas as pd
from json import load



class Pages():
    f = open('languages.json')
    data_languages = load(f)
    
    def __init__(self):
        self.data_lng = self.data_languages['id']
        self.lang = 'id'

    def home(self):
        st.title(self.data_lng['title'])
        st.write(self.data_lng['title_desc'])
        img = Image.open('assets/Logo_gunadarma.png')
        new_width = 100
        new_height = 100
        new_size = (new_width, new_height)
        img_resized = img.resize(new_size, Image.BICUBIC)
        st.image(img_resized)
        if st.button('Absen'):
            st.session_state.pages = 'Absensi'
            
    def predict(self):
        st.title(self.data_lng['title_predict'])
        utils = Utils(
            error_file=self.data_lng['error_file'],
        )

        
        imgSt = st.camera_input('Take a picture')
        img = utils.loadImageFile(imgSt) if imgSt is not None else None
        

        if imgSt and img:
            with st.spinner('Please wait'):
                prediction, probabilities = utils.getPrediction(img)
                if probabilities < 0.85:
                    st.title('Wajah tidak dikenali')
                else:
                    result = prediction.capitalize() if prediction is not None else ''
                    col1, col2 = st.columns([2, 2])
                    col1.subheader(self.data_lng['prediction_result'])
                    col1.image(imgSt, use_column_width=True, clamp=True)

                    col2.subheader('Absen Masuk : ' + result)
            
            
        else:
            st.info(self.data_lng['info_upload'])
