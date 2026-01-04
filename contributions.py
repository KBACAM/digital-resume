import streamlit as st

# --- GENERAL SETTINGS ---
st.set_page_config(page_title="Contributions", 
                   page_icon="🏆",
                   layout="centered", 
                   initial_sidebar_state="expanded") 


st.header("🏆 Contributions")

st.subheader("Conferences")

st.video(data = "https://www.youtube.com/watch?v=RH3-Lv9p9MU",
         start_time = "11m15s",
         loop=False,
         autoplay=True)

st.subheader("Publications")