import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

image = Image.open('./images/beertaps.png')
st.image(image)

st.write('# Cheers!')
st.write('## Get Your Beer Recommendations Here!')

model_df = pd.read_csv('./app_data/model_df.csv')
meta_data_df = pd.read_csv('./app_data/df_meta_data.csv')


#recommender function 
def beer_recommender(beer, n_recs): 

    y = np.array(model_df.loc[beer]).reshape(1,-1)
    cos_sim = cosine_similarity(model_df, y)
    cos_sim = pd.DataFrame(data=cos_sim, index = model_df.index)
    cos_sim.sort_values(by = 0, ascending = False, inplace=True)
    
    results = cos_sim.index.values[1:n_recs+1]
    results_df = meta_data_df.loc[results]
    results_df.drop(columns = ['beer_id'], inplace=True)
    results_df.reset_index(inplace=True)
    return results_df

beer_input = st.selectbox("Step 1: Just start typing the name of a beer that you like below.", options=meta_data_df.Name)
beer = meta_data_df.index[meta_data_df['Name'] == beer_input]
n_recs = st.selectbox("Step 2. Select how many recommendations you want.", options=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
beer_button = st.button("Cheers!")
# beer1 = "Sculpin"
# n_recs1 = 5 
if beer_button: 
    results = beer_recommender(beer, n_recs)
    st.table(results)