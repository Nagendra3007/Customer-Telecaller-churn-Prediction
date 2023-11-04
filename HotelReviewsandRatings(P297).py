# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:39:04 2023

@author: Janhavi
"""

import pickle
import streamlit as st

st.title('Hotel Reviews and Ratings!(P297)')

load = open('model.pkl','rb')
model = pickle.load(load)

def predict(Review, Rating, Sentiment):
    prediction = model.predict([[Review, Rating, Sentiment]])
    return prediction

def main():
    st.markdown('This is the webapp for prediction of Hotel Reviews And Ratings! :chart: ')
    review = st.text_area(
        'Review'
        )
    st.write('Please write your text!', review)
    rating = st.slider(
        'Rating', 
        options = [1,2,3,4,5]
        ) 
    st.write('The rating is', rating)
    sentiment = st.select_slider(
        'Sentiment',
        options = ['Positive', 'Neutral', 'Negative'],
        )  
    st.write('The Sentiment is', sentiment)
         
if st.button('predict'):
    result = predict(Review, Rating, Sentiment)
    st.success(
        'This Review is: ',
        st.success['Good'.format(result): ]
        )
if _name_ == '_main_' :
    main()

