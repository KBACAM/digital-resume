from dataclasses import dataclass, field
from typing import Union, List, Dict

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
    yearStart: int = 2000
    yearEnd: Union[int, None] = None
    description: str = "Job Description"


@dataclass
class HeaderDetails:
    """
    Data class for header details.
    Parameters:
    - name: Full name
    - description: Short description or title
    - email: Contact email
    """
    page_title: str = "Digital CV"
    name: str = "Your Name"
    description: str = "Your Description"
    email: str = "name@example.com"
    social_media: Dict[str, str] = field(default_factory=lambda: {
        "LinkedIn": "https://linkedin.com/",
        "GitHub": "https://github.com/"
    })
    
@dataclass
class SectionList: 
    header: str = "Header"
    items: List[str] = field(default_factory=lambda: ["Item 1", "Item 2", "Item 3"])


def _format_year_range(
        yearStart: int,
        yearEnd: Union[int, None]
    ) -> str:

    assert len(str(yearStart)) == 4, "yearStart must be a 4-digit year"
    if yearEnd is not None:
        assert len(str(yearEnd)) == 4, "yearEnd must be a 4-digit year or None"
        assert yearEnd >= yearStart, "yearEnd must be greater than or equal to yearStart"
    else:
        yearEnd = "Present"
    return f"{yearStart} - {yearEnd}"


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
        experiences: List[ExperienceItem]
    ) -> str:
    """
    Adds experience sections to a Streamlit app.
    Parameters:
    - st: Streamlit module
    - experiences: List of ExperienceItem
    """
    st.header("Work Experience")
    for exp in experiences:
        st.subheader(f"{exp.title} | {exp.company}")
        st.markdown(f"**{_format_year_range(exp.yearStart, exp.yearEnd)}**")
        st.markdown(exp.description)
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