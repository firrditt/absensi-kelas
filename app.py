import streamlit as st
from json import load
from pages import Pages
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    st.set_page_config(page_title="Absensi Kelas 4IA10", page_icon="👨" ,layout="wide")
    hide_menu_style = """
    <style>
        #MainMenu {display: none; }
        footer {visibility: hidden;}
        .css-fk4es0 {display: none;}
        #stStatusWidget {display: none;}
        .css-r698ls {display: none;}

        [data-testid="stAppViewContainer"] {
            background: linear-gradient(to right, #ACFADF , #FD8D14);
        }

        [data-testid="stSidebar"] {
            background-color: #C8AE7D
        }

        [data-testid="stHeader"] {
            background-color: transparent
        }
    </style>
    """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    page = Pages()

    absensi = ['Masuk', 'Pulang']
    st.session_state.absensi = st.selectbox(
        "Select absensi", absensi
    )
    page.predict()

if __name__ == "__main__":
    main()