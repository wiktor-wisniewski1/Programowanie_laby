import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\PYTHON\Programowanie_laby\lista 6\magazyny.csv')
#print(df)

wybrane = df[['magazyn','miasto','wojewodztwo', 'produkty']]
#print(wybrane)


województwo = input("Podaj nazwę województwa:  ")
ilość = int(input("Minimalna liczba prodóktów: "))

po_fitrowaniu = wybrane[
    (wybrane['wojewodztwo'].str.lower() == województwo.lower()) 
    & (wybrane['produkty'] >= ilość)
]
#print(po_fitrowaniu)
if po_fitrowaniu.empty:
    print("Nie ma magazynu, który spełnia wymagania.")
else:
    posortowane = po_fitrowaniu[['magazyn','miasto','produkty']].sort_values(by='produkty',ascending=True)
    suma_produktów = posortowane['produkty'].sum()
    ilość_magazynów = posortowane['magazyn'].count()
    print(posortowane)
    print(f"suma produktów w województwie: {województwo} to: {suma_produktów}")
    print(f"Ilość znalezionych magazynów: {województwo} to: {ilość_magazynów}")    



    top5 = posortowane.nlargest(5,['produkty'])
    print(top5)

    top5.plot(
        x = 'miasto',
        y = 'produkty',
        kind = 'barh',
        color = 'steelblue',
        edgecolor = 'black',
        linewidth = 1.2,
        legend = False,
        figsize = (10,6)
    )

    plt.title('5 magazynów, które mają najwięcej produktów')
    plt.xlabel('miasto')
    plt.ylabel('magazyny')
    plt.tight_layout()
    plt.show()