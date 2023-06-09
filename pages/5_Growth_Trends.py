import streamlit as st

st.markdown("""

### Misleading and Dishonest Growth Targets

In the Managing Growth chapter, under the topic “Residential Growth Targets,” the final revision changed the 
target from 1,400 per year to 1,580 per year.  This is misleading, since the actual target is 1580 + 150 Green 
Neighborhood + 150 Affordable = 1880, per Table 10-1 page 4. The target should be defined to include the 
Green Neighborhood and Affordable.

#### Recommended changes

* Define the total number of allocations to include Green Neighborhood and Affordable.

* Set the total number of allocations at 1400, until such a time as there is sufficient school capacity to 
eliminate portable classrooms, and the school maintenance backlog is within the projected revenue streams 
provided by ongoing income and property tax revenues and transfer fees, without relying on impact fees from new 
development.

* Eliminate all recommendations to weaken the APFO law by removing categories of development from APFO requirements.

* Eliminate consideration of “mitigation fees” that allow developers to buy their way out of APFO delays.

* Recommend that the length of APFO delays be tied to the number of portable classrooms in the school system. If 
the number of portable classrooms increases, the APFO delay increases, without grandfathering projects in the 
pipeline. If the number of portable classrooms decreases, the APFO delay decreases. Forbid increasing class sizes 
as a way of reducing the number of portable classrooms.

* Eliminate the notion of Accessory Dwelling Units (ADUs) as a matter of right, as it creates uncertainty in the 
growth of residential development units, and complicates school enrollment projections. ADUs are a bad idea 
generally, as the primary builders of ADUs will be flippers, who will convert owner-occupied homes into multi-unit 
rental properties, which will destabilize established neighborhoods. 

* Forbid school planning projections from incorporating APFO delays into student enrollment growth as is the 
current practice. This has the perverse effect of delaying the construction of new schools. 


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