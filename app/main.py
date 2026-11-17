import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.etl import processar_dados
st.set_page_config(page_title="Paletes Atacadão - CD", page_icon="📦", layout="wide")

# CSS
st.markdown("""
<style>
    /* 1. Estilo base de todas as tags */
    div[data-baseweb="tag"] {
        border-radius: 8px !important;
        border: none !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    /* 2. Texto branco por padrão e negrito */
    div[data-baseweb="tag"] span { color: white !important; font-weight: 600; }

    /* =========================================================
       TIPO DE PALETE
    ========================================================= */
    /* PBR (1º botão) - Marrom */
    div[data-testid="stSidebar"] div[data-baseweb="select"]:nth-of-type(1) div[data-baseweb="tag"]:nth-child(1) {
        background-color: #8B5A2B !important;
    }
    
    /* CHEP (2º botão) - Azul */
    div[data-testid="stSidebar"] div[data-baseweb="select"]:nth-of-type(1) div[data-baseweb="tag"]:nth-child(2) {
        background-color: #0056b3 !important;
    }

    /* =========================================================
       FORNECEDORES
    ========================================================= */
    /* Ambev */
    div[data-testid="stSidebar"] div[data-baseweb="select"]:nth-of-type(2) div[data-baseweb="tag"]:nth-child(1) { background-color: #F2B705 !important; }
    /* Ambev: Texto preto para contrastar com o amarelo */
    div[data-testid="stSidebar"] div[data-baseweb="select"]:nth-of-type(2) div[data-baseweb="tag"]:nth-child(1) span { color: black !important; }

    /* Coca-Cola */
    div[data-testid="stSidebar"] div[data-baseweb="select"]:nth-of-type(2) div[data-baseweb="tag"]:nth-child(2) { background-color: #E41E26 !important; }

    /* Nestle */
    div[data-testid="stSidebar"] div[data-baseweb="select"]:nth-of-type(2) div[data-baseweb="tag"]:nth-child(3) { background-color: #005B9F !important; }

    /* Unilever */
    div[data-testid="stSidebar"] div[data-baseweb="select"]:nth-of-type(2) div[data-baseweb="tag"]:nth-child(4) { background-color: #1F3A93 !important; }
</style>
""", unsafe_allow_html=True)

st.title("📦 Controle de Paletes - CD Atacadão:")
st.markdown("Gestão de PBR e CHEP:")
df = processar_dados('data/raw/dados_palete.csv')

# Barra Lateral
st.sidebar.header("🎯 Painel de Filtros.")
st.sidebar.subheader("Tipo de Palete:")

tipo_palete = st.sidebar.multiselect("Selecione:", 
    options=df['Tipo_Palete'].unique(), 
    default=df['Tipo_Palete'].unique(),
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.subheader("Fornecedor:")

fornecedor = st.sidebar.multiselect("Selecione:", 
    options=df['Fornecedor'].unique(), 
    default=df['Fornecedor'].unique(),
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Nota:** O Saldo Retido mostra os paletes que estão no CD.")

# Filtra o DataFrame
df_filtrado = df[(df['Tipo_Palete'].isin(tipo_palete)) & (df['Fornecedor'].isin(fornecedor))]

# KPI's
col1, col2, col3 = st.columns(3)
col1.metric(label="📦 Total Recebido:", value=f"{df_filtrado['Qtd_Recebida'].sum()} un")
col2.metric(label="✅ Paletes Devolvidos:", value=f"{df_filtrado['Qtd_Devolvida'].sum()} un")
col3.metric(label="⚠️ Saldo Retido no CD:", value=f"{df_filtrado['Saldo_Retido'].sum()} un")

st.divider()

# GRÁFICO DE PIZZA
st.subheader("Saldo Retido por Fornecedor:")
cores_marcas = {
    'Ambev': '#F2B705',
    'Coca-Cola': '#E41E26',
    'Nestle': '#005B9F',
    'Unilever': '#1F3A93'
}

# Agrupando os dados
df_pizza = df_filtrado.groupby('Fornecedor')['Saldo_Retido'].sum().reset_index()
df_pizza = df_pizza[df_pizza['Saldo_Retido'] > 0] # Remove quem tem saldo zero

fig_pizza = px.pie(
    df_pizza, 
    values='Saldo_Retido', 
    names='Fornecedor',
    hole=0.65,
    color='Fornecedor',
    color_discrete_map=cores_marcas
)

fig_pizza.update_traces(
    textposition='inside', 
    textinfo='label+value',
    texttemplate='%{label}<br><b>%{value} un</b>',
    marker=dict(line=dict(color="#61616181", width=2)) 
)

fig_pizza.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#FAFAFA', size=14),
    showlegend=False,
    margin=dict(t=30, b=30, l=30, r=30)
)

# Exibindo o gráfico centralizado
col_pizza1, col_pizza2, col_pizza3 = st.columns([1, 2, 1])
with col_pizza2:
    st.plotly_chart(fig_pizza, use_container_width=True)

st.divider()

# Tabela
st.subheader("Status de Rastreamento:")
st.dataframe(
    df_filtrado[['NF_Entrada', 'Fornecedor', 'Tipo_Palete', 'Saldo_Retido', 'Status_Devolucao']], 
    use_container_width=True,
    hide_index=True
)
