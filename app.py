# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wvLliMQQrlpbMhvdEilORQcpS4yYoc3T
"""

import streamlit as st
from PIL import Image
import os
import json
import numpy as np
import pandas as pd
from fastai.vision.all import load_learner
from fastai.vision.all import PILImage
from fastai.vision.all import Resize
from fastai.vision.all import *
from fastai.vision.data import ImageDataLoaders
import pathlib
import urllib

st.set_page_config(page_title="RealORFake",page_icon="🤖",layout="wide",initial_sidebar_state="expanded")

plt = platform.system()
if plt == 'Windows': pathlib.PosixPath = pathlib.WindowsPath
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

model = load_learner('fakeorreal.pkl',cpu=True)

st.title("**💥Welcome to the image prediction app!💥**")
st.subheader('A machine learning model for predicting whether the image is a "real human" image or was generated by "AI"')
st.markdown("After the birth of AI that can generate an image, there is a confusion between real and AI-generated image. So, this model is made to make sure if the image is as we think it is or not.")
st.markdown('⚠️Please notice that this model was made from specific image generators. Some fake image result may be wrong.⚠️')

st.markdown("-----------------")
st.markdown("**Crop your image into the human face only🧒 -- No body🧍‍♂️**")
file = st.file_uploader("📥Upload your image:")
st.markdown("-----------------")

sample_path = ("./Sample Image)
file_name = os.listdir(sample_path)
sample_image = st.sidebar.selectbox(
    'Sample :',
    (file_name))

if file is None:
    img = PILImage.create(os.path.join(sample_path, sample_image))
    st.markdown('\n')
    st.title("Example :")
    st.image(img)
    st.subheader("✒️Result :")

else:
    img = PILImage.create(file)
    st.title("📌📂Here is the image you've selected:")
    st.image(img)
    st.subheader("✒️Result :")

st.sidebar.image('image dumb/JUSTAiB.jpg')
st.sidebar.title("**More Details**")
st.sidebar.markdown("**Github :**")
st.sidebar.markdown("https://github.com/melin0236/AiBxDarun-Image-Classification-Real-human-face-or-A.i-generated/tree/main")
st.sidebar.markdown("-----------------")
st.sidebar.markdown("**Blog (written in Thai) :**")
st.sidebar.markdown("((Blog))")
st.sidebar.markdown("-----------------")
st.sidebar.markdown("**Sending Feedback :**")
st.sidebar.markdown("Gmail : bunpan.kaopun@gmail.com")

c_type = ['fake', 'real']
im_predicted = model.predict(img)
c_name = im_predicted[0]
ts_prob = im_predicted[2]
prob = torch.sort(ts_prob, descending=True)
m_prob = prob[0][0]

if c_name in c_type:
     st.spinner(text="⏰In progress...")
     st.success(f"💡This image is **{c_name}**  image with the probability of **{m_prob*100:.02f}**%💡")

else:
     st.error(f"💀Sorry, please upload another image💀")
st.markdown(' ')
st.markdown('________________________________________________')

st.subheader("🙇‍♀️Special Thanks :")
st.markdown("AI builder for this good opportunity")

st.subheader("🪄About me :")
st.markdown("Hello! I'm a grade 10 student in Thailand who is learning about computer science and things about coding.")
st.markdown("If you found a mistake in this model or the app, please feel free to feedback the mistake in sidebar. Or if you have any suggestion, you can also send them in my email. Thank you!")
st.markdown('As for the error in fake image prediction, I will do my best to improve it with more kind of dataset in order to make the model more accurate for most kind of image.')
st.title("Thank you so much!💖")
