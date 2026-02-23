import streamlit as st
import pandas as pd

st.title("Bases de Datos en la Nube: MongoDB")

st.markdown("""
### Ejercicio
MongoDB es una base de datos NoSQL muy popular que almacena la información de forma muy similar a JSON.

**Instrucciones:**
1. Imagina que tienes acceso a un clúster de MongoDB Atlas. Para este ejercicio no necesitas conectarte realmente a la base de datos a menos que tengas un clúster de prueba.
2. Basándote en el material de clase, escribe el **código necesario (comentado si no tienes conexión)** para conectarte usando `pymongo` y la clase `MongoClient`.
3. Supón que la base de datos se llama `Veterinaria` y la colección se llama `mascotas`.
4. El código debe incluir cómo extraer los documentos y convertirlos en el DataFrame `df_mongo`.
""")

st.subheader("Tu resultado:")
st.markdown("Si no tienes la conexión real, escribe tu código usando `st.code()` para demostrar cómo lo harías teóricamente.")

# ESTUDIANTE: Escribe tu código (o tu st.code teórico) a continuación
codigo_mongo = """
import pandas as pd
from pymongo import MongoClient

# 1. Conectarse a MongoDB Atlas
cliente = MongoClient('mongodb+srv://tu_usuario:tu_clave@cluster.mongodb.net') 

# 2. Seleccionar base de datos y colección
base_datos = cliente["Veterinaria"]
coleccion = base_datos["mascotas"]

# 3. Extraer y convertir
datos = list(coleccion.find())
df_mongo = pd.DataFrame(datos)

# Muestra en Streamlit
st.dataframe(df_mongo)
"""

st.code(codigo_mongo, language="python")
