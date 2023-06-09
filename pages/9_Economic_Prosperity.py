import streamlit as st

st.markdown("""

### Economic Prosperity

The fifth chapter called “Supporting Economic Prosperity”, which presents the industrial, commercial and other business 
considerations to be taken in shaping the county’s future land-use decisions does anything but. 

After reviewing the chapter, several unanswered questions remain to be addressed:

* The chapter recommends amending the Adequate Public Facilities Ordinance (APFO), which is a residential development impact 
mitigation tool to address housing need to keep up with jobs-growth. This seems like another attempt to circumvent the mitigation 
requirements of APFO by adding an incompatible provision. How will the county ensure that the intended requirements of APFO 
remain unaffected by this new proposal?

* The chapter estimates that an average of 3,000 new jobs per year were created over the past ten years. It extrapolates 
based on this figure that 59,000 new jobs will be created by 2040. This 59,000 jobs figure is used as a basis to project that 
30,000 new housing units will be needed by 2040. In making this claim, the chapter assumes that ALL of the 3,000 new jobs per year 
resulted in a demand for housing, which is NOT true. By the same token, only a fraction of the 59,000 new jobs by 2040 will lead to housing demand.

* During the public meeting to discuss this chapter, DPZ Director Amy Gowan asserted that residential development pays for itself and
pointed to the Urban Analytics study as a basis for her assertion. The Urban Analytics study is riddled with flaws. Specifically, the 
Urban Analytics model was not benchmarked to demonstrate that it can produce known results. Before predicting the future, why 
was it not shown to predict the present by using development data for the past 20 years?

* Looking at this chapter on economic prosperity, it ignores/neglects to mention the trends along Route 1 over the years where 
previously industrial zoned properties have been rezoned to so-called Mixed-Use zoning, thereby reducing the county’s commercial tax-base.

#### The new zone type proposed for Route 1 is substantially similar to the existing, failed CAC zone type

The chapter mentions so-called Corridor Activity Center (CAC)-zoned regions in Route 1 and states that:
The purpose of the CAC District, as stated in the Zoning Regulations, is to “...provide for the development of pedestrian-oriented, 
urban activity centers with a mix of uses which may include retail, service, office, and residential uses.” The chapter then says, 
This intended purpose has not been realized.

As noted in the 2018 Land Development Regulations Assessment, many stakeholders indicated the 50% retail requirement was difficult to 
meet given retail market conditions along the Corridor. While the goals of this district remain desirable, the locations of these centers 
and incentives to create them must be revisited.

In 2021, the County Executive introduced CB8-2021, which further eliminated the commercial component of this zone type. First the county 
reduced the tax dollars potential of the land by rezoning from industrial to mixed-use (CAC), second, it completely eliminated the commercial 
component of the zone type for a property-owner thereby creating precedent for the remaining CACs.

The report notes that:

Many parcels along the Route 1 Corridor are zoned Corridor Activity Center (CAC). The chapter proposes new zone types for Route 1 
that is substantively unchanged from the current CAC zone type.

* The chapter says one of the key approaches to enhancing Howard County’s economy includes “ensuring a healthy jobs-housing balance.” 
What does “healthy” mean in this context? How is it quantified?

* The chapter acknowledges the future of “automation.” How is the county getting ready for automation? What kind of 
efforts are underway to address the impact on the service industry? How many of the service jobs will be impacted? 
How will overall income be affected? Relatedly over 80% of jobs that will exist in the 2030s have not been invented yet. 
So how does the 59,000 jobs by 2040 reconcile with this level of uncertainty in types of jobs. How does this economic prosperity 
plan account for them? What does “enhancing” access to employment training and education entail?

* The chapter says that some people from the public engagement and planning process have remarked that “it is difficult to 
grow a diverse job base without affordable housing in places served by public transit.” What does “served” mean here? Is the mere 
existence of a bus stop qualify the area as being “served”? There is zero evidence that suggests that people have adequate access 
to public transportation to how is that measured?

* The chapter says that “commercial land uses comprise 3%, or approximately 6.9 square miles, of land in the County.” 
Given that residential development in Howard County has not provided the needed revenue to cover its impacts on infrastructure 
and other public service needs, what does this 6.9 square miles translate into tax dollars? What is the optimal amount to cover 
the shortfall on taxes, to improve and maintain the level-of-service?

* The chapter says that “industrial land, including. manufacturing, warehousing, and utilities represents 3% of 
the County, or approximately 7.12 square miles. How has the decline in industrial zoned land especially along 
Route 1 affected the tax-base?

* The chapter says “the DCP also calls for new 6,244 residential housing units.” How many of these units are “affordable”?

The challenge in predicting the next 20 years given the different sources of uncertainties and unknowns is greatly appreciated. 
This challenge is exacerbated when untrue assumptions about the impact on revenue of residential development or critical components 
of the county’s economy - the schools - are ignored.

""")

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)