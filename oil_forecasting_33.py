# -*- coding: utf-8 -*-
"""Oil_forecasting_33.ipynb.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JIYxI11woVCFtur7yrutTPOyviIJtBQw
"""

import streamlit as st
import pandas as pd
import pickle
import matplotlib as plt
import plotly.graph_objects as go
import numpy as np
import plotly.graph_objects as go


import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

# >>>>>>>>> HEADER

st.header(':red[TECH CHALLENGE:] Oil Forecasting', divider='rainbow')

st.markdown('''Você foi contratado(a) para uma consultoria, e seu trabalho envolve analisar os dados de preço do petróleo **Brent**, que pode ser encontrado no site do Ipea.
            Essa base de dados histórica envolve duas colunas: data e preço (em dólares). :fuelpump:''')

st.markdown('''Um grande cliente do segmento pediu para que a consultoria desenvolvesse um **dashboard interativo** e que gere insights relevantes para tomada de decisão.
            Além disso, solicitaram que fosse desenvolvido um **modelo de Machine Learning** para fazer o forecasting do preço do petróleo.''')


# carregando o dataframe
url = ('https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls')
dados = pd.read_excel(url, sheet_name="Data 1", skiprows=2)
dados = dados.rename(columns={'Date': 'date',
                              'Europe Brent Spot Price FOB (Dollars per Barrel)': 'dollars_per_barrel'})

# >>>>>>>>> GRÁFICO
# st.image('images/Imagem1-1.png')

st.subheader('Preço do Petróleo BRENT desde 1987', divider='orange')

st.line_chart(data=dados, x='date', y='dollars_per_barrel',
              color='#df4d4d', use_container_width=True)


# >>>>>>>>> TABS

tab1, tab2, tab3 = st.tabs(["Modelo", "Dashboard", "Info"])
