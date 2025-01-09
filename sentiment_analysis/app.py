import streamlit as st
from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

st.title("Análisis de Sentimientos")

user_input = st.text_area("Introduce un texto para analizar:")

if st.button("Analizar"):
    if user_input.strip():
        result = sentiment_analysis(user_input)
        sentiment = result[0]['label']
        score = result[0]['score']
        
        st.write(f"Sentimiento: {sentiment}")
        st.write(f"Confianza: {score*100:.2f}%")
    else:
        st.write("Por favor, ingresa un texto para analizar.")
