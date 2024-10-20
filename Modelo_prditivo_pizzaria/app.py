import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_csv('pizzas.csv')


modelo = LinearRegression()
x = df[['diametro']]
y = df[['preco']]

modelo.fit(x, y)
# comando no terminal para chamar = streamlit run app.py
st.title("Prevendo o valor de uma Pizza")
st.divider()

diametro = st.number_input("Digite o tamanho da pizza.")
if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da Pizza no diametro {diametro:.2f} é de R${preco_previsto:.2f}")