#Importar las librerías necesarias.
import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import os

#Cargar el dataset proporcionado en un DataFrame de Pandas.
DataAnalisis = pd.read_csv("DataAnalytics.csv")

#Mostrar las primeras y últimas filas del DataFrame para una inspección visual.
DataAnalisis.head(5)
DataAnalisis.tail(5)

#Mostrar el tamaño del dataset (número de filas y columnas).
print(DataAnalisis.shape)
print(DataAnalisis.size)

print("Número de filas", len(DataAnalisis))
print("Número de columnas", len(DataAnalisis.columns))

#Listar los nombres de las columnas y sus tipos de datos.
DataAnalisis.info()

#Verificar si hay valores nulos y calcular su porcentaje por columna.
DataAnalisis.isnull().sum()

#Detectar y eliminar filas o columnas innecesarias.
print("No considero necesario borrar columnas ni filas")

#Convertir tipos de datos si es necesario (por ejemplo, fechas).
print("Los datos ya están en su formato correcto")

#Renombrar columnas para hacerlas más descriptivas.##


#Explorar estadísticas generales de las columnas numéricas.##


#Verificar la distribución de los datos clave, como el tiempo de interacción y el número de interacciones (para analizar estas distribuciones, utilizar histogramas).
plt.figure(figsize=(8,5))
sns.histplot(DataAnalisis['tiempo de interacción'], bins= 20, kde= True)
plt.title("Distribución del tiempo de interacción")
plt.xlabel("Tiempo de interacciones")
plt.ylabel("?")
plt.grid()
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(DataAnalisis['número de interacción'], bins= 20, kde= True)
plt.title("Distribución del número de interacción")
plt.xlabel("Número de interacciones")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()

#Analizar los valores únicos en columnas categóricas (colores presionados, juegos, dificultad).##


#Explorar el contenido de los datos con los métodos estudiados (datos repetidos, nulos, valores atípicos, consultas generales).
valores_nulos = DataAnalisis.isnull().sum()
valores_nulos

DataAnalisis1 = DataAnalisis.fillna(method = "bfill").fillna(method = "ffill")
DataAnalisis1

valores_nulos = DataAnalisis1.isnull().sum()
valores_nulos

cuantitativas = DataAnalisis1.select_dtypes(include=['float64', 'int64', 'float', 'int'])
cualitativas = DataAnalisis1.iloc[ : , [0]]

fig = plt.figure(figsize = (15, 8))
cuantitativas.plot(kind = 'box', vert = False)
plt.title("Valores atípicos del DataFrame")
plt.show() #Dibujamos el diagrama

#detectar el rango intercualitico 
y = cuantitativas

porcentaje25 = y.quantile(0.25) #Q1
porcentaje75 = y.quantile(0.75) #Q3
iqr = porcentaje75 - porcentaje25

limiter_sup_iqr = porcentaje75 + 1.5*iqr 
limiter_inf_iqr = porcentaje25 - 1.5*iqr 

print(limiter_sup_iqr)
print(limiter_inf_iqr)

DataAnalisis_iqr = cuantitativas[(y<=limiter_sup_iqr)&(y>=limiter_inf_iqr)]
DataAnalisis_iqr

valores_nulos=DataAnalisis_iqr.isnull().sum()
valores_nulos

DataAnalisis2_iqr=DataAnalisis_iqr.copy()
DataAnalisis2_iqr=DataAnalisis2_iqr.fillna(round(DataAnalisis_iqr.mean(),1))
DataAnalisis2_iqr

IQR = pd.concat([cualitativas, DataAnalisis2_iqr], axis=1)
IQR

valores_nulos=IQR.isnull().sum()
valores_nulos

