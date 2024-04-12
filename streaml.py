import streamlit as st
from streamlit_option_menu import option_menu as op

row1 = st.container()
row2 = st.container()

with st.sidebar:
    selected = op(
        menu_title="Meny",
        options=["Hem", "Om oss", "Kontakt"],
        icons=["house-heart-fill", "calendar2-heart-fill", "envelope-heart-fill"],
        menu_icon="house-heart-fill",
        default_index=0,
    )

col1, col2, col3, col4 = st.columns([4, 4, 4, 4])

if selected == "Hem":
    st.title("Welcome to the home page")
    st.header("Detta är bara början")

    with row1:
        with col1:
            st.image("blom.jpg")
            if st.button("Blommor"):
               st.write("Samuel umtiti")

    
    with col2:
        st.image("ettan.jpg")
        st.write("hhgggg")

if selected == "Om oss":
    st.title("Detta är vi")

if selected == "Kontakta oss":
    st.title("Kontakta oss")


