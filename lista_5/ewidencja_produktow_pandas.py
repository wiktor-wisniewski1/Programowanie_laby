import pandas as pd
df = pd.DataFrame({
"Produkt" : ["Mysz","Klawiatura", "Monitor", "Podkladka"],
"Cena" : [50, 120, 650, 30],
"Ilosc" : [10, 5, 3, 20]
})


df["wartość"] = df["Cena"] * df["Ilosc"]

print(pd.DataFrame(df))
print(f"Droższe niż 100zł: {df["Produkt"][df["Cena"] > 100] }")
print(f"Wartość magazynu: {df["wartość"].sum() }zł")
print(f"średnia cena: {df["Cena"].mean()}zł")
