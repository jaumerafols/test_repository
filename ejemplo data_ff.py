
## pip install streamlit

import streamlit as st
import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear el gráfico
plt.plot(x, y, label='Línea de tendencia', color='blue', marker='o')

# Personalización
plt.title('Gráfico de Línea Simple')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()