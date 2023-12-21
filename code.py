import nltk
import streamlit as st
from textblob import TextBlob
from streamlit_option_menu import *
from streamlit_extras.keyboard_url import keyboard_to_url
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
import json as js
import time
import googletrans
from googletrans import Translator
from googletrans import LANGUAGES
import gtts
from gtts import gTTS
import os
import requests
import pandas as pd
#__________________________________________________________


class language_ai :

    def process(self):
        st.set_page_config(page_title='Q&A Project By Praveen', layout="wide")
        col1, col2, col3 = st.columns([2, 7, 1])

        col2.markdown(
            "<h1 style='font-size: 80px;'><span style='color: cyan;'></span> <span style='color: cyan;'>Questioning </span><span style='color: white;'>Answering </span><span style='color: cyan;'> System</span> </h1>",
            unsafe_allow_html=True)
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        API_URL = ""
        headers = {"Authorization": ""}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.markdown(
                "<h1 style='font-size: 40px;'><span style='color: cyan;'>Provide </span> <span style='color: white;'>Context </span> </h1>",
                unsafe_allow_html=True)
            context = st.text_area("")
            st.markdown(
                "<h1 style='font-size: 40px;'><span style='color: cyan;'>Provide </span> <span style='color: white;'>Question</span> </h1>",
                unsafe_allow_html=True)
            try:
                question = st.text_input("")
                if st.button("Proceed"):
                    output = query({
                        "inputs": {
                            "question": question,
                            "context": context
                        },
                    })
                    st.markdown(
                        "<h1 style='font-size: 40px;'><span style='color: cyan;'>Result </span> <span style='color: white;'>:)</span> </h1>",
                        unsafe_allow_html=True)
                    st.code(f'Question : {question} , Answer : {output["answer"]}')

            except:
                st.success("Provide Correct Question !!!")






#___________________________________________________________________________________________________________________________________________





# Object Creation

object = language_ai()
object.process()
