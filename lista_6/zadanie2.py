import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\PYTHON\Programowanie_laby\lista_6\klienci.csv", encoding="utf-8-sig")
print(df.head())


#
do_analizy = df[['klient', 'miasto', 'wojewodztwo', 'zamowienia']]
print(do_analizy)

#sortowanie
posortowane = do_analizy.sort_values(by='zamowienia',ascending=True)
print(posortowane)

#TOP 5
top5 = do_analizy.nlargest(5,'zamowienia')
print(top5)

print()

#suma 
suma = df['zamowienia'].sum()
print(f"łączna ilość zamówionych produktów: {suma}")

# nowa kolumna
df['udzial_procent'] = (df['zamowienia'] / suma * 100).round(2) 

do_analizy = df[['klient', 'miasto', 'wojewodztwo', 'zamowienia', 'udzial_procent']]

top5 = do_analizy.nlargest(5,'zamowienia')
print(top5)


top_10 = (
    df.groupby("klient")["zamowienia"]
    .sum()
    .nlargest(10)
)

top_10.plot.bar(
    title="TOP 10 klientów według liczby zamówionych sztuk",
    xlabel="Klient",
    ylabel="Liczba sztuk",
)

plt.tight_layout()  # Dopasowanie marginesów, aby napisy się nie ucinały
plt.show()


klienci = df.groupby("klient")["zamowienia"].sum()

top_10_suma = klienci.nlargest(10).sum()
pozostali_suma = klienci.sum() - top_10_suma


wartosci = [top_10_suma, pozostali_suma]
etykiety = ["TOP 10 klientów", "Wszyscy pozostali"]


plt.pie(
    wartosci,
    labels=etykiety,
    autopct="%.2f%%",  
    startangle=90      
)

plt.title("Udział TOP 10 klientów w całości")
plt.tight_layout()
plt.show()
