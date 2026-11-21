import pandas as pd 
import matplotlib.pyplot as plt
df_magazyn = pd.read_csv('C:\PYTHON\Programowanie_laby\lista 6\magazyny.csv')
df_klient = pd.read_csv('C:\PYTHON\Programowanie_laby\lista 6\klienci.csv')
#print(df_magazyn)
#print(df_klient)

wybrane_magazyn = df_magazyn[['wojewodztwo','produkty']]
wybrane_klient = df_klient[['wojewodztwo', 'zamowienia']]
#print(wybrane_klient)
#print(wybrane_magazyn)

suma_magazyn = wybrane_magazyn.groupby('wojewodztwo',as_index=False)['produkty'].sum()
suma_klient = wybrane_klient.groupby('wojewodztwo',as_index=False)['zamowienia'].sum()
#print(suma_magazyn)
#print(suma_klient)

połączone = pd.merge(suma_magazyn, suma_klient, on='wojewodztwo')
#print(połączone)

połączone['roznica'] = połączone['produkty'] - połączone['zamowienia']
#print(połączone)

posortowane = połączone.sort_values(by='roznica',ascending= True)
print(posortowane)

posortowane.plot(
    x='wojewodztwo',
    y=['produkty', 'zamowienia'],
    kind='bar',
    color=['blue', 'orange'],
    edgecolor='black',
    linewidth=1,
    figsize=(10, 6),
)

plt.title('Produkty i zamówienia według województwa')
plt.xlabel('Województwo')
plt.ylabel('Liczba sztuk')
plt.xticks(rotation=45)
plt.legend(['Produkty', 'Zamówienia'])
plt.tight_layout()
plt.show()


kolory = ['red' if x < 0 else 'green' for x in posortowane['roznica']]

posortowane.plot(
    x='wojewodztwo',
    y='roznica',
    kind='barh',
    color=kolory,
    edgecolor='black',
    linewidth=1,
    legend=False,
    figsize=(10, 6),
)

plt.axvline( 0, color='black', linewidth=1)  

plt.title('Różnica (produkty - zamówienia) według województwa')
plt.xlabel('Różnica')
plt.ylabel('Województwo')
plt.tight_layout()
plt.show()
