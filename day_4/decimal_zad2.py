# decimal pozwala ominąć problem zaokrąglenia
# zajmuje dużó pamięci, powolne obliczenia
from decimal import Decimal

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')

suma = kwota1 + kwota2
print('Suma:', suma)

roznica = kwota1 - kwota2
print("Różnica:", roznica)
# Suma: 15.75
# Różnica: 4.75

precyzja = Decimal("0.00")

podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem:", kwota_z_podatkiem)
print("Kwota z podatkiem:", kwota_z_podatkiem.quantize(precyzja))
# Kwota z podatkiem: 12.6075
# Kwota z podatkiem: 12.61
