import streamlit as st
import pickle
import pandas as pd


def recommend(movie):

    if movie not in movies['title'].values:
        st.error("Movie not found in the database. Please select another movie.")
        return []


    movie_index = movies[movies['title'] == movie].index[0]


    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movies = [movies.iloc[i[0]].title for i in movies_list[1:6]]

    return recommended_movies


movies = pd.read_pickle('movies.pkl')
similarity = pd.read_pickle('similarity.pkl')

st.title('Movie Recommender System')


selected_movie_name = st.selectbox(
    'What would you like to watch today?',
    movies['title'].values
)


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i, recommendation in enumerate(recommendations, start=1):
        st.write(f"{i}. {recommendation}")
