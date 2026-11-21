import numpy as np
ceny = []
ilosc = int(input("Podaj ilość produktów"))
for i in range(ilosc):
    cena = float(input("Podaj cene produktu: "))
    ceny.append(cena)
rabat = int(input("Podaj rabat w (%): "))

ceny = np.array(ceny)
po_rabacie = ceny * (1 - rabat / 100)

print(f"Ceny początkowe: {ceny}")
print(f"Ceny po rabacie: {po_rabacie}")
print(f"Suma przed rabatem: {np.sum(ceny)}")
print(f"Suma po rabacie: {np.sum(po_rabacie)}")
print(f"Ceny powyżej 100zł po rabacie: {po_rabacie[po_rabacie > 100]}")