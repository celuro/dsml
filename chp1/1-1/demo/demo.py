import pandas as pd

abalone = pd.read_csv('abalone.data', header=None)
print(abalone.head())
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera Weight', 'Shell weight', 'Rings']
print(abalone.head())

iris = pd.read_csv('iris.data')
print(iris.head())

