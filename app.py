import streamlit as st

pg = st.navigation(
    [
        st.Page("cv-digital.py", title= "Digital CV", icon="📄"),
        st.Page("contributions.py", title= "Contributions", icon="🏆"), 
    ]
)

st.set_page_config(
    page_title= "Karen Baca - Digital Portfolio",
    page_icon=":wave:",
)

pg.run()