import numpy as np
import pandas as pd
import streamlit as st

st.title("Hi! Welcome to MoviePicker!")



data = pd.read_csv('ratings.csv')
data.head(10)

movie_titles_genre = pd.read_csv("movies.csv")

data = data.merge(movie_titles_genre,on='movieId', how='left')

Average_ratings = pd.DataFrame(data.groupby('title')['rating'].mean())

Average_ratings['Total Ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

movie_user = data.pivot_table(index='userId',columns='title',values= 'rating')

correlations = movie_user.corrwith(movie_user['Toy Story (1995)'])

recommendation = pd.DataFrame(correlations,columns=['Correlation'])
recommendation.dropna(inplace=True)
recommendation = recommendation.join(Average_ratings['Total Ratings'])
recommendation.head()

recc = recommendation[recommendation['Total Ratings']>100].sort_values('Correlation',ascending=False).reset_index()
recc = recc.merge(movie_titles_genre,on='title', how='left')


text_input = st.text_input("Enter a movie name","Toy Story (1995)")

st.markdown(f"Tavsieler : {recc.head(10)}");