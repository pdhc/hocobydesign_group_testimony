import streamlit as st

st.markdown("""

### Implementation Details

The General Plan is indeed supposed to be “general” for a reason. Implementation is done over time, starting with
zoning changes that will come next, and development plans showing cohesiveness with the plans goals. 

Since the plan has a very high priority goal of extreme increases in residential development, especially with regard to assumptions that
those efforts will provide more affordable housing units, it becomes very important to include language in the
implementation suggestions in the plan, to make sure that goal does not trump all else, everywhere, no matter what,
and equally importantly, that projects actually will actually provide the benefits assumed.

In the past, when advocates have requested more specific language in the General Plan to get away from really
subjective terms making policy, we have been told the plan must remain general to move with changing times defining
how to serve goals. This go round, the plan includes many, very specific suggestions, several requesting enormous
changes to APFO, and exact examples of development benefits that will supposedly exist. We need to spell out and
require those benefits to protect diverse needs and competing resources.

#### Recommended changes

****Chapter 1**** – Regarding Missing Middle housing – using this need as a goal for high density housing is not appropriate
since it will not necessarily provide it since fees can be paid in lieu of provision. Thus, please edit the implementation
goals to include requirements of a majority of the project giving these or even more affordable units to get benefits,
waivers and fast passes. Suggesting massive benefits for providing a word like “significant” units should be more
specifically defined, at least saying a majority, or some high increase over current required levels.

****Chapter 5**** - p. 37 #2 – Language should be added to safeguard buffering requirements next to existing neighborhoods
for the extreme goal of high density activity centers, many of which are located next to old neighborhoods and shopping
centers right next to R20. Suggested edit - where it notes implementation goals to “allow sufficient density in activity
centers…” ADD “along with improved buffering and retained environmental protections.” Same buffering language
should occur in Chapter 6 p. 44 implementations. This edit will help make high density not just trump all other land use
responsibilities.

****Chapter 6**** - p. 49 – Again, the affordable overlay should have a minimum of what is a “significant portion” of units.

****Chapter 6**** - p. 51 implementing actions – 4 d – Here is an example of specific suggestions of exemptions to be given to
APFO school waits without minimums noted of what is required to get them, or any quantifying of an appropriate
amount of affordable provision. Suggesting that specific exemptions will aid in reaching affordable unit goals without any suggested requirement as to amounts of provision by a project is a recipe for not meeting this goal at all, and it
being taken advantage of, when we could instead use this time to be far more responsible in securing real and genuine
progress.

****Schools**** - Unfortunately, the County continues to misinterpret the HCPSS feasibility study regarding sourcing of new students
from development vs. resales. In Chapter 10, data is presented as to how low a percentage of new students come from
new homes. It is clearly and honestly noted that “new” homes are being defined as new occupancy permits in the last
year. See p. 22 1-c.

****Schools**** - How can we purport to be planning long-term land use goals for the County while still accepting that “new” housing
continue to be defined as producing a new occupancy permit in the last year? How are homes not new development
anymore after one year?

****Schools**** - We must add to p. 22 Implementations in the School Chapter - Add item vi. “Collect Data Sets on sourcing of student
enrollment to define a new development beyond 1 year old units.” When we finally got increased impact fees per unit, 
the proposed increases derived through fiscal analyses deemed relevant to the calculation, were reduced by this exact percentage 
that was in that year’s feasibility study due to the notion that resales made up the rest of student enrollment. 
Not a good myth to keep using in planning.

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