import pandas as pd
import streamlit as st
import pickle
import requests

# Define your API key here
#api_key = '8265bd1679663a7ea12ac168da84d2e8'  # Replace with your actual API key


# Fetch the movie poster
# def fetch_poster(movie_id):
#url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
 #   try:
 #      response = requests.get(url, timeout=10)  # Set a timeout for the request
 #       response.raise_for_status()  # Raise an error for bad responses
 #       data = response.json()
 #       if 'poster_path' in data and data['poster_path']:
 #           return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
 #       else:
 #           return None  # Return None if no poster is found
 #   except requests.exceptions.Timeout:
 #       st.error("The request timed out. Please try again.")
 #       return None
 #   except requests.exceptions.RequestException as e:
 #       st.error(f"An error occurred: {e}")
 #       return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
       # poster = fetch_poster()
       # recommended_movies_posters.append(poster)

    return recommended_movies


# Load movie data and similarity data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    names = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])

    with col2:
        st.text(names[1])

    with col3:
        st.text(names[2])

    with col4:
        st.text(names[3])

    with col5:
        st.text(names[4])

