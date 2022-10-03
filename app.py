import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

image = Image.open('./images/beertaps.png')
st.image(image)

st.write('# Cheers!')
st.write('## Get Your Beer Recommendations Here!')