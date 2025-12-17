import numpy as np
import pandas as pd

# a = pd.Series([15, 14, 13, 12, 11, 10])
# # print(a)
# # print(type(a))
#
# a = np.random.randn(6, 4)
#
# # a = pd.DataFrame(np.random.randn(6, 4), columns=['a', 'b', 'c', 'd'])
# # print(a)
# # df1 = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'), index = list('abcdef'))
# # print(df1)

#Zadanie Fisher Iris
# miejsce na kod zadania
with open("sources/iris.csv") as f:
    d = pd.read_csv(f)

#liczba obiektow
print(d.shape[0])
#liczba atrybutow - tutaj jest ich jeden numeryczny i 4 kategoryczne (species + te swerchu) - nie wliczamy Unnamed
print(d.shape[1])
#liczba kategorii
print(d['species'].unique())
#lub
print(d['species'].nunique())

print(d.groupby("species").mean())