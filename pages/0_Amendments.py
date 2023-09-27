import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
import pygwalker as pyg
import numpy as np
import modules.config as config

st.set_page_config(
    page_title="HOCO BY DESIGN AMENDMENTS",
    layout="wide"
)

# st.markdown(""" # HOCO BY DESIGN AMENDMENTS
    
#     """)

df = pd.read_csv(config.url)
conditions = [(df['Impact']=='None'), (df['Impact']!='None')]
values = ['No', 'Yes']
df['Substantive'] = np.select(conditions, values)
# st.dataframe(df, use_container_width=True)


# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, return_html=True)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True, width=1000)
# sponsor = df.Sponsor.unique()
# selected = st.selectbox('Sponsor', sponsor)

# if selected:
#     df_selected = df[df['Sponsor']==selected]
#     st.write(df_selected.groupby('Substantive')['Impact'].value_counts())
#     # col1, col2 = st.columns()

#     # with col1:
#     #     st.write('Substantive'+df_selected.)

# groupby = st.multiselect('View Table:', df.columns, None)

# if groupby:
#     new_table = fun.group_by_filing_period(df, groupby)
#     st.write(new_table)
