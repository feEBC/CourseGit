import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Convertir de:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
valor = st.number_input("Valor")

if modo == "Celsius a Fahrenheit":
    resultado = round(valor * 9 / 5 + 32, 2)
    st.write(f"{valor} °C son {resultado} °F")
else:
    resultado = round((valor - 32) * 5 / 9, 2)
    st.write(f"{valor} °F son {resultado} °C")