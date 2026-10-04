# Passo a Passo
# titulo 
# Secao cadastrar vendas
    #data, vendedor (lista de Vendedor), produto (lista dos produtos), quantidade, valor
    # botao cadastrar venda - clicar no botao cadastra a venda
# Secao vendas cadastradas
    #tabela de vendas
# Secao Dashboard
    # Total vendido card
    # grafico de barra/ venda por vendedor
    # grafico de pizza /  venda por produto
# streamlit run codigovendas.py
# streamlit plotly pandas

import streamlit as st
import plotly.express as px
import pandas as pd

# carregar a base de dados
tabela_vendas= pd.read_csv("vendas.csv")


st.sidebar.write("# Sistema de Cadastro de Vendas")
data= st.sidebar.date_input("Data")
vendedor= st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto= st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade= st.sidebar.number_input("Quantidade", step=1, min_value=1)
valor= st.sidebar.number_input("Valor", step=0.01, min_value=0.01)
botao_cadastrar_venda= st.sidebar.button("Cadastrar Venda")

# logica de cadastro:
if botao_cadastrar_venda:
    nova_venda=[str(data), vendedor, produto, quantidade, valor]
    ultima_linha= len(tabela_vendas)
    tabela_vendas.loc[ultima_linha]= nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada com sucesso!")
    
# Secao cadastrar vendas
st.sidebar.write("## Cadastrar Vendas")
st.dataframe(tabela_vendas)

# Secao Visualizar vendas cadastradas
st.write("## Vendas cadastradas")

# Secao Dashboard
st.write("## Dashboard")

# Card/Metrica -> Faturamento total
faturamento= tabela_vendas["valor"].sum() 
st.metric("Faturamento_Total", f"R${faturamento:.2f}")

# Grafico de barra -> Vendas por vendedor
grafico1=px.bar(tabela_vendas, x="vendedor", y="valor", color="vendedor")
st.plotly_chart(grafico1)

# Grafico de pizza -> Vendas por produto
grafico2= px.pie(tabela_vendas, names="produto", values= "valor", hole=0.3)
st.plotly_chart(grafico2)