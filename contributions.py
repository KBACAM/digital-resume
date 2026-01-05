import streamlit as st
from content import RefList


st.set_page_config(page_title="Contributions", 
                   page_icon="🏆",
                   layout="centered", 
                   initial_sidebar_state="expanded") 


st.header("Conferences and Publications")

st.subheader(RefList.neo4j_video.md)
st.video(data = "https://www.youtube.com/watch?v=RH3-Lv9p9MU",
         start_time = "9m33s",
         loop=False,
         autoplay=True)

st.subheader(RefList.plp.md)
st.markdown(RefList.plp.citation, unsafe_allow_html=True)


st.subheader(RefList.genie_pub.md)
st.markdown(RefList.genie_pub.citation, unsafe_allow_html=True)


st.subheader(RefList.masterThesis.md)
st.markdown(RefList.masterThesis.citation, unsafe_allow_html=True)