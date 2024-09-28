import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df_partidas_realizadas = pd.read_csv("Partidas_Realizadas.csv")
df_partidas_nao_realizadas = pd.read_csv("Partidas_Nao_Realizadas.csv")
df_classificaçao = pd.read_csv("Classificacao.csv")



pontos_min = df_classificaçao["Pontos"].min()
pontos_max = df_classificaçao["Pontos"].max()

max_pontos = st.sidebar.slider("pontos range", pontos_min, pontos_max, pontos_max)
df_pontos = df_classificaçao[df_classificaçao["Pontos"] <= max_pontos]

df_pontos 

fig = px.bar(df_pontos["Vitorias"].value_counts())
fig2 = px.histogram(df_pontos["Pontos"])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)

