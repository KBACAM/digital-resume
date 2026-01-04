from pathlib import Path
from cv_builder.content import WorkDetails, EducationDetails, HeaderDetails, QualificationDetails, SkillsDetails
from cv_builder.sections import add_experience_section, add_list_section, add_social_links, add_rating_stars
import streamlit as st
from PIL import Image
import os

# -- path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = os.path.join(current_dir, "styles", "main.css")
resume_file = os.path.join(current_dir, "assets", "csv.pdf")
resume_photo = os.path.join(current_dir, "assets", "csv-photo.jpg")

# --- GENERAL SETTINGS ---
st.set_page_config(page_title="Professional CV", 
                   page_icon=":wave:",
                   layout="centered", 
                   initial_sidebar_state="expanded") 

# --- LOAD CSS, PDF & PROFIL PIC ---
# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(resume_photo)

st.sidebar.title("Navigation") # Add a title to the sidebar
st.sidebar.write("Use the sidebar for controls.")

# --- HERO SECTION ---
col_left, col_right = st.columns([1, 2], gap=None)
with col_left:
    st.image(profile_pic, width=200)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name="CV.pdf",
        mime="application/octet-stream",
    )
with col_right:
    st.title(HeaderDetails.name)
    st.markdown(HeaderDetails.title_html, unsafe_allow_html=True)
    st.markdown(HeaderDetails.description_html, unsafe_allow_html=True)


# --- SOCIAL LINKS ---
st.write('\n')
add_social_links(st, HeaderDetails.social_media)

st.divider()

# --- QUALIFICATIONS ---
st.write('\n')
add_list_section(st, QualificationDetails)

st.divider()

# --- SKILLS ---
st.write('\n')
add_list_section(st, SkillsDetails)

st.divider()

# --- WORK EXPERIENCE ---
st.write('\n')
add_experience_section(st, "Work Experience", WorkDetails)

st.divider()

# --- EDUCATION ---
st.write('\n')
add_experience_section(st, "Education", EducationDetails)



st.write("Made with ❤️ by Karen Baca")