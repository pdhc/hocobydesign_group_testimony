import streamlit as st

st.markdown("""

### County in Motion

****General comments/context****

Transportation includes automobiles and other powered vehicles
(and potentially autonomous vehicles in the future), active transportation focuses on bicycling
(including E-bikes and scooters) and walking, transit includes publicly provided inter and intra
County. All development, redevelopment or remediation of existing transportation shortfalls
plans/reviews should include a holistic assessment of all these forms of transportation. One of
the foundational elements of any assessment should be the equity of the transportation
system, geographically, socio-economically and for residents limited by physically. Technical
terminology in comments below is avoided in favor of plain English. 

****Maintenance**** 

This section pertains to maintaining the transportation system, which addresses the importance of 
investing in the ongoing maintenance and upkeep of the system. Specifically, focus in this section is on physical 
maintenance of roads, sidewalks, bicycling infrastructure, control/directional devices (e.g. stoplights) and transit vehicles.

What is not addressed is the routine clearance of active transportation routes of debris
and snow to ensure the networks are available year-round. Currently sidewalk clearance
has been assumed to be done by adjacent property owners even when not feasible and
bicycle lanes are only done periodically. The maintenance of ancillary
systems/equipment (e.g., bicycle racks, ADA compliant curbs, etc.) should be included.
Bottom line: The lifecycle cost of any transportation infrastructure should be considered
and budgeted for when approved for acquisition.

****Safety****

This section deals with safety and the transportation system, which details the actions the County is taking
to ensure the transportation system is safe for all users>

Includes the physical condition of transportation networks, design of
new/remodeled using best practices, and additions such as crosswalks and devices such
as pedestrian hybrid beacon (AKA Hawk signals). Bottom line: A safety assessment need
to be included in every new transportation project and whenever fatal or serious
accident occur on existing infrastructure.

****Mobility and Access****

This section deals with transportation mobility and access, which addresses the wide range of topics, 
factors, and actions the County considers in managing the transportation system.

In this section mobility equates to ability to keep moving quickly
(traffic) and access to the multi-modal networks to connect people with places they
want to get to. There are key elements on how new development/redevelopment impact should be assessed. 
Current Planning &amp; Zoning (P&amp;Z) technical reports assess road traffic at nearest intersections but road 
traffic is cumulative and the impact (traffic
generated can extend far beyond initial development area to major County and State
roads. In addition, Complete Streets requires the impact of new/denser development on
existing pedestrian and bicycle infrastructure and routes and the opportunity it may
offer to close gaps in existing active transportation infrastructure. Finally, a transit
assessment needs to be implemented which looks at new development, especially
‘Activity Centers’ which need transit to connect them inter and intra County (extending
existing routes or creating new routes) otherwise they will be disconnected islands.
Bottom line: Transportation demand and utilization is cumulative and must be factored
into approval processes.

****Delivering Projects****

This section deals with delivering transportation projects, which outlines the challenges in delivering transportation 
projects and options to accelerate projects. 

One of the gaps mentioned earlier in new transportation
infrastructure is to calculate the lifecycle cost to maintain that infrastructure. Bottom
line: Accelerating projects is good but the implied maintenance required can accumulate
to a point that is unaffordable.


****Future Transportation****

This section deals with the future of the transportation system, which outlines the pending and expected changes facing the
transportation system in the County and region.

Automated vehicles and transit will impact safety on our
transportation infrastructure unless considered at every stage in the approval process.
The other factor the has lingered post-pandemic is work from home for many of the
jobs/professions that in the past have made Howard County an attractive place to live
due to proximity to work opportunities. This may significantly reduce transportation
demand and could decrease demand for housing and intra-County transportation.
Finally, looking at European models sequential transportation (bike-walk-transit) should
be emulated and made viable to reduce vehicle use, congestion and pollution. Bottom
line: The future in unpredictable and transportation planning must be agile and be
constantly monitored and modified as circumstances change.


****Investment Priorities****

This section deals with transportation investment priorities, which details a range of transportation investments to 
support the goals in HoCo By Design.


We cannot continue to develop either horizontally (e.g., spread
into Western County) or vertically (e.g., denser ‘Activity Centers’) without assessing the
impact on transportation as well as other County provided services (schools, fire/police,
parks, etc.). Transportation funding will continue to be limited and maybe more so in
the future with many other deferred and new priorities vying for limited funding. We
must address existing transportation gaps and equity issues across the County before
adding new transportation demand. Bottom line: Dollars are limited and funds must be
utilized to address existing needs before adding new requirements to an already
strained system.

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