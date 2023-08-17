import streamlit as st
import pickle
import pandas as pd
from PIL import Image

similarity = pickle.load(open('similarity.pkl', 'rb'))


def redirect_button(url: str, text: str = None, color="#FD504D"):
    st.markdown(
        f"""
    <a href="{url}" target="_blanks ">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 8px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
        unsafe_allow_html=True
    )


def fetch_poster(product_id):
    link = products.loc[products['product_id']
                        == product_id, 'img_link'].values[0]
    return link


def fetch_product_link(product_id):
    link = products.loc[products['product_id']
                        == product_id, 'product_link'].values[0]
    return link


def recommend(product):
    product_index = products[products['product_name'] == product].index[0]
    distances = similarity[product_index]
    products_list = sorted(list(enumerate(distances)),
                           reverse=True, key=lambda x: x[1])[1:6]

    recommended_product_poster = []
    recommended_list = []
    recommended_product_links = []

    for i in products_list:
        product_id = products.iloc[i[0]].product_id
        recommended_product_poster.append(fetch_poster(product_id))
        recommended_list.append(products.iloc[i[0]].product_name)
        recommended_product_links.append(fetch_product_link(product_id))

    return recommended_list, recommended_product_poster,  recommended_product_links


amazon_dict = pickle.load(open('amazon_dict.pkl', 'rb'))
products = pd.read_csv('amazon.csv')

st.title("Product Recommender System")

selected_product_name = st.selectbox(
    "Select a product",
    products['product_name'].values)

if st.button("Recommend"):
    names, posters, links = recommend(selected_product_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        url = links[0]
        st.text(names[0])
        st.image(posters[0], use_column_width=True)
        redirect_button(url, "Go to Product")

    with col2:
        url = links[1]
        st.text(names[1])
        st.image(posters[1], use_column_width=True)
        redirect_button(url, "Go to Product")

    with col3:
        url = links[2]
        st.text(names[2])
        st.image(posters[2], use_column_width=True)
        redirect_button(url, "Go to Product")

    with col4:
        url = links[3]
        st.text(names[3])
        st.image(posters[3], use_column_width=True)
        redirect_button(url, "Go to Product")

    with col5:
        url = links[4]
        st.text(names[4])
        st.image(posters[4], use_column_width=True)
        redirect_button(url, "Go to Product")
