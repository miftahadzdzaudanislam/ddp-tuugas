from Gempa import *

# objek
pertama = gempa('Banten', 1.2)
kedua = gempa('Palu', 6.1)
ketiga = gempa('Cianjur', 5.6)
keempat = gempa('Jayapura', 3.3)
kelima = gempa('Garut', 4.0)

# Banten
pertama.cetak()
pertama.dampak()

# Palu
kedua.cetak()
kedua.dampak()

# Cianjur
ketiga.cetak()
ketiga.dampak()

# Jayapura
keempat.cetak()
keempat.dampak()

# Garut
kelima.cetak()
kelima.dampak()