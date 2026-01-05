from portfolio.models import ExperienceItem, HeaderDetails, SectionList, MdReferences, Reference

RefList = MdReferences(references=[
    Reference(
        ref="neo4j_video",
        text="Neo4j Graph Summit Stockholm 2023",
        link="https://neo4j.com/videos/volvo-cars-retrieving-safety-insights-using-graphs/"
    ),
    Reference(
        ref="plp",
        text="Conference Publication",
        title="Common Spatial Pattern EEG decomposition for Phantom Limb Pain detection",
        link="https://ieeexplore.ieee.org/document/9630561",
        citation="""
        Lendaro, E., Balouji, E., Baca, K., Muhammad A. and Ortiz-Catalan, M. (2021).
        Common Spatial Pattern EEG decomposition for Phantom Limb Pain detection, 
        2021 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), Mexico, 2021, pp. 726-729.
"""
    ), 
    Reference(
        ref="genie",
        text="Gender Initiative for Excellence (Genie)",
        link="https://www.chalmers.se/en/about-chalmers/organisation-and-governance/equality-at-chalmers/genie-gender-initiative-for-excellence/",
    ), 
    Reference(
        ref="genie_pub",
        text="Acknowledgment (Genie Initiative)",
        link="http://dx.doi.org/10.1017/qrd.2021.3",
        citation = """
        Saline, M., Sheeran, M., Wittung Stafshede, P. (2021). 
        A large ‘discovery’ experiment: Gender Initiative for Excellence (Genie) at Chalmers University of Technology. QRB Discovery, 2. <br>
        http://dx.doi.org/10.1017/qrd.2021.3
        """
        ),     
    Reference(
        ref="aiaware",
        text="AI Aware Scale Up",
        link="https://www.drivesweden.net/en/project/ai-aware-scale"
    ), 
    Reference(
        ref="masterThesis",
        text="Master's Thesis",
        link="https://odr.chalmers.se/server/api/core/bitstreams/f9286796-aa99-4b14-9858-3f4bbe308c46/content",
        citation="""
        Baca, K., Söderkvist, W. (2019).
        Discovering Patterns in Driving Data.
        Master's Thesis, Chalmers University of Technology. Chalmers ODR. <br>
        https://odr.chalmers.se/server/api/core/bitstreams/f9286796-aa99-4b14-9858-3f4bbe308c46/content
         """
    )
])

WorkDetails: list[ExperienceItem] = [

    ExperienceItem(
        title="Data Analyst",
        company="Volvo Cars",
        location="Göteborg, Sweden",
        yearStart=2023,
        yearEnd=None,
        description=(
            """
            Management and support for remote vehicle data collection instructions in vehicle fleet. Some of the tasks include:
            - Understanding the data collection needs from different teams and translating them into data collection instructions.
            - Monitoring and troubleshooting end-to-end the data collection process using complex queries and visualization tools.
            - Building tools to validate instructions content and deployment. 
            """
        )
    ),
    ExperienceItem(
        title="Global Graduate - Data Science Track",
        company="Volvo Cars",
        location="Gothenburg, Sweden",
        yearStart=2021,
        yearEnd=2023,
        description=(
            f"""
            24-months career boosting program designed to develop our potential as future leaders. During this time I got the opportunity to work with the next assignments:

             - **APAC Data and Analytics** <br>
            Investigating false positive Diagnostic Trouble Codes using Machine Learning techniques.

             - **CX Consumer Insights and Analytics** <br>
            Analyzed the relationship between overall customer satisfaction (CSAT) and retailer car delivery throughput in the UK, and developed a new Medallia-based survey program to measure consumer-facing employee satisfaction.

             - **Open Innovation Arena** <br>
            Participated in the {RefList.aiaware.md} project by collaborating on the design a graph data model for the analysis of Swedish traffic accidents in Neo4j.
            Data sources included information such as weather, friction, road infrastructure and historical accidents. Results were presented in the Volvo Cars Graph Day 2023 and {RefList.neo4j_video.md}.

             - **Advanced Analytics and AI** <br>
            Exploration and implementation of an evaluation metric for car sales forecast. <br>
            Predictions were evaluated using a hierarchical approach based on different car variant levels such as model, trim and model year.
            """

        )
    ),
    ExperienceItem(
        title="Data Science Research Engineer",
        company="Chalmers University of Technology",
        location="Göteborg, Sweden",
        yearStart=2019,
        yearEnd=2021,
        description=(
            f"""
            Group founded by Chalmers AI Research Center (CHAIR) for supporting data-related academic projects. Some of the projects I took part of were:

            - Survival Analysis to investigate causally related factors (e.g. gender and age) of academia turnover. 
            This project was founded by the {RefList.genie.md}.

            - Analysis and classification of electrical brain activity to study Phantom Limb Pain using time series and image based feature extraction methods (see {RefList.plp.md}).

            - Analysis of COVID-19 patients data for forecasting hospital admissions. This project was in collaboration with Sahlgrenska University Hospital.
            """
        )
    )
]

EducationDetails: list[ExperienceItem] = [
    ExperienceItem(
        title="MSc in Engineering Mathematics and Computational Science",
        company="Chalmers University of Technology",
        location="Göteborg, Sweden",
        yearStart=2017,
        yearEnd=2019,
        description=""
    ), 

    ExperienceItem(
        title="BSc in Engineering Physics",
        company="Monterrey Institute of Technology and Higher Education (ITESM)",
        location="Monterrey, Mexico",
        yearStart=2012,
        yearEnd=2017,
        description=""
    )
]

HeaderDetails = HeaderDetails(
    name="Karen Baca",
    title= "Data Scientist | Data Enthusiast",
    description="With experience in the automotive industry and academia, I have been involved in multiple data-related projects, gaining valuable experience on creating and communicating insights.",
    social_media={
        "LinkedIn": "https://linkedin.com/in/karenbaca",
        "GitHub": "https://github.com/KBACAM",
        f"📫 karen@bacawik.com": f"mailto:karen@bacawik.com"
    }
)

QualificationDetails = SectionList(
    header="Qualifications",
    items=[
        "✔️ 2 Years supporting data-related academic projects as Research Engineer",
        "✔️ 4 Years experience extracting actionable insights from data in the automotive industry",
        "✔️ Strong hands on experience and knowledge in Python and SQL",
        "✔️ Good understanding of statistical principles and their respective applications",
        "✔️ Excellent team-player and displaying strong sense of initiative on tasks"
    ]
)

SkillsDetails = SectionList(
    header="Hard Skills",
    items=[
        "👩‍💻 Programming: Python (Scikit-learn, Pandas, PySpark), SQL, Go",
        "📊 Data Visualization: Plotly, Matplotlib, Seaborn, Power BI",
        "📚 Modeling: Regression, Survival Analysis, Clustering"
    ]
)




