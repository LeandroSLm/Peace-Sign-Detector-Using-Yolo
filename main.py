import streamlit as st
from PIL import Image
from yolo_PeaceSignDetector import *

st.title("Detector de sinais de mão")

uploaded_file = st.file_uploader("Envie a imagem para avaliação", type=["jpg", "jpeg", "png"])

if uploaded_file:
    imagem = Image.open(uploaded_file)
    st.image(imagem,caption="Imagem para analise")
    resultado = model(imagem)
    resultado[0].save("output.jpg")
    st.image("output.jpg", caption="Imagem Processada", use_container_width=True)
    
if os.path.exists("output.jpg"):
        os.remove("output.jpg")


    
