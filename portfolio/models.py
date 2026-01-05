from dataclasses import dataclass, field
from typing import Union, List, Dict, Optional

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


@dataclass
class Reference:
    ref: str  # Short name for the reference
    text: str  # Text for the link
    link: str  # URL for the link
    title: Optional[str] = None  # Optional title for the reference
    citation: Optional[str] = None  # Optional citation information

    @property
    def md(self):
        """Return the markdown formatted string [text](link)."""
        return f"[{self.text}]({self.link})"  # Custom markdown format

@dataclass
class MdReferences:
    references: List[Reference] = field(default_factory=list)

    def __post_init__(self):
        """Automatically create dynamic attributes for each reference using 'ref'."""
        for reference in self.references:
            # Dynamically create an attribute for each reference based on `ref`
            setattr(self, reference.ref, reference)