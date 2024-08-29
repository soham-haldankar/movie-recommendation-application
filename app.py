import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=784ddc9c4f16790f7ece7afb81511fdb'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/original" + data['poster_path']



def recommend(movie):
    movie_index = movies_all[movies_all['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1: 6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies_all.iloc[i[0]].movie_id

        recommended_movies.append(movies_all.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_all = pickle.load(open('movies.pkl', 'rb'))
movies = movies_all['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System ')

selected_movie_name = st.selectbox('Based on which movie do you want recommendations?',
                      movies)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5  = st.columns(5)

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
