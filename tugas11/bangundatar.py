import math

# Modul Bangun Datar

# Segitiga
def segitiga(sisi, alas, tinggi):
    l = 1/2 * alas * tinggi
    k = sisi + sisi + alas
    print()
    print(f'Luas dan keliling segitiga \nsisi = {sisi} \nalas = {alas} tinggi = {tinggi}')
    print(f'Luasnya adalah L = {1/2} x {alas} x {tinggi} = {l}')
    print(f'Kelilingnya adalah K = {sisi} + {sisi} + {alas} = {k}')

# Persegi
def Persegi(sisi):
    l = sisi * sisi
    k = sisi * 4
    print(f'Luas dan keliling persegi \nsisi = {sisi}')
    print(f'Luasnya adalah L = {sisi} x {sisi} = {l}')
    print(f'Kelilingnya adalah K = {sisi} x {4} = {k}')

# Persegi Panjang
def persegi_panjang(sisi1, sisi2):
    l = sisi1 * sisi2
    k = 2 * (sisi1 + sisi2)
    print(f'Luas dan keliling persegi panjang \nsisi pertama = {sisi1} \nsisi kedua = {sisi2}')
    print(f'Luasnya adalah L = {sisi1} x {sisi2} = {l}')
    print(f'Kelilingnya adalah K = {2} x ({sisi1} x {sisi2}) = {k}')

# Belah Ketupat
def belah_ketupat(sisi, d1, d2):
    l = 1/2 * d1 * d2
    k = sisi * 4
    print(f'Luas dan keliling belah ketupat \nsisi = {sisi} \ndiagonal 1 = {d1} \ndiagonal 2 = {d2}')
    print(f'Luasya adalah L = {1/2} x {d1} x {d2} = {l}')
    print(f'Kelilingnya adalah K = {sisi} x {4} = {k}')

# Jajar Genjang
def jajar_genjang(sisi, alas, tinggi):
    l = alas * tinggi
    k = 2 * (sisi + alas)
    print(f'Luas dan keliling jajar genjang \nsisi = {sisi} \nalas = {alas} \ntinggi = {tinggi}')
    print(f'Luasya adalah L = {alas} x {tinggi} = {l}')
    print(f'Kelilingnya adalah K = {2} x ({sisi} + {alas}) = {k}')

# Lingkaran
def lingkarang(jari):
    diagonal = jari + jari
    phi = 3.14
    l = phi * jari ** 2
    k = phi * diagonal
    print(f'Luas dan keliling linkaran \njari-jari = {jari} \ndiagonal = {diagonal}')
    print(f'Luasya adalah L = phi x {jari} x {jari} = {l}')
    print(f'Kelilingnya adalah K = phi x {diagonal} = {k}')

# Layang-Layang
def layang(sisipndk, sisipnjng, d1, d2):
    l = 1/2 * d1 * d2
    k = 2 * (sisipndk + sisipnjng)
    print(f'Luas dan keliling layang-layang \nsisi pendek = {sisipndk} \nsisi panang = {sisipnjng} \ndiagonal 1 = {d1} \ndiagonal 2 = {d2}')
    print(f'Luasya adalah L = {1/2} x {d1} x {d2} = {l}')
    print(f'Kelilingnya adalah K = {2} x ({sisipndk} + {sisipnjng}) = {k}')