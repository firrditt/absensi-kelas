import streamlit as st
from utils import Utils
from components import Components
from PIL import Image
import pandas as pd
from json import load
import datetime



class Pages():
      
    def predict(self):
        data = load(open('dataset.json'), encoding='utf-8')
        st.title('Absensi')
        utils = Utils(class_names=data)
        
        imgSt = st.camera_input('Absen')
        img = utils.loadImageFile(imgSt) if imgSt is not None else None
        

        if imgSt and img:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            timeNow = datetime.datetime.now().strftime('%H:%M:%S')
            batasTimeMasuk = ''
            with st.spinner('Please wait'):
                prediction, probabilities = utils.getPrediction(img)
                if probabilities < 0.9:
                    st.title('Wajah tidak dikenali')
                else:
                    df = utils.getData()
                    ket = ''
                    if 'Masuk' in st.session_state.absensi:
                        ket = 'masuk'
                        checkDF = df[(df['nama'] == prediction['nama']) & (df['keterangan'] == 'MASUK') & (df['tanggal'] == today)]
                    else:
                        ket = 'pulang'
                        checkDF = df[(df['nama'] == prediction['nama']) & (df['keterangan'] == 'PULANG') & (df['tanggal'] == today)]

                    if not checkDF.empty:
                        df = df[df['nama'] == prediction['nama']]
                        st.title(f'Anda telah melakukan absensi {ket}')
                    else:
                        if 'Masuk' in st.session_state.absensi:
                            data = {
                                **prediction,
                                'waktu': timeNow,
                                'tanggal': today,
                                'keterangan': 'MASUK'
                            }
                        else:
                            data = {
                                **prediction,
                                'waktu': timeNow,
                                'tanggal': today,
                                'keterangan': 'PULANG'
                            }
                        df = utils.postAbsen(data)
                        
                        df = df[(df['nama'] == prediction['nama']) & (df['tanggal'] == today)]
                    st.table(df)
                    # result = prediction['nama'].capitalize() if prediction['nama'] is not None else ''
                    # col1, col2 = st.columns([2, 2])
                    # col1.subheader('Hasil Absen')
                    # col1.image(imgSt, use_column_width=True, clamp=True)

                    # col2.subheader('Absen Masuk : ' + result)
            
            
        else:
            st.info('Mohon Mengambil Gambar')
