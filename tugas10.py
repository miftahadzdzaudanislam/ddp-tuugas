print('1.')
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

def lulus_saja(siswa_lulus):
    lulus=[]
    for i in siswa_lulus:
        if i['nilai']>65:
            lulus.append(i['nama'])
    return lulus
print('Siswa yang lulus adalah', lulus_saja(hasil_akhir))
print('-------------------------------------------------')

print('2.')
buah2an = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
terbalik = buah2an[::-1]
print(terbalik)
print('--------------------------------------------------')

print('3.')
buah2an = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def double(buah):
    double_buah = []
    for z in buah:
        double_buah.append(z)
        double_buah.append(z)
    return double_buah
print(double(buah2an))
print('-------------------------------------------------')

print('4.')
kampus = ('nurul fikri')
def hapus(kmps):
    kampus_singkat = ''
    for x in kmps:
        if x != 'u' and x != 'i' and x != ' ':
            kampus_singkat += x
    return kampus_singkat
print(hapus(kampus))