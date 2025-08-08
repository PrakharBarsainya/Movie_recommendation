import streamlit as st
import pandas as pd
import requests
import pickle  # ✅ fix typo from `pick` to `pickle`
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()

# Load the processed data and similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

# Function to fetch movie poster
def fetch_poster(movie_title):  # Accepts movie title (string)
    api_key = 'u0DmoKUYLC6P9Y8COL5fGe8D2EQCL6IplC1S9CWB'
    encoded_title = quote_plus(str(movie_title))

    url = f'https://api.watchmode.com/v1/autocomplete-search/?apiKey={api_key}&search_value={encoded_title}&search_type=1'
    response = requests.get(url)

    if response.status_code != 200:
        return "https://via.placeholder.com/300x450?text=API+Error"

    data = response.json()
    results = data.get('results', [])

    if results and 'image_url' in results[0]:
        return results[0]['image_url']
    else:
        return "https://via.placeholder.com/300x450?text=No+Poster+Found"

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🎬 Movie Recommendation System")

# Movie selector
selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)
    st.subheader("🎥 Top 10 Recommended Movies:")

    # Display posters in a 2x5 grid
    for i in range(0, 10, 5):
        cols = st.columns(5)
        for col, j in zip(cols, range(i, i+5)):
            if j < len(recommendations):
                movie_title = recommendations.iloc[j]['title']
                poster_url = fetch_poster(movie_title)  # ✅ fixed: pass title here
                with col:
                    st.image(poster_url, width=130)
                    st.caption(movie_title)

