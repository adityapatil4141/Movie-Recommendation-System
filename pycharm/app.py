# libraries
import streamlit as st
import pickle
import pandas as pd
import requests

# Get Poster
def fetch_poster(movie_id):
    response =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4415e8c8b04a09cbe2cadc684f533565'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/original" + data['poster_path']

# recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster =[]
    for a in movie_list:
        movie_id = movies.iloc[a[0]].movie_id
        recommended_movies.append(movies.iloc[a[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

# import movies_dict
movies_dict = pickle.load(open('/Users/macbookpro/PycharmProjects/movie-recommender-system/movies_dict_new.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# import similarity
similarity = pickle.load(open('/Users/macbookpro/PycharmProjects/movie-recommender-system/similarity3.pkl', 'rb'))

# similarity = pickle.load(open('similarity.pkl', 'rb'))

# title
st.title("Movie Recommender System")

# dropdown
selected_movie_name = st.selectbox(
    'Movies list',
    movies['title'].values)

# recommend button

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    import streamlit as st

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
