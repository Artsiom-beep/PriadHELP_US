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

# Zadanie Jednym z najchętniej wykorzystywanych w dydaktyce analizy danych zbiorów danych jest zbiór Fisher's iris. Zbiór tej jest znajduje się w pliku iris.csv.
#
# wczytaj go z dysku do ramki danych
# określ jej parametry: liczbę obiektów, atrybutów, kategorii
# wyznacz średnie wartości atrybutów w kategoriach


# with open("sources/iris.csv") as f:
#     d = pd.read_csv(f)
#
# #liczba obiektow
# print(d.shape[0])
# #liczba atrybutow - tutaj jest ich jeden numeryczny i 4 kategoryczne - nie wliczamy Unnamed
# print(d.shape[1])
# #liczba kategorii
# print(d['species'].unique())
# #lub
# print(d['species'].nunique())
#
# print(d.groupby("species").mean())






# Zadanie Wczytaj plik waluty1.xls, zawierający kursy trzech walut w pewnym okresie czasu do ramki danych,
# Zapisz dane w nowej ramce danych, a następnie:
#
# określ jego paramtery: liczbę obiektów, atrybutów
# określ dla każdej waluty zmiennośc kursu w całym okresie okresie,
# tj. znajdzie kurs najniższy i najwyższy wskaż daty wystąpienia tych kursów
# (mogą przydać się funkcje np.argmin/np.argmax lub np.idxmin/np.idxmax) oraz policzy różnicę kursową.

# import pandas as pd
#
# # Считаем файл без index_col, чтобы колонки rok, mies, dzien остались
# d = pd.read_excel('sources/waluty1.xls')
# print(d.shape[0])
# print(d.shape[1])
# print(d.head())
#
# d['Data'] = pd.to_datetime({'year': d['rok'], 'month': d['mies'], 'day': d['dzien']})
#
# # Делаем дату индексом
# d.set_index('Data', inplace=True)
#
# # Берём только курсы валют
# kursy = d[['CHF','USD','EUR','JPY']]
#
# # Считаем min, max и разницу
# wyniki = pd.DataFrame({
#     'Min': kursy.min(),
#     'Data_min': kursy.idxmin(),
#     'Max': kursy.max(),
#     'Data_max': kursy.idxmax(),
#     'Roznica': kursy.max() - kursy.min()
# })
#
# print(wyniki)








# Zadanie Wyznacz następujące wartości:
#
# łączną liczbę notowań (lub inaczej: dni, w które giełda pracowała) w kolejnych latach
# liczbę notowań w ciągu całego okresu w poszczególne dni tygodnia
# średnią wartość indeksu w poszczególnych latach
# wzrost poziomu indeksu w poszczególnych latach

# print(wig30seria.head())
# wig30mies = wig30seria.resample(rule = 'ME').mean()
# #wig30mies = wig30mies.groupby(wig30mies.index.year).count()
# #wig30mies = wig30mies.groupby(wig30mies.index.day_name()).count()
# #wig30mies = wig30mies.groupby(wig30mies.index.year).mean()
# wig30seria.groupby(wig30seria.index.year).apply(lambda x: x.iloc[-1] - x.iloc[0])
# wig30mies.head()