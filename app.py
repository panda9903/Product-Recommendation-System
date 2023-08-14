import streamlit as st
import pickle
import pandas as pd
import requests 

similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(product_id):
    return products[img_link]

amazon_dict = pickle.load(open('amazon_dict.pkl', 'rb'))
products = pd.DataFrame(amazon_dict)