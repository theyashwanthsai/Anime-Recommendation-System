import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # linear algebra
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st



data = pd.read_csv("cleaned_data.csv")


cv = CountVectorizer(max_features = 13500,stop_words="english")
vectors = cv.fit_transform(data["Tags"])

similarity = cosine_similarity(vectors)

def Rec(user_input):
    Index_of_anime = data[data["Name"] == user_input].index[0]
    Similarity_score = similarity[Index_of_anime]
    Sorted_scores = sorted(list(enumerate(Similarity_score)),reverse = True,key= lambda x: x[1]) [1:6]
    Recommended_Anime = []
    
    for i in Sorted_scores:
        Recommended_Anime.append(data.iloc[i[0]].Name)
    return Recommended_Anime

st.title('Anime Recommender')
anime_id = st.selectbox('Select an anime:', data['Name'].values)
similar_anime = Rec(anime_id)
st.table(similar_anime)