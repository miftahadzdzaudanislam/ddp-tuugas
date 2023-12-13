import math

# Modul Perhitngan

# Penjumlaan
def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print(f'hasil penjumlahan dari {bil1} + {bil2} = {hasil}')

# Pengurangan
def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print(f'hasil pengurangan dari {bil1} - {bil2} = {hasil}')

# Perkalian
def kali(bil1, bil2):
    hasil = bil1 * bil2
    print(f'hasil perkalian dari {bil1} x {bil2} = {hasil}')

# Pembagian
def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print(f'hasil pembagian dari {bil1} : {bil2} = {hasil}')

# Perpangkatan
def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print(f'hasil dari {bil1} pangkat {bil2} = {hasil}')

# Logaritma
def log(bil1):
    hasil = math.log(bil1)
    print(f'hasil dari log{bil1} = {hasil}')

# Akar
def akar(bil1):
    hasil = math.sqrt(bil1)
    print(f'hasil akar dari {bil1} = {hasil}')

# Sin
def sin(bil1):
    hasil = math.sin(bil1)
    print(f'hasil Sin dari {bil1} = {hasil}')

# Cos
def cos(bil1):
    hasil = math.cos(bil1)
    print(f'hasil Cos dari {bil1} = {hasil}')

# Tan
def tan(bil1):
    hasil = math.tan(bil1)
    print(f'hasil Tan dari {bil1} = {hasil}')