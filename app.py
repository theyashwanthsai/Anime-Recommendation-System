# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import numpy as np # linear algebra
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import streamlit as st



# data = pd.read_csv("cleaned_data.csv")


# cv = CountVectorizer(max_features = 13500,stop_words="english")
# vectors = cv.fit_transform(data["Tags"])

# similarity = cosine_similarity(vectors)

# def Rec(user_input):
#     Index_of_anime = data[data["Name"] == user_input].index[0]
#     Similarity_score = similarity[Index_of_anime]
#     Sorted_scores = sorted(list(enumerate(Similarity_score)),reverse = True,key= lambda x: x[1]) [1:11]
#     Recommended_Anime = []
    
#     for i in Sorted_scores:
#         Recommended_Anime.append(data.iloc[i[0]].Name)
#     return Recommended_Anime

# st.title('Anime Recommender')
# anime_id = st.selectbox('Select an anime:', data['Name'].values)
# similar_anime = Rec(anime_id)
# if st.button('Recommend'):
#     st.table(similar_anime)


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load the dataset
anime_data = pd.read_csv("cleaned_data.csv")

# Preprocess the data
cv = CountVectorizer(stop_words='english')
anime_vectors = cv.fit_transform(anime_data['Tags'].fillna(''))

# Build the recommendation model
anime_similarity = cosine_similarity(anime_vectors)

# Create a Streamlit app
st.title('Anime Recommendation System')

selected_anime = st.selectbox('Select an anime:', anime_data['Name'].values)

if st.button('Get Recommendations'):
    anime_index = anime_data[anime_data['Name'] == selected_anime].index[0]
    anime_scores = list(enumerate(anime_similarity[anime_index]))
    anime_scores = sorted(anime_scores, key=lambda x: x[1], reverse=True)[1:11]
    recommended_anime = [anime_data.iloc[score[0]]['Name'] for score in anime_scores]
    st.table(recommended_anime)
