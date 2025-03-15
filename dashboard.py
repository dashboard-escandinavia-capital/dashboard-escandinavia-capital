import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Dashboard Escandinávia Capital")

# Carregar os dados (exemplo)
def carregar_dados():
    try:
        df = pd.read_csv("trades.csv")
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["data_hora", "ativo", "tipo", "preco", "quantidade", "valor_total"])

df = carregar_dados()

st.subheader("📋 Últimas Operações")
st.dataframe(df.tail(10))

st.subheader("📈 Performance Acumulada")
if not df.empty:
    df['resultado'] = df.apply(lambda row: -row['valor_total'] if row['tipo'] == 'COMPRA' else row['valor_total'], axis=1)
    df['resultado_acumulado'] = df['resultado'].cumsum()

    plt.figure(figsize=(10, 5))
    plt.plot(df['data_hora'], df['resultado_acumulado'], marker='o')
    plt.xlabel('Data e Hora')
    plt.ylabel('Resultado Acumulado (R$)')
    plt.grid(True)
    st.pyplot(plt)
else:
    st.write("Nenhuma operação registrada ainda.")
