# -*- trying out streamlit -*-
"""
Created on Fri Apr 14 11:25:56 2023

@author: David
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Avocado Prices dashboard')

st.markdown('''
This is a dashboard showing the *average prices* of different types of :avocado: 
Data source: [Kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
''')

st.header('Summary statistics')
avocado = pd.read_csv('avocado.csv')
avocado_stats = avocado.groupby('type')['average_price'].mean()
st.dataframe(avocado_stats)

st.header('Line chart by geographies')
with st.form('line_chart'):
    selected_geography = st.selectbox(label='Geography', options=avocado['geography'].unique())
    submitted = st.form_submit_button('Submit')
    if submitted:
        filtered_avocado = avocado[avocado['geography'] == selected_geography]
        line_fig = px.line(filtered_avocado,
                           x='date', y='average_price',
                           color='type',
                           title=f'Avocado Prices in {selected_geography}')
        st.plotly_chart(line_fig)
        
with st.sidebar:
    st.subheader('About')
    st.markdown('This dashboard is made by Just into Data, using **Streamlit**')
    st.sidebar.image('https://streamlit.io/images/brand/streamlit-mark-color.png', width=50)
    
@st.cache_data
def load_data(path):
    dataset = pd.read_csv(path)
    return dataset
avocado = load_data('avocado.csv')