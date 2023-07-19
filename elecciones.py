import pandas as pd
import streamlit as st

st.title("""Escrutinio Rapido""")
mesa = st.number_input("""Mesa: """, min_value=1, max_value=900, help="""Número de mesa""")
votos_totales = st.number_input("""Votantes: """, value=1, min_value=1, max_value=400, help="""Cantidad de votantes""")
votos_cernadas = st.number_input("""Votos Cernadas: """, min_value=1, max_value=400, help="""Cantidad de votos Segundo Cernadas""")
votos_cufre = st.number_input("""Votos Cufre: """, min_value=1, max_value=400, help="""Cantidad de votos Claudio Cufre""")

title = st.text_input('Comentarios adicionales: ', '')

if st.button('Guardar'):
  st.write('El porcentaje de votos de JxC es ', ((votos_cernadas+votos_cufre)/votos_totales-1)*100)
