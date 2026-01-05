from typing import List, Dict
from portfolio.models import ExperienceItem, SectionList

def add_list_section(
        st: any,
        section: SectionList
    ) -> str:
    """
    Adds a list section to a Streamlit app.
    Parameters:
    - st: Streamlit module
    - section: SectionList dataclass
    """
    st.header(section.header)
    for item in section.items:
        st.write(f"- {item}")
    st.write('\n')

def add_experience_section(
        st: any,
        header: str,
        experiences: List[ExperienceItem]
    ) -> str:
    """
    Adds experience sections to a Streamlit app.
    Parameters:
    - st: Streamlit module
    - experiences: List of ExperienceItem
    """
    st.header(header)
    for exp in experiences:

        text_left, text_right = st.columns([4,1])
        with text_left:
            st.markdown(
                exp.title_html,
                unsafe_allow_html=True)
            st.markdown(
                exp.company_location_html,
                unsafe_allow_html=True)
        with text_right:
            st.markdown(
                exp.year_html,
                unsafe_allow_html=True
            )
        st.markdown(
            exp.description, 
            unsafe_allow_html=True)
        
        st.markdown('\n')

def add_social_links(
        st: any,
        social_media: Dict[str, str]
    ) -> str:
    """
    Adds social media links to a Streamlit app.
    Parameters:
    - st: Streamlit module
    - social_media: Dictionary of social media platform names and URLs
    """
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")
