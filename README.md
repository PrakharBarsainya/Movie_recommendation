# 🎬 Movie Recommendation System
An interactive movie recommendation system built with Streamlit, using machine learning techniques to suggest similar movies and the Watchmode API to display movie posters dynamically.

# 📌 Project Overview
This application recommends 10 movies similar to a user-selected movie from the dataset. The UI is powered by Streamlit, and movie posters are fetched in real time using the Watchmode API.

## ⚙️ Features
- ✅ Movie Recommendation based on content similarity

- 🖼️ Dynamic Poster Fetching using Watchmode API

- 📊 Interactive Web UI using Streamlit

- 🔍 complete Movie Search

- 🧠 Easy to deploy and extend

# 🧠 How It Works
- User selects a movie from a dropdown list.

- A recommendation function (get_recommendations) retrieves 10 similar movies.

- The fetch_poster() function queries the Watchmode API for posters of the recommended movies.

- Posters and titles are displayed in a clean 2x5 grid.

# 📦 Dependencies
Make sure you have the following Python packages:

- pandas

- requests

- streamlit



# Install all requirements:
- pip install -r requirements.txt
# 🚀 How to Run
Clone the repository:

git clone https://github.com/PrakharBarsainya/Movie_recommendation.git
cd movie-recommendation-system
Run the app:

streamlit run app.py
Open the URL in your browser:
http://localhost:8501

# 🖼️ Poster API Integration
Poster images are retrieved via the Watchmode Autocomplete Search API.

# 📫 Contact
Developed by [https://github.com/PrakharBarsainya]

# 📊 Dataset
The movie metadata used in this project is sourced from the TMDB 5000 Movie Dataset available on Kaggle.

# 🔗 Download Link:
📥 Download the dataset from Kaggle
[👉 TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

# 📁 Files Included:
- movies.csv – Contains movie titles, genres, overview, cast, crew, and other metadata

- credits.csv – Contains detailed cast and crew information

