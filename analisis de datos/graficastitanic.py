import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Cargar el archivo CSV
titanic = pd.read_csv(r'train.csv')

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(titanic['Age'].dropna(), kde=True, color='blue', bins=30)
plt.title('Distribución de Edades de los Pasajeros')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# 2. Gráfico de la tasa de supervivencia por género (barplot)
plt.figure(figsize=(8, 6))
sns.barplot(x='Sex', y='Survived', data=titanic, palette='Set2')
plt.title('Tasa de Supervivencia por Género')
plt.xlabel('Género')
plt.ylabel('Tasa de Supervivencia')
plt.show()

# 3. Gráfico de la tasa de supervivencia por clase (barplot)
plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=titanic, palette='Set3')
plt.title('Tasa de Supervivencia por Clase')
plt.xlabel('Clase')
plt.ylabel('Tasa de Supervivencia')
plt.show()

# 4. Gráfico de la distribución de edades por género (boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Sex', y='Age', data=titanic, palette='pastel')
plt.title('Distribución de Edades por Género')
plt.xlabel('Género')
plt.ylabel('Edad')
plt.show()

# 5. Gráfico de la tasa de supervivencia por género y clase (heatmap)
survival_rate = titanic.groupby(['Sex', 'Pclass'])['Survived'].mean().unstack()
plt.figure(figsize=(8, 6))
sns.heatmap(survival_rate, annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Tasa de Supervivencia por Género y Clase')
plt.xlabel('Clase')
plt.ylabel('Género')
plt.show()

# 6. Gráfico de la distribución de pasajeros por puerto de embarque (countplot)
plt.figure(figsize=(8, 6))
sns.countplot(x='Embarked', data=titanic, palette='Set1')
plt.title('Distribución de Pasajeros por Puerto de Embarque')
plt.xlabel('Puerto de Embarque')
plt.ylabel('Número de Pasajeros')
plt.show()
