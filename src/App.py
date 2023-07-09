import streamlit as st
from streamlit_option_menu import option_menu
from DPCM import *
from ADPCM import *
from AudioFileProcess import *
import io

with st.sidebar:
    selected = option_menu(
                menu_title="Main Menu",     
                options=["DPCM", "ADPCM"],
                menu_icon="cast", 
                default_index=0,  
                orientation="vertical",
            )

if selected == "DPCM":
    st.title(":orange[DPCM]")
    uploaded_file = st.file_uploader("Upload an image (.wav)", type=["wav"])
    
    if uploaded_file is not None:
        st.audio(uploaded_file)
        encodeButton = st.button("Encode")
        if encodeButton:
            samples = getSamplesFromAudio(uploaded_file)
            DPCMencode = DPCMencoder(samples)
            st.text_area("Mã nhị phân", value=DPCMencode, height=300)
            st.text(f"Số lượng bit: {len(DPCMencode)}")
            DPCMdecode = DPCMdecoder(DPCMencode)
            decodeFile = io.BytesIO()
            st.text("File giải nén")
            convertSamplesToAudio(DPCMdecode, decodeFile)
            st.audio(decodeFile)
        

if selected == "ADPCM":
    st.title(":green[ADPCM]")
    uploaded_file = st.file_uploader("Upload an image (.wav)", type=["wav"])
    if uploaded_file is not None:
        st.audio(uploaded_file)
        encodeButton = st.button("Encode")
        if encodeButton:
            samples = getSamplesFromAudio(uploaded_file)
            ADPCMencode = ADPCMencoder(samples)
            st.text_area("Mã nhị phân", value=ADPCMencode, height=300)
            st.text(f"Số lượng bit: {len(ADPCMencode)}")
            ADPCMdecode = ADPCMdecoder(ADPCMencode)
            decodeFile = io.BytesIO()
            st.text("File giải nén")
            convertSamplesToAudio(ADPCMdecode, decodeFile)
            st.audio(decodeFile)