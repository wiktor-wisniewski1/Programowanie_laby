import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\PYTHON\Programowanie_laby\lista 6\magazyny.csv", encoding="utf-8-sig")
#print(df.head())


#

wybrane_z_magazyny = ['magazyn','miasto', 'wojewodztwo', 'produkty']
df_wybrane = df[wybrane_z_magazyny]
print(df_wybrane.head())

#3. Wyświetlić liczbę magazynów w pliku.

liczba_magazynów = len(df['magazyn'])
print()
print(f"Liczba magazynów: {liczba_magazynów}")

#4. Posortować magazyny malejąco według kolumny produkty.
df_posortowane = df_wybrane.sort_values(by=['produkty'], ascending=False)
print(df_posortowane)


print()


#5. Wyświetlić 5 magazynów z największą liczbą produktów: identyfikator magazynu, miasto i liczba produktów.
największe = df_posortowane.iloc[:6,:]
print(największe)

#6. Obliczyć i wyświetlić łączną liczbę produktów we wszystkich magazynach.
suma_produktów = df['produkty'].sum()
print()
print(f"Suma produktów: {suma_produktów}")


#7. Narysować wykres poziomy barh() dla 10 magazynów z największą liczbą produktów. Na osi Y umieść identyfikatory magazynów, a na osi X liczbę produktów.

top10 = df.nlargest(10, 'produkty')

plt.figure(figsize=(10, 6))
plt.barh(top10['magazyn'].astype(str), top10['produkty'], color='steelblue')

plt.xlabel('Liczba produktów')
plt.ylabel('Identyfikator magazynu')
plt.title('Top 10 magazynów z największą liczbą produktów')
plt.tight_layout()
plt.show()