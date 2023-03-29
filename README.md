# Anime-Recommendation-System
### Exploring the Kaggle dataset and building a website which recommend similar anime.

This project is a simple implementation of a content-based recommendation system for anime using Python and Streamlit. The following are the main steps involved in building the recommendation system:

1) Load the dataset: The code loads a pre-processed dataset (check notebook file) of anime titles and their corresponding tags.

2) Preprocess the data: The tags for each anime are vectorized using the CountVectorizer method from the scikit-learn library.

3) Build the recommendation model: The cosine similarity between the anime vectors is computed using the cosine_similarity method from the scikit-learn library. This similarity score is then used to recommend similar anime titles.

4) Create a Streamlit app: The code creates a Streamlit app that allows users to select an anime title from a dropdown list and get recommendations for similar anime titles.

The [app](https://theyashwanthsai-anime-recommendation-system-app-0rpzw9.streamlit.app) is deployed on Streamlit Cloud and can be accessed through a web browser.

The [dataset](https://www.kaggle.com/datasets/vishalmane10/anime-dataset-2022)


![Screenshot 2023-03-26 at 8 24 03 PM](https://user-images.githubusercontent.com/68785131/227785191-3d339017-6826-4ae6-8f74-5fbef27ea70b.png)


### ToDo:
Create a backend using flask/django and deploy it since streamlit cloud has some issues with the dataset (?)
