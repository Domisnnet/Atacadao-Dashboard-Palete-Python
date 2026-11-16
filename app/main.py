import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# Adiciona a pasta src ao caminho para importar o ETL
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.etl import processar_dados

# Configuração da página
st.set_page_config(page_title="Paletes Atacadão CD", page_icon="📦", layout="wide")

st.title("📦 Dashboard de Controle de Paletes - CD Atacadão")
st.markdown("Gestão de PBR e CHEP com rastreabilidade de NFs.")

# Carrega os dados
df = processar_dados('data/dados_exemplo.csv')

# --- Barra Lateral de Filtros ---
st.sidebar.header("Filtros")
tipo_palete = st.sidebar.multiselect("Tipo de Palete", options=df['Tipo_Palete'].unique(), default=df['Tipo_Palete'].unique())
fornecedor = st.sidebar.multiselect("Fornecedor", options=df['Fornecedor'].unique(), default=df['Fornecedor'].unique())

# Filtra o DataFrame
df_filtrado = df[(df['Tipo_Palete'].isin(tipo_palete)) & (df['Fornecedor'].isin(fornecedor))]

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Recebido", f"{df_filtrado['Qtd_Recebida'].sum()} un")
col2.metric("Total Devolvido", f"{df_filtrado['Qtd_Devolvida'].sum()} un")
col3.metric("Saldo Retido no CD", f"{df_filtrado['Saldo_Retido'].sum()} un", delta_color="inverse")

st.divider()

# --- Gráficos ---
col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("Saldo Retido por Fornecedor")
    fig_bar = px.bar(df_filtrado.groupby('Fornecedor')['Saldo_Retido'].sum().reset_index(), 
                     x='Fornecedor', y='Saldo_Retido', color='Fornecedor', text_auto=True)
    st.plotly_chart(fig_bar, use_container_width=True)

with col_dir:
    st.subheader("Status de Rastreamento (NFs)")
    # Tabela interativa detalhada
    st.dataframe(df_filtrado[['NF_Entrada', 'Fornecedor', 'Tipo_Palete', 'Saldo_Retido', 'Status_Devolucao']], use_container_width=True)

st.info("💡 Nota: Dados fictícios para Prova de Conceito. Integração real será via exportação CSV do Cerberus.")