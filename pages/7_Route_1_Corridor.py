import streamlit as st

st.markdown("""

### The new zone type proposed for Route 1 is substantially similar to the existing, failed CAC zone type

The Route 1 Corridor should not be a replay of the failed Corridor Activity Center zoning approach. To prevent this from happening, 
incorporate the following recommendations:

* Any “Redevelopment Authority” should have representation from the community, should be subject to open meetings laws, 
and should be subject to the Public Information Act.

* Authorization to assemble parcels for redevelopment should explicitly include assembly of parcels for school sites, 
and should explicitly include assembly of a site for a public high school in Elkridge at the PDX/UPS freight hubs on 
Route 1 across from the Elkridge Library. Schools are an essential part of a community, and the Route 1 corridor 
lacks schools where the students live.

* Property tax incentives for Route 1 redevelopment should not include incentives for residential development. 
A failure of CAC zoning was that residential development is more profitable than other uses, and developers got exemptions 
for the mixed-use developments they were required to create, and built primarily dense residential instead. 
Tax incentives should be focused on encouraging mixed use.


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