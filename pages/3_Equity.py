import streamlit as st

st.markdown("""

### Abuse of the concept of Equity to treat some communities inequitably

In the Introduction and in Chapter 8, Infrastructure, there is a discussion of Equity in Capital Planning, which proposed that Complete Streets and 
Recreation and Parks projects should be prioritized “through an equity lens” as bike and pedestrian projects are now.

For bike projects, the history of this approach has produced spectacularly inequitable results.  Columba, which already had the best bike infrastructure 
in the county, has received a disproportionate share of new infrastructure investment, while other parts of the county like Elkridge, which has no bike 
infrastructure at all, has received no investment to speak of.

The cause of this inequitable outcome is based on two factors.

1. The “equitable” prioritization process does not consider what infrastructure already is in place. There is no establishment of a 
baseline service level, and no determination of shortfalls against the baseline.

2. A false assumption that communities with a larger disadvantaged population (Columbia) have historically received a lower level 
of county investment and services.

It is worth noting that there is no “Equity Lens” in the planning for Water and Sewer, Police, and Fire Protection. Why is that?

Perhaps it is because the current planning approach for these types of infrastructure produce an equitable result. These departments 
determine the level of service to be provided to everyone, determine the baseline of what service is currently provided, look at shortfalls 
and growth trends, and build a budget to invest appropriately. For sewer service, developers have to pay up front!

There is no reason why Complete Streets, Recreation and Parks, and bike and pedestrian infrastructure cannot be handled in the same way. 
An obvious conclusion is that “equity” is nothing more than a pretext to make an inequitable bias in favor of Columbia for new investment.

Recommended changes
Explicitly require priority for investment in underserved parts of the county, to bring all parts of the county up to the same level of county services. “Underserved” does not mean the presence of disadvantaged populations. It means places that do not have services such as nearby schools, complete streets, community centers, and facilities for recreation and arts, and so on.


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