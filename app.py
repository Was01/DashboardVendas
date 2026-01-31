import streamlit as st
import pandas as pd

st.set_page_config(page_title='Meu primeiro site', layout="wide")

try:
    dados = pd.read_csv('resultados.csv')
except FileNotFoundError:
    st.error("Arquivo 'resultados.csv' não encontrado!")
    st.stop()

with st.container():
    st.title('Dashboard de vendas')
    st.subheader('Contratos fechados ao longo de maio')
    st.write('---')

# Cálculos e métricas
total_vendas = 0
contratos_medios = 0
total_registros = 0
max_contratos = 0
data_max_contratos = "N/A"

if not dados.empty:
    total_vendas = dados['Contratos'].sum()
    contratos_medios = dados['Contratos'].mean()
    total_registros = dados.shape[0]
    
    idx_max = dados['Contratos'].idxmax()
    max_contratos = dados.loc[idx_max, 'Contratos']
    data_max_contratos = dados.loc[idx_max, 'Data']

# Seção de métricas 

with st.container():
    st.subheader('Métricas Gerais')
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total de Vendas", f"{total_vendas}")
    c2.metric("Média/Dia", f"{contratos_medios:,.1f}")
    c3.metric("Qtd. Registros", f"{total_registros}")
    c4.metric("Recorde Diário", f"{max_contratos}")
    c5.metric("Data do Recorde", f"{data_max_contratos}")
    st.write('---')

with st.container():
    st.subheader('Gráficos')
    qte_dias=st.selectbox("Selecione o período",["5Dias","10Dias","15Dias","20Dias","30Dias"])
    num_dias=int(qte_dias.replace("Dias",""))
    dados=dados[-num_dias-1:-1]
    st.bar_chart(dados,x='Data',y='Contratos')