# import pandas as pd
# import matplotlib.pyplot as plt
#
# w = pd.read_excel("sources/waluty1.xls")
#
# # 1) rok/mies/dzien -> int (убирает эффект 1970...000002010)
# w["rok"]  = pd.to_numeric(w["rok"],  errors="coerce").astype("Int64")
# w["mies"] = pd.to_numeric(w["mies"], errors="coerce").astype("Int64")
# w["dzien"]= pd.to_numeric(w["dzien"],errors="coerce").astype("Int64")
# w = w.dropna(subset=["rok","mies","dzien"])
#
# # 2) индекс датой (правильнее, чем склейка строк)
# w.index = pd.to_datetime(dict(year=w["rok"], month=w["mies"], day=w["dzien"]))
# w = w.drop(columns=["rok","mies","dzien"]).sort_index()
#
# # 3) все остальные колонки -> числа (курсы)
# for c in w.columns:
#     w[c] = (w[c].astype(str)
#                 .str.replace(",", ".", regex=False)
#                 .str.replace(" ", "", regex=False))
#     w[c] = pd.to_numeric(w[c], errors="coerce")
#
# # 4) дневной график
# w.plot()
# plt.xlabel("Data")
# plt.ylabel("Kurs")
# plt.tight_layout()
# plt.show()
#
# # 5) средние miesięczne (каждый месяц = средняя по дням)
# mies = w.resample("MS").mean()   # MS = начало месяца
# mies.plot()
# plt.xlabel("Data (miesiące)")
# plt.ylabel("Kurs (średnia miesięczna)")
# plt.tight_layout()
# plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt
#
# k = pd.read_excel("sources/kursy.xlsx")
#
# # pierwsza kolumna = data (nie zakładaj nazwy z pliku)
# k = k.rename(columns={k.columns[0]: "Data"})
#
# # zamiana na datetime; błędne wartości (np. "Data") -> NaT
# k["Data"] = pd.to_datetime(k["Data"], errors="coerce")
#
# # usuń wiersze, gdzie data się nie sparsowała (np. wiersz z "Data")
# k = k.dropna(subset=["Data"]).sort_values("Data")
#
# # kolumny cen (dopasuj nazwy jeśli masz polskie znaki / inne nagłówki)
# ceny = ["Otwarcie", "Najwyzszy", "Najnizszy", "Zamkniecie"]
#
# for c in ceny:
#     k[c] = (k[c].astype(str)
#               .str.replace(",", ".", regex=False)
#               .str.replace(" ", "", regex=False))
#     k[c] = pd.to_numeric(k[c], errors="coerce")
#
# k.plot(x="Data", y=ceny)
# plt.xlabel("Data")
# plt.ylabel("Kurs")
# plt.tight_layout()
# plt.show()






# import pandas as pd
# import matplotlib.pyplot as plt
#
# # wczytanie danych
# w = pd.read_excel("sources/waluty1.xls")
#
# # kolumny daty -> int
# w["rok"]   = pd.to_numeric(w["rok"], errors="coerce")
# w["mies"]  = pd.to_numeric(w["mies"], errors="coerce")
# w["dzien"] = pd.to_numeric(w["dzien"], errors="coerce")
# w = w.dropna(subset=["rok", "mies", "dzien"])
#
# # indeks czasowy
# w.index = pd.to_datetime(dict(year=w["rok"], month=w["mies"], day=w["dzien"]))
# w = w.drop(columns=["rok", "mies", "dzien"])
#
# # kolumny walut -> liczby
# for c in w.columns:
#     w[c] = (w[c].astype(str)
#                 .str.replace(",", ".", regex=False)
#                 .str.replace(" ", "", regex=False))
#     w[c] = pd.to_numeric(w[c], errors="coerce")
#
# # średnie roczne (na podstawie kursów dziennych)
# roczne_srednie = w.resample("Y").mean()
# roczne_srednie.index = roczne_srednie.index.year  # tylko rok na osi X
#
# # wykres kolumnowy
# roczne_srednie.plot(kind="bar")
# plt.xlabel("Rok")
# plt.ylabel("Średni kurs")
# plt.tight_layout()
# plt.show()