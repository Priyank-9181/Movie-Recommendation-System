import streamlit as st
from service.model import recommend, new_movies


st.title("Movie Recommendation System")

option = st.selectbox(
    "Select A Movie That You Watch Already",
    new_movies["title"],
)

st.write("You selected:", option)

if st.button("Submit", type="tertiary", use_container_width=True):
    data = recommend(option)

    for idx, i in enumerate(st.columns(5)):
        with i:
            st.text(data[idx]["title"])
            st.image(data[idx]["poster"])
