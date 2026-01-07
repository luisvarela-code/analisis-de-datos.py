# analisis-de-datos.py
Este repositorio contiene un análisis completo del famoso dataset del Titanic, implementando tanto técnicas de análisis exploratorio de datos como visualizaciones profesionales. El proyecto está estructurado en dos scripts principales que trabajan con el dataset de entrenamiento del Titanic.
# Descripcion del archivo titanic.py
Es un analisis detallado del dataset que incluye:
- Carga y exploración inicial de los datos
- Estadísticas descriptivas de las variables clave (edad, clase, supervivencia)
- Procesamiento de datos faltantes (valores nulos)
- Filtrado y segmentación de pasajeros por diferentes criterios
- Cálculo de métricas importantes:
   - Tasa de supervivencia por género y clase
   - Edad promedio por grupo
   - Distribución de pasajeros por puerto de embarque
   - Análisis de pasajeros que viajaban solos.
# Visiualizacion de los datos(graficastitanic.py)
- Histograma de distribución de edades de los pasajeros
- Gráficos de barras de tasa de supervivencia por género y clase
- Boxplot de distribución de edades por género
- Heatmap de tasa de supervivencia por género y clase (visualización bidimensional)
- Gráfico de conteo de pasajeros por puerto de embarque
# Objetivo
- Comprender los factores que influyeron en la supervivencia de los pasajeros
- Identificar patrones demográficos y socioeconómicos entre los pasajeros
- Practicar técnicas de análisis exploratorio de datos (EDA)
- Desarrollar habilidades en visualización de datos con Python
- Crear un portfolio profesional de análisis de datos
# Librerias Utilizadas
- Pandas - Manipulación y análisis de datos
- Seaborn - Visualización estadística
- Matplotlib - Creación de gráficos personalizados
- Jupyter Notebook (implícito) - Entorno de desarrollo
# Visualizaciones por medio de graficas
![image url](https://github.com/luisvarela-code/analisis-de-datos.py/blob/main/analisis%20de%20datos/Figure_1.png?raw=true)
![image url](https://github.com/luisvarela-code/analisis-de-datos.py/blob/main/analisis%20de%20datos/Figure_2.png?raw=true)
![image url](https://github.com/luisvarela-code/analisis-de-datos.py/blob/main/analisis%20de%20datos/Figure_3.png?raw=true)
![image url](https://github.com/luisvarela-code/analisis-de-datos.py/blob/main/analisis%20de%20datos/Figure_4.png?raw=true)
![image url](https://github.com/luisvarela-code/analisis-de-datos.py/blob/main/analisis%20de%20datos/Figure_5.png?raw=true)
![image url](https://github.com/luisvarela-code/analisis-de-datos.py/blob/main/analisis%20de%20datos/Figure_6.png?raw=true)
# Detalles encontrados
- Supervivencia por género: Las mujeres tuvieron una tasa de supervivencia significativamente mayor
- Supervivencia por clase: Los pasajeros de primera clase tuvieron mayores probabilidades de sobrevivir
- Intersección género-clase: Las mujeres de primera clase fueron el grupo con mayor tasa de supervivencia
- Distribución de edades: La mayoría de los pasajeros estaban entre 20 y 40 años
- Puerto de embarque: Southampton fue el puerto con más pasajeros embarcados
