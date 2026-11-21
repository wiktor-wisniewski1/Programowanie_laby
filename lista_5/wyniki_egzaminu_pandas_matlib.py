import pandas as pd
import matplotlib.pyplot as plt

while True:
    try:
        liczba_studentow = int(input("Podaj liczbę studentów (co najmniej 1): "))
        if liczba_studentow >= 1:
            break
        print("Liczba musi wynosić co najmniej 1.")
    except ValueError:
        print("Proszę podać prawidłową liczbę całkowitą.")

dane = []
for i in range(liczba_studentow):
    nazwisko = input(f"Podaj nazwisko studenta {i+1}: ")
    while True:
        try:
            punkty = float(input(f"Podaj punkty (0-100) dla {nazwisko}: "))
            if 0 <= punkty <= 100:
                break
            print("Punkty muszą być z przedziału od 0 do 100.")
        except ValueError:
            print("Proszę podać prawidłową wartość liczbową.")
    dane.append((nazwisko, punkty))


df = pd.DataFrame(dane, columns=["Nazwisko", "Punkty"])


def przypisz_ocene(punkty):
    if punkty < 50: return 2.0
    elif punkty < 60: return 3.0
    elif punkty < 70: return 3.5
    elif punkty < 80: return 4.0
    elif punkty < 90: return 4.5
    else: return 5.0

df["Ocena"] = df["Punkty"].apply(przypisz_ocene)


print("\n--- Tabela studentów ---")
print(df)

srednia = df["Ocena"].mean()
zdani = (df["Ocena"] >= 3.0).sum()

print(f"\nŚrednia ocen: {srednia:.2f}")
print(f"Liczba studentów z oceną co najmniej 3.0: {zdani}")

df_sorted = df.sort_values(by="Punkty", ascending=False).reset_index(drop=True)
print("\n--- Tabela posortowana malejąco według punktów ---")
print(df_sorted)


plt.figure(figsize=(8, 5))
plt.bar(df_sorted["Nazwisko"], df_sorted["Ocena"], color="#4C72B0", edgecolor="black")
plt.title("Oceny studentów")
plt.xlabel("Nazwisko")
plt.ylabel("Ocena")

plt.yticks([0, 2.0, 3.0, 3.5, 4.0, 4.5, 5.0]) 

plt.tight_layout()
plt.show()