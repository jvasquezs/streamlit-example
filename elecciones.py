import pandas as pd
import streamlit as st

try:
  mesas=pd.read_csv("https://drive.google.com/file/d/1D5UHd0erineK4asRMBxnpecF1Vu9bd-2",index_col=0)
  print(mesas)
except:
  st.write('Fallo')
  mesas=pd.DataFrame(index=range(1,1000), columns=["Votos","Cernadas","Cufre"])

st.title("""Escrutinio Rapido""")
mesa = st.number_input("""Mesa: """, min_value=1, max_value=900, help="""Número de mesa""")
votos_totales = st.number_input("""Votantes: """, value=1, min_value=1, max_value=400, help="""Cantidad de votantes""")
votos_cernadas = st.number_input("""Votos Cernadas: """, min_value=1, max_value=400, help="""Cantidad de votos Segundo Cernadas""")
votos_cufre = st.number_input("""Votos Cufre: """, min_value=1, max_value=400, help="""Cantidad de votos Claudio Cufre""")

title = st.text_input('Comentarios adicionales: ', '')

if st.button('Guardar'):
  st.write('El porcentaje de votos de JxC es ', ((votos_cernadas+votos_cufre)/votos_totales)*100)
  mesas.loc[mesa] = [votos_totales,votos_cernadas,votos_cufre]
  mesas.to_csv("https://drive.google.com/file/d/1D5UHd0erineK4asRMBxnpecF1Vu9bd-2")
