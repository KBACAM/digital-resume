from dataclasses import dataclass, field
from typing import Union, List, Dict, Optional


@dataclass 
class RatingItem:
    """
    Data class for skill rating details.
    Parameters:
    - skill: Name of the skill
    - rating: Rating value (1-5)
    """
    skill: str = "Skill Name"
    rating: int = 3  # Rating from 1 to 5


@dataclass
class ExperienceItem: 
    """
    Data class for work experience details.
    Parameters:
    - title: Job title
    - company: Company name
    - init_year: Start year (4-digit integer)
    - end_year: End year (4-digit integer or None for present)
    - description: Job description
    """
    title: str = "Job Title"
    company : str = "Company Name"
    location: Optional[str] = "Location"
    yearStart: int = 2000
    yearEnd: Union[int, None] = None
    description: str = "Job Description"

    @property
    def title_html(self):
        return f"""<div style='text-align:left; font-weight:bold; font-size:1.2em'>
        {self.title}
        </div>
        """

    @property
    def year_html(self):
        end = self.yearEnd if self.yearEnd else "Present"
        return f"""
        <div style='text-align:right; font-size:1.2em; font-weight:bold'>
        {self.yearStart} - {end}
        </div>
        """

    @property
    def company_location_html(self):
        return f"""
        <div style='text-align:left; font-weight:bold;font-size:1.0em'>
        {self.company} - {self.location}
        </div>
        """

    @property
    def location_html(self):
        return f"""
        <div style='text-align:left; font-size:1.0em'>
        {self.location}
        </div>
        """ if self.location else ""
    

@dataclass
class HeaderDetails:
    """
    Data class for header details.
    Parameters:
    - name: Full name
    - title: Professional title
    - description: Short description of your professional profile
    - email: Contact email
    """
    name: str = "Your Name"
    title: str = "Professional Title"
    description: str = "Short description about your professional profile"
    social_media: Dict[str, str] = field(default_factory=lambda: {
        "LinkedIn": "https://linkedin.com/",
        "GitHub": "https://github.com/"
    })
    
    @property
    def title_html(self):
        return f"""
        <div style='text-align:left; font-weight:bold; font-size:1.2em'>
        {self.title}
        </div>
        """
    @property
    def description_html(self):
        return f"""
        <div style='text-align:left; font-size:1.0em'>
        {self.description}
        </div> 
        """


@dataclass
class SectionList: 
    header: str = "Header"
    items: List[str] = field(default_factory=lambda: ["Item 1", "Item 2", "Item 3"])

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


def add_rating_stars(
        st: any,
        header: str,
        ratings: List[RatingItem]
):
    """
    Adds a rating stars section to a Streamlit app.
    Parameters:
    - st: Streamlit module
    - header: Section header
    - ratings: List of RatingItem
    """
    st.header(header)
    for item in ratings:
        st.feedback(
            options= "stars",
            key = item.skill,
            disabled = True, 
            default = item.rating - 1
        )
