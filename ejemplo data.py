
pip install streamlit
pip install pandas

import pandas as pd
import streamlit as st


pip install streamlit
pip install pandas

# 1. Crear a partir de un Diccionario de Listas
datos = {
    'Nombre': ['Ana', 'Luis', 'María'],
    'Edad': [23, 30, 28],
    'Ciudad': ['Madrid', 'Bogotá', 'Lima']
}
df = pd.DataFrame(datos)
print(df)