import streamlit as st

st.markdown("""

### Growth and Conservation Framework

Chapter 2 provides multiple sources of projections for housing and job growth in the county, and proposes 
plans for future land use in terms of six major land use categories.In the Future Land Use Map, these categories are 
divided into 19 different use types. The basis for defining the use types and their location is not provided, nor is the 
relationship between them and the county’s existing zoning districts. It is not clear if the proposal is to completely redefine 
zoning districts and regulations to accommodate the seemingly arbitrary plan.

The county is described as being largely built out, with most land either being developed or in preservation. 

The multiple and varied sources for housing and job projections are dispersed throughout the chapter and their relevance 
is difficult to interpret. (See table 1). 

For example, statistics from the Department of Planning and Zoning are provided, consisting of permit applications and 
growth since 2020. For September 2020 to now (assuming a time span of 2.5 years), the numbers average 2,800 homes and 563 jobs per year. 
Since this period overlaps with the COVID pandemic, it is likely not an accurate reflection of future trends.

""")
            
st.markdown("""

Missing from this chapter are past trends in Howard County job and housing, for example, as included in the 
[Maryland Department of Planning Report](https://planning.maryland.gov/Documents/capacity-for-future-nonresidential-growth-howard-county.pdf).

The Maryland report shows an average of 3,100 jobs/year created from 2010-2020. The report also calculates a 2009 jobs/housing ratio of 1.77. 
Using this ratio, the average of 3,100 jobs a year corresponds to 1,750 new homes per year for Howard County. 

The Maryland Planning report’s numbers for new homes and jobs is similar to the chapter’s projections provided by RCLCO Real Estate Advisors 
of 1,550 new homes and 2,950 jobs per year (page 10). 

An apparent error on page 11 of this chapter describes Howard County’s jobs-housing ratio as lower than that of other counties. According to the Maryland report, 
the Howard County jobs/housing ratio is in fact HIGHER than other counties. In 2000 it was 1.77, similar to Montgomery, Baltimore City and Ann Arundle counties, 
while the state average was 1.54.

Absent is mention of projected population growth. How can the county plan on 30 years of growth without an analysis of the county’s birth rate, 
death rate, and projection of individuals moving to the county, with a breakdown of the demographics in terms of age and place of work?  
Similarly, no estimate is provided of the salaries that the new jobs will pay. Without these, it is impossible to assess whether the employers will pay enough for 
the employees to house themselves, or whether the housing for their employees will need to be subsidized. 

Current and projected demand for square feet of commercial space is provided but this important metric is not provided for housing. 
Given the crucial need for conservation, and pressures facing the county’s residents with respect to access to housing, and the need for energy conservation, 
the plan does not address the potential that smaller homes would provide in meeting housing needs, while maintaining our open spaces, and increasing residential energy efficiency.

""")


st.markdown("""

The description of county goals for growth are not clearly defined and are sometimes unrealistic or inconsistent with Howard County’s unique circumstances.

* Page 4 suggests a need to “ensure affordable housing for all who want to live and work in the County.” 
Rather than addressing the housing needs of the county’s residents, this statement demonstrates a strategy directed for the benefit of outside interests. 
The term “affordable housing” is ambiguous, since in the context of Howard County, affordable housing refers to specific programs to subsidize housing 
for those who qualify. A better goal would be for the county to have a wider variety of housing options available to all its residents. 

* Page 10 attributes the desirability of Howard County as a place to live as being due to its economic growth. This statement overlooks the negative impact 
of growth witnessed in the past ten years in Howard County, such as inadequate infrastructure, devastating storm water runoff from impervious surfaces, 
and loss of open spaces for recreation. It also overlooks the fact that the attraction of Howard County has been for the reputation of the county schools, 
Columbia’s reputation for social inclusion, and for the rural setting conveniently located between Baltimore and Washington DC, all of which are put at 
risk by economic growth, rather than due its growth.

* Page 11 refers to a report of a market demand for 59,000 jobs in the county over two decades, and points out that this is more than twice of what can 
be accommodated with existing land use constraints.

* However, rather than outlining the importance of preserving these constraints, the report concludes that land use changes will need 
to occur in the county. Without an assessment of how these jobs would benefit the county residents, the prioritization of job creation 
over conservation is a disservice to the residents. 

* Page 22. HoCo By Design describes its desire to meet market demand of growth. This strategy prioritizes special interests who profit by sales and development 
over residents who depend on their government to develop policy to maintain a high quality of life.

* The chapter acknowledges the role that the Public Service Area (PSA) plays in curtailing growth. The section STRATEGY FOR GROWTH AND CONSERVATION 
itemizes five categories of negative impact associated with expansion of the Public Service Area. However, the chapter also disregards these as 
it lays out a plan to continue expansion for housing and commercial use. For example, the plan allows expansion of the PSA into 
properties adjoining the existing PSA. Clearly, this would lead to an iterative process, whereby the PSA is expanded throughout the county.

* The Fiscal impact assessment (page 23) describes new growth as generating more revenues than costs for services and infrastructure. 
Yet the report also points out that the revenues referred to are one time costs, rather than the growth’s increased tax base (page 24). 
In this way, the chapter considers only the one time revenues associated with new growth rather than long term costs of services (schools, 
road maintenance, police, hospitals) and costs of negative impact (flooding from runoff water, loss of recreation areas or conversion of 
recreation areas to pay-to-use services)

* The fiscal impact points out that revenues can be generated through local taxes, but provides no discussion of tax rates, in terms of what increases 
would be needed to accommodate new growth.

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