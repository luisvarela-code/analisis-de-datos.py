import pandas as pd

# Cargar el archivo CSV
titanic = pd.read_csv(r'train.csv')

# Mostrar las primeras filas del DataFrame
titanic.head()

# Obtener información general del DataFrame
titanic.info()

# Estadísticas descriptivas de la columna 'age'
titanic['Age'].describe()

# Contar los valores nulos en la columna 'age'
titanic['Age'].isnull().sum()
# Filtrar pasajeros mayores de 30 años
titanic[titanic['Age'] > 30]

# Calcular la edad promedio de los pasajeros
titanic['Age'].mean()

# Calcular la edad promedio por género
titanic.groupby('Sex')['Age'].mean()

# Contar el número de pasajeros por clase (Pclass)
titanic['Pclass'].value_counts()

# Contar el número de pasajeros que sobrevivieron (Survived = 1) y (Survived = 0)
titanic['Survived'].value_counts()

# Filtrar pasajeros que sobrevivieron y tienen más de 50 años
titanic[(titanic['Survived'] == 1) & (titanic['Age'] > 50)]

# Calcular la tasa de supervivencia por género
titanic.groupby('Sex')['Survived'].mean()

# Calcular la tasa de supervivencia por clase
titanic.groupby('Pclass')['Survived'].mean()

# Calcular la tasa de supervivencia por género y clase
titanic.groupby(['Sex', 'Pclass'])['Survived'].mean()

# Contar el número de pasajeros por puerto de embarque (Embarked)
titanic['Embarked'].value_counts()

# Calcular la edad promedio de los pasajeros que sobrevivieron y los que no
titanic.groupby('Survived')['Age'].mean()

# Contar el número de pasajeros que viajaban solos (sin familiares a bordo)
titanic[(titanic['SibSp'] == 0) & (titanic['Parch'] == 0)].shape[0]

# Calcular la tasa de supervivencia de los pasajeros que viajaban solos
titanic[(titanic['SibSp'] == 0) & (titanic['Parch'] == 0)]['Survived'].mean()
