# Zadanie Napisz funkcję zliczającą brakujące dane. Funkcja powinna zwracać dwie listy (lub wektory albo słowniki)
# - pierwsza zawierające liczby braków w kolejnych obiektach (wiersze), druga dla kolejnych atrybutów (kolumny).

# # miejsce na rozwiązanie zadania
# print(pd.isnull(df))
#
#
# def count_missing(df):
#     """
#     Zwraca:
#     - listę liczby braków w kolejnych wierszach
#     - listę liczby braków w kolejnych kolumnach
#     """
#     missing_rows = df.isna().sum(axis=1).tolist()
#     missing_cols = df.isna().sum(axis=0).tolist()
#     real_rows = df.notna().sum(axis=1).tolist()
#     return missing_rows, missing_cols, real_rows
#
#
# rows, cols, realrows = count_missing(df)
#
# print("\nLiczba braków w wierszach:")
# print(rows, len(rows))
#
# print("\nLiczba braków w kolumnach:")
# print(cols, len(cols))
#
# print("\nLiczba nie brakow w wierszach:")
# print(realrows)






# Zadanie W pliku pasazerowie_lot.xls zawarte są dane o liczbie pasażerów samolotów w latach 2005-16 w państwach należących do Unii Europejskiej
# oraz z nią stowarzyszonych. Dane pochodzą z serwisu internetowego EUROSTAT-u. Wykonaj następujące zadania:
#
# wczytaj plik
# zastanów się, jaka jest najwygodniesza postać ramki danych do dalszego przetwarzania - przekształć dane do tej postaci
# usuń wszystkie obiekty, w których występuje choć jeden brak
# narysuj wykres słupkowy pokazujący łączną liczbę przewiezionych pasażerów z podziałem na lata,
# słupki powinny być posortowane od najkrótszego (najmniej pasażerów), do najdłuższego (najwięcej przewiezionych pasażerów)

# 1. Wczytanie pliku Excel
# # =========================
# df = pd.read_excel("sources/pasazerowie_lot.xls")
#
#
# # Usunięcie wierszy całkowicie pustych
# df = df.dropna()
#
# # Usunięcie wierszy zbiorczych typu EU / Euro (zostają tylko kraje)
# df = df[~df.iloc[:, 0].str.contains("EU|Euro", na=False)]
#
# # Zmiana formatu z szerokiego (lata w kolumnach)
# # na długi: kolumny -> rok, wartości -> liczba pasażerów
# df_long = df.melt(
#     id_vars=df.columns[0],   # kolumna z nazwą kraju
#     var_name="rok",          # nowa kolumna z rokiem
#     value_name="pasazerowie" # nowa kolumna z liczbą pasażerów
# )
#
# # Konwersja wartości na liczby; błędne zapisy zamieniane na NaN
# df_long["pasazerowie"] = pd.to_numeric(
#     df_long["pasazerowie"],
#     errors="coerce"
# )
#
# # Usunięcie wierszy z brakującymi danymi
# df_long = df_long.dropna()
#
# # Zsumowanie liczby pasażerów dla każdego roku
# roczne = (
#     df_long
#     .groupby("rok", as_index=False)["pasazerowie"]
#     .sum()
#     .sort_values("pasazerowie")  # sort od najmniejszej do największej
# )
#
# # Wykres słupkowy: łączna liczba pasażerów w kolejnych latach
# plt.bar(roczne["rok"], roczne["pasazerowie"])
# plt.xticks(rotation=45)          # obrót etykiet lat
# plt.xlabel("Rok")
# plt.ylabel("Liczba pasażerów")
# plt.tight_layout()               # dopasowanie marginesów








# Zadanie W poniższym przykładzie wykorzystano dane o zarobkach (w tysiącach złotych) w dwóch firmach o takiej samej liczbie pracowników,
# umieszczone w ramce danych. Wyznaczono także przeciętne wynagrodzenie w obu firmach jako średnią arytmetyczną oraz jako medianę.
#
# Wyświetl wykres kolumnowy pokazujący zarobki poszczególnych pracowników w każdej z firm.
# Przeanalizuj i porównaj strukturę zarobków w obu firmach.
# Aplikując o pracę i mając jedynie dane o przeciętnym wynagrodzeniu, którą firmę należałoby wybrać?
# Która miara lepiej oddaje sens pojęcia "przeciętne wynagrodzenie" ?
# Z której miary i dlaczego korzysta się podając dane o przeciętnym wynagrodzeniu ?


# b = pd.DataFrame(columns=['firma A', 'firma B'])
#
# b['firma A'] = [2.2, 3.4, 4.3, 4.4, 4.5, 5.5, 6.6, 5.6, 5.6, 6.0,
#                 6.1, 6.3, 7.4, 8.5, 7.7, 7.8, 10.2, 11.3, 15.1]
# b['firma B'] = [3.2, 3.4, 3.3, 3.4, 3.5, 4.5, 3.6, 4.4, 4.5, 5.0,
#                 5.1, 5.3, 5.4, 5.5, 6.7, 6.8, 45.2, 50.3, 45.1]
#
# # wykres kolumnowy
# b.plot(kind='bar')
# plt.xlabel("Pracownik")
# plt.ylabel("Zarobki (tys. zł)")
# plt.tight_layout()
# plt.show()
#
# # średnia i mediana
# for col in b.columns:
#     print(
#         col,
#         "średnia =", b[col].mean(),
#         "mediana =", b[col].median()
#     )









# Zadanie Znajdź w danych z pliku pasazerowie_lot.xls państwa o:
#
# największym i najmniejszym bezwzględnym przyroście liczby pasażerów w całym obserwowanym okresie
# największym i najmniejszym względnym przyroście liczby pasażerów w całym obserwowanym okresie
# lata o największym i najmniejszym przyroście liczby pasażerów w Polsce
# lata o największym i najmniejszym przyroście liczby pasażerów we wszystkich obserwowanych państwach
# zastanów się każdorazowo nad możliwymi iterpretacjami wyników

# Miejsce na kod

# wczytanie i wstępne czyszczenie
# wczytanie i czyszczenie
# df = pd.read_excel("sources/pasazerowie_lot.xls", skiprows=2)
# df = df.dropna()
# df = df[~df.iloc[:, 0].str.contains("EU|Euro", na=False)]
#
# # zapamiętanie nazwy kolumny z krajami
# kol_kraj = df.columns[0]
#
# # format długi
# df_long = df.melt(
#     id_vars=kol_kraj,
#     var_name="rok",
#     value_name="pasazerowie"
# )
#
# df_long["pasazerowie"] = pd.to_numeric(df_long["pasazerowie"], errors="coerce")
# df_long = df_long.dropna()
#
# df_long = df_long.sort_values([kol_kraj, "rok"])
#
# # --- przyrosty krajów ---
# first_last = (
#     df_long
#     .groupby(kol_kraj)
#     .agg(
#         poczatek=("pasazerowie", "first"),
#         koniec=("pasazerowie", "last")
#     )
# )
#
# first_last["przyrost_bezwzgl"] = first_last["koniec"] - first_last["poczatek"]
# first_last["przyrost_wzgledny"] = first_last["przyrost_bezwzgl"] / first_last["poczatek"]
#
# print("Największy bezwzględny przyrost:", first_last["przyrost_bezwzgl"].idxmax())
# print("Najmniejszy bezwzględny przyrost:", first_last["przyrost_bezwzgl"].idxmin())
#
# print("Największy względny przyrost:", first_last["przyrost_wzgledny"].idxmax())
# print("Najmniejszy względny przyrost:", first_last["przyrost_wzgledny"].idxmin())
#
# # --- przyrosty rok do roku ---
# df_long["przyrost"] = df_long.groupby(kol_kraj)["pasazerowie"].diff()
#
# # Polska
# polska = df_long[df_long[kol_kraj] == "Poland"]
# print("Polska – max przyrost:", polska.loc[polska["przyrost"].idxmax(), "rok"])
# print("Polska – min przyrost:", polska.loc[polska["przyrost"].idxmin(), "rok"])
#
# # wszystkie kraje łącznie
# roczne = df_long.groupby("rok")["pasazerowie"].sum().diff()
# print("Wszystkie kraje – max przyrost:", roczne.idxmax())
# print("Wszystkie kraje – min przyrost:", roczne.idxmin())







# Zadanie Wczytaj dane z pliku waluty1.xls. Wykorzystujac miary tendencji centralnej oraz miary rozrzutu określ dla każdej waluty w
# którym półroczu którego roku (rozważ jedynie półrocza, dla których znane są wszystkie kursy) kurs był najwyższy,
# najniższy (biorąc pod uwagę jego wartość średnią w danym okresie) oraz wykazywał największą zmienność.
#
# import pandas as pd
#
# # 1. Wczytanie danych
# df = pd.read_excel("waluty1.xls")
#
# # zakładamy: pierwsza kolumna = data, pozostałe = waluty
# df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])
# df = df.set_index(df.columns[0])
#
# # 2. Rok i półrocze
# df["rok"] = df.index.year
# df["polrocze"] = df.index.month.apply(lambda m: 1 if m <= 6 else 2)
#
# # 3. Usunięcie półroczy z brakami
# df_long = df.reset_index().melt(
#     id_vars=["rok", "polrocze"],
#     value_vars=df.columns[:-2],
#     var_name="waluta",
#     value_name="kurs"
# )
#
# df_long = df_long.dropna()
#
# # zostają tylko pełne półrocza
# liczebnosci = (
#     df_long
#     .groupby(["waluta", "rok", "polrocze"])
#     .size()
# )
#
# pelne = liczebnosci.groupby("waluta").transform("max")
# df_long = df_long[liczebnosci == pelne].reset_index(drop=True)
#
# # 4. Statystyki półroczne
# stat = (
#     df_long
#     .groupby(["waluta", "rok", "polrocze"])
#     .agg(
#         srednia=("kurs", "mean"),
#         odchylenie=("kurs", "std")
#     )
# )
#
# # 5. Wyniki dla każdej waluty
# wyniki = []
#
# for waluta in stat.index.get_level_values(0).unique():
#     s = stat.loc[waluta]
#
#     max_avg = s["srednia"].idxmax()
#     min_avg = s["srednia"].idxmin()
#     max_var = s["odchylenie"].idxmax()
#
#     wyniki.append({
#         "waluta": waluta,
#         "najwyzszy_kurs": max_avg,
#         "najnizszy_kurs": min_avg,
#         "najwieksza_zmiennosc": max_var
#     })
#
# wyniki = pd.DataFrame(wyniki)
# print(wyniki)







# Zadanie Napisz kod umożliwiający ocenę stopnia korelacji kursów walut (z dowolnego źródła danych) w poszczególnych latach oraz
# w całym okresie dla którego dane są dostępne.
# Które waluty były skorelowane najmocniej, a które najsłabiej? O czym może świadczyć korelacja kursów dwóch walut?

# --- 1. Wczytanie danych ---
# założenie: pierwsza kolumna = data, kolejne = kursy walut
# df = pd.read_excel("waluty1.xls")
#
# df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])
# df = df.set_index(df.columns[0])
#
# # --- 2. Korelacja w całym okresie ---
# corr_all = df.corr()
#
# # para walut o najsilniejszej i najsłabszej korelacji (bez przekątnej)
# corr_stack = corr_all.where(~(corr_all == 1)).stack()
#
# najsilniejsza = corr_stack.idxmax(), corr_stack.max()
# najsłabsza = corr_stack.idxmin(), corr_stack.min()
#
# print("Najsilniejsza korelacja (cały okres):", najsilniejsza)
# print("Najsłabsza korelacja (cały okres):", najsłabsza)
#
# # --- 3. Korelacja w poszczególnych latach ---
# df["rok"] = df.index.year
#
# korelacje_roczne = {}
#
# for rok, dane in df.groupby("rok"):
#     dane_waluty = dane.drop(columns="rok")
#     corr = dane_waluty.corr()
#     corr_stack = corr.where(~(corr == 1)).stack()
#     korelacje_roczne[rok] = {
#         "najsilniejsza": (corr_stack.idxmax(), corr_stack.max()),
#         "najsłabsza": (corr_stack.idxmin(), corr_stack.min())
#     }
#
# # podgląd wyników rocznych
# for rok, wynik in korelacje_roczne.items():
#     print(rok, wynik)