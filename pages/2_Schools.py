import streamlit as st
import matplotlib.pyplot as plt

housing_units = [113125,	115195,	116446,	117826,	119773,	120793,	122593]
total_enrollment = [51681,	52511,	54870,	55638,	56799,	57907,	58868]
year = [2013,2014,2015,2016,2017,2018,2019]
student_yield=[]

for i in range(len(housing_units)):
    student_yield.append(total_enrollment[i] / housing_units[i])


fig, ax = plt.subplots()
ax.plot(year, total_enrollment)
ax.set(xlabel = 'Year')
ax.plot(year, housing_units)
ax.legend(['Total Enrollment', 'Housing Units'])
ax2 = ax.twinx()
ax2.plot(year, student_yield, color = 'red')
ax2.legend(['Student Yield'])

st.markdown("""

### Inadequate attention to schools

In Howard County, there are 0.48 students per residential housing unit. This is an easy number to derive. 
This number has remained stable for the last decade.

The number of students per unit reflects the demographics of the county. The development community tries to 
obfuscate this by talking about different student yields for different types and ages of housing. This is an 
obvious shell game to try to make somebody else pay for the impact of new development. Building types of units 
that have a low student yield does not reduce the growth in enrollment, it just redistributes where the families with kids live.

""")
            
st.pyplot(fig)

st.markdown("""

HoCo By Design should include a plan for building additional school capacity in the amount of 0.5 seats per new residential unit, 
to come online when the proposed residential units come online, plus new capacity to replace the existing portable classrooms. 
Use the allocation table in Chapter 9 as a guide to the projected growth.

New school capacity should be located where the most current and future students are most distant from their existing schools, 
to make transportation times more equitable for all students, and to reduce the overall cost of transporting students. This information is known.

Schools are a critical and significant land use in Howard County, and the Future Land Use Map (FLUM should include the location of future school sites.

The new chapter for School Facilities includes these statements:

****Page 3**** - Strategic Advisory Group Findings - support for “innovative approaches” for new schools. This appears to 
be an attempt to build new schools in the east that are not up to HCPSS standards. All HCPSS schools should be of 
the same quality, and built to the Educational Specification. It is not acceptable to give some parts of the county second rate school facilities.

****Page 8**** - Table 8-5 shows student yield for new housing of various types in different regions. This is misleading. 
On average, every residential unit in Howard County generates on average 0.5 students per unit per year. That is the only relevant number.

****Page 2**** - “Ensure coordination of HoCo By Design and the HCPSS Long Range Master Plan so that school 
capacity projects are planned in activity center areas identified for transformation on the FLUM.”

New capacity projects should be located where there is a shortage of nearby existing capacity. 
Current students with no nearby schools who have endured overcrowding and long bus rides should be a priority over future students in activity 
centers that won’t exist for years. More troubling, this is how to justify never building a high school in Elkridge, where more students travel 
farther to their school than any part of Howard County. 

****Page 12-13 Land Use Considerations**** - There is much talk in this section about reducing the required school site footprints, and it 
even says the only suitable secondary school site is on Marriottsville Road. It ignores the Howard County preferred site for High School 14 in Troy Park, 
which meets the current guidelines for site acreage. There is no need to change the facility standards for HS 14, and there is a site right now.

It is also very disturbing that the Gateway redevelopment is to be planned with their own schools, while there is 
no discussion of building new schools where development has already occurred without schools to go with it. Such as a high school in Elkridge.

##### Recommended changes:

* Require that all new public schools be built to the same Educational Specification standard as existing public schools. 
Limit consideration of ‘innovative approaches” to financing and acquisition issues. All Howard County students deserve the same 
high quality educational experience in a high quality facility.

* There should be an implementing action to prioritize new capacity projects for areas that have been left behind in school 
construction during development that has already occurred. The priority should be to bring the same level of service to all 
existing communities, and future developments can take their turn in line.

* Remove the false and misleading analysis on student yields based on type and age of home, and instead use a simple and easily verified 
yield formula of the number of students divided by the number of housing units in the county. This number has been 0.48 +- 0.1 students/per unit for the last decade.

* Prioritize adding new school capacity in areas where the most students travel farthest to their assigned schools. 
Optimize school locations and attendance area assignments to minimize the variance in travel time system-wide.

* Provide a detailed plan on how will the next general plan address school overcrowding, how will it ensure that communities are not 
segregated by income and race, leading to high concentration of low-income students in some schools.
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