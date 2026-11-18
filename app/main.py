import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.etl import processar_dados
st.set_page_config(page_title="Paletes Atacadão - CD", page_icon="📦", layout="wide")
st.title("📦 Controle de Paletes - CD Atacadão:")
st.markdown("Gestão de PBR e CHEP:")
df = processar_dados('data/raw/dados_palete.csv') # Fonte dos Dados
st.sidebar.header("🎯 Painel de Filtros") # Barra Lateral
st.sidebar.subheader("Tipo de Palete:")
tipos_disponiveis = df['Tipo_Palete'].unique()
tipos_selecionados = []
for tipo in tipos_disponiveis:
    if st.sidebar.checkbox(tipo, value=True, key=f"tipo_{tipo}"):
        tipos_selecionados.append(tipo)
        
st.sidebar.markdown("---") # Divisória

st.sidebar.subheader("Fornecedor:") # Índice de Fornecedores
fornecedores_disponiveis = df['Fornecedor'].unique()
fornecedores_selecionados = []
for fornecedor in fornecedores_disponiveis:
    if st.sidebar.checkbox(fornecedor, value=True, key=f"forn_{fornecedor}"):
        fornecedores_selecionados.append(fornecedor)

st.sidebar.markdown("---") # Divisória

st.sidebar.info("💡 **Nota:** O Saldo Retido mostra os paletes que estão no CD.") # Nota de Rodapé

df_filtrado = df[(df['Tipo_Palete'].isin(tipos_selecionados)) & (df['Fornecedor'].isin(fornecedores_selecionados))] # Filtragem de Dados
col1, col2, col3 = st.columns(3) # KPI's
col1.metric(label="📦 Total Recebido:", value=f"{df_filtrado['Qtd_Recebida'].sum()} un")
col2.metric(label="✅ Total Devolvido:", value=f"{df_filtrado['Qtd_Devolvida'].sum()} un")
col3.metric(label="⚠️ Saldo Retido no CD:", value=f"{df_filtrado['Saldo_Retido'].sum()} un")
st.divider()

st.subheader("Saldo Retido por Fornecedor:") # GRÁFICO DE PIZZA
cores_marcas = {
    'Ambev': '#F2B705',
    'Coca-Cola': '#E41E26',
    'Nestle': '#005B9F',
    'Unilever': '#1F3A93'
}

df_pizza = df_filtrado.groupby('Fornecedor')['Saldo_Retido'].sum().reset_index()
df_pizza = df_pizza[df_pizza['Saldo_Retido'] > 0] 

# Evita erro no gráfico , se estiver zerado, não exibe o gráfico de pizza
if not df_pizza.empty:
    fig_pizza = px.pie(
        df_pizza, 
        values='Saldo_Retido', 
        names='Fornecedor',
        hole=0.5, 
        color='Fornecedor',
        color_discrete_map=cores_marcas
    )

    fig_pizza.update_traces(
        textposition='inside', 
        textinfo='label+value', 
        texttemplate='%{label}<br><b>%{value} un</b>',
        marker=dict(line=dict(color='#0E1117', width=2)) 
    )

    fig_pizza.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#FAFAFA', size=14),
        showlegend=False,
        margin=dict(t=30, b=30, l=30, r=30)
    )

    col_pizza1, col_pizza2, col_pizza3 = st.columns([1, 2, 1])
    with col_pizza2: st.plotly_chart(fig_pizza, use_container_width=True)
else:
    st.warning("Nenhum dado selecionado nos filtros.")
    
st.divider()

st.subheader("Status de Rastreamento:") # Tabela
def colorir_status(val):
    if "Pendente" in val:
        return 'color: #E41E26; font-weight: bold;' # Vermelho
    elif "Parcial" in val:
        return 'color: #F2B705; font-weight: bold;' # Amarelo
    elif "Devolvido" in val:
        return 'color: #00C853; font-weight: bold;' # Verde
    return ''

df_exibicao = df_filtrado[['NF_Entrada', 'Fornecedor', 'Tipo_Palete', 'Saldo_Retido', 'Status_Devolucao']].copy() # Header da Tabela 
df_exibicao['NF_Entrada'] = df_exibicao['NF_Entrada'].astype(str).str.replace(r'\.0$', '', regex=True)
df_exibicao['Status_Devolucao'] = df_exibicao['Status_Devolucao'].str.replace(r'\.0', '', regex=True)
df_exibicao['Saldo_Retido'] = df_exibicao['Saldo_Retido'].astype(str) + " un"
styled_df = df_exibicao.style.map(colorir_status, subset=['Status_Devolucao'])
st.dataframe( styled_df, use_container_width=True, hide_index=True,
    column_config={
        "NF_Entrada": st.column_config.TextColumn("NF Entrada:", width="small"),
        "Fornecedor": st.column_config.TextColumn("Fornecedor:", width="medium"),
        "Tipo_Palete": st.column_config.TextColumn("Tipo de Palete:", width="small"),
        "Saldo_Retido": st.column_config.TextColumn("Saldo Retido:", width="small"),
        "Status_Devolucao": st.column_config.TextColumn("Status da Devolução:", width="medium")
    }
)
