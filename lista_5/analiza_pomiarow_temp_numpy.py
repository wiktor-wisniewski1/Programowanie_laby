import numpy as np

pomiary = []
ilosc = int(input("Podaj ilość pomiarów: "))
for i in range(ilosc):
    temp = int(input(f"Podaj temperature {i + 1}: "))
    pomiary.append(temp)

pomiary = np.array(pomiary)

print(f"Średnia: {np.mean(pomiary)} C")
print(f"Minimalna: {np.min(pomiary)} C")
print(f"Makysmalna: {np.max(pomiary)} C")
print(f"Rozstęp {np.max(pomiary) - np.min(pomiary)} C")
6