import streamlit as st

st.markdown("""
### Destruction of our Historic Districts

In the Quality by Design chapter, page 25, it states “According to the Development Regulations Assessment, 
there could be opportunities to revise the historic district zones in the County. Currently, the Zoning Regulations 
describe the requirements and restrictions applicable to historic districts instead of generally addressing the 
allowable land uses or development standards. 

Frequently, in zoning regulations, historic districts are identified with an overlay zone or as a character-based 
district that more clearly defines the boundaries and helps demonstrate how 
historic preservation regulations interact with underlying zoning and subdivision regulations. 

Overlay zones with a clearly defined base zoning district can help provide predictability of permitted uses within a historic district, 
encourage development patterns that are consistent with the historic character, and create opportunities to 
establish future districts that may benefit from such designation criteria.” 

On page 25 it states “Evaluate the existing historic district zones and consider replacing them with new historic zoning 
district overlays or form-based districts”.

We should not be encouraging development in historic districts. This is wildly inappropriate. This section is nothing 
but an attempt to allow developers to destroy our historic districts.

Our existing historic districts have clearly defined boundaries, and there is no confusion about how historic 
preservation regulations interact with underlying zoning. Developers attempt to manufacture confusion when they want to do 
things that are inappropriate and not permitted by the established guidelines.

In the Character Area technical appendix, the final revision to the ‘Historic Communities’ and ‘Single-Family Neighborhood,’ topic 
modified the narrative to state that character should be prioritized rather than paramount. The reason for doing this is 
“Concern that language describing character as ‘paramount’ in certain character areas could prohibit diverse housing 
types envisioned in the Plan.” 

This is no reason to eliminate the 'paramount' language, especially in Historic Communities. Protecting the integrity of our historic 
districts does not contravene building diverse housing types and there are certain parts of the county where that is not ideal. 
Historic districts are special places. Once the historic integrity is lost, it’s gone forever.

#### Recommended changes:

* Remove the false and misleading discussion that misrepresents the current historic district boundaries and governance in Howard County.

* Strengthen the Historic Preservation Commission by requiring a Certificate of Approval for subdivision plans within historic districts.


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