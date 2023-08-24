import streamlit as st
from utils import Utils
from components import Components
from PIL import Image
import pandas as pd
from json import load
import datetime
import pytz



class Pages():
      
    def predict(self):
        data = load(open('datasets/dataset.json', encoding='utf-8'))
        st.title('Absensi')
        utils = Utils(class_names=data)
        
        imgSt = st.camera_input('Absen')
        img = utils.loadImageFile(imgSt) if imgSt is not None else None
        

        if imgSt and img:
            today = datetime.datetime.utcnow()
            indonesia_timezone = pytz.timezone('Asia/Bangkok')
            current_utc_datetime = pytz.utc.localize(today)
            dateNow = current_utc_datetime.astimezone(indonesia_timezone).strftime('%Y-%m-%d')
            timeNow = current_utc_datetime.astimezone(indonesia_timezone).strftime('%H:%M:%S')

            with st.spinner('Please wait'):
                prediction, probabilities = utils.getPrediction(img)
                if probabilities < 0.85:
                    st.title('Wajah tidak dikenali')
                else:
                    df = utils.getData()
                    ket = ''
                    if 'Masuk' in st.session_state.absensi:
                        ket = 'masuk'
                        checkDF = df[(df['nama'] == prediction['nama']) & (df['keterangan'] == 'MASUK') & (df['tanggal'] == dateNow)]
                    else:
                        ket = 'pulang'
                        checkDF = df[(df['nama'] == prediction['nama']) & (df['keterangan'] == 'PULANG') & (df['tanggal'] == dateNow)]

                    if not checkDF.empty:
                        df = df[df['nama'] == prediction['nama']]
                        st.title(f'Anda telah melakukan absensi {ket}')
                    else:
                        if 'Masuk' in st.session_state.absensi:
                            data = {
                                **prediction,
                                'waktu': timeNow,
                                'tanggal': dateNow,
                                'keterangan': 'MASUK'
                            }
                        else:
                            data = {
                                **prediction,
                                'waktu': timeNow,
                                'tanggal': dateNow,
                                'keterangan': 'PULANG'
                            }
                        df = utils.postAbsen(data)
                        
                        df = df[(df['nama'] == prediction['nama']) & (df['tanggal'] == dateNow)]
                    st.table(df)
            
        else:
            st.info('Mohon Mengambil Gambar')
