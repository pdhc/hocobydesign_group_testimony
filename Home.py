import streamlit as st
st.header("HoCo By Design Community Testimony")

st.markdown("""The Howard County Council is delebrating HoCo By Design - the once-every-ten-year General Plan.
It is imperative that community members share their concerns about the plan. Accordingly, community members have put
together the following testimony, which has been endorsed by the following organizations.
            """)

st.markdown("""
The following organizations and groups are signatories to the following testimony. Organizations who would
like to sign on to this testimony may send info with a point of contact here.
""")
            
st.header(":mailbox: Send group affiliation and contact info here.")

contact_form = """
<form action="https://formsubmit.co/progressivedemsofhoco@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

st.write('----')

st.header("Community Organizations Supporting Testimony")

st.write('---')
hcca,n4b = st.columns(2)
with hcca:
    st.image("groups/hcca.jpg")
with n4b:
    st.image("groups/n4b.jpeg")
st.write('---')
pdhc,sca = st.columns(2)
with pdhc:
    st.image("groups/pdhc.jpeg")
with sca:
    st.image("groups/sca.jpg")
st.write('---')
tpv,ionhoco = st.columns(2)
with tpv:
    st.image("groups/tpv.png")
with ionhoco:
    st.image("groups/ionhoco.jpeg")
st.write('---')
orhoco,ionhoco = st.columns(2)
with orhoco:
    st.image("groups/orhoco.png")

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