import streamlit as st

st.markdown("""

### Overview


The PlanHoward 2030 general plan led to explosive increases in the rate of residential development. This explosive increase took place while the county’s laws to mitigate increase in development - the Adequate Public Facilities Ordinance (APFO) - were extremely lax. So much so that by the time APFO was updated in 2018, most of the schools were bursting at the seams.

The consequence has been of course the decline of service. For schools,  deferred maintenance has ballooned, the number of class room trailers continues to increase, county debt shows no signs of declining, our roads are as congested as ever, and much of our other public infrastructure - police, fire, water and sewer, hospitals - continue to experience increasing levels of service demands.

Certain regions have experienced more decline than others. For example, the Route 1 Corridor and Elkridge were left behind. These parts of the county had massive residential development that did not include building sufficient school capacity, infrastructure, and amenities that the rest of the county enjoys.

HoCobyDesign perpetuates the zoning decisions that led to inequities experienced by Elkridge and the Route 1 Corridor. The lack of proper consideration for infrastructure will exacerbate the unsustainable fiscal conditions and burden our infrastructure unless serious efforts are made to consider the impact of residential developments on public facilities. 

Let us be perfectly clear, there are those who say do not build any new houses. There are those who say build an unlimited number of houses. We are saying build the houses that our infrastructure can manage and adjust the rate based on the rate of improvements to infrastructure. Furthermore, all parts of the county should be subject to the same high quality of service.


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