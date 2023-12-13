print('1.')
def profil(nama, alamat, gender, umur, hobi):
    print(f'Nama\t: {nama} \nAlamat\t: {alamat} \nGender\t: {gender} \nUmur\t: {umur} tahun \nHobi\t: {hobi}')
profil('Miftah Adz Dzaudan Islam', 'Parung Bogor',
'Laki-Laki', '19', 'menggambar')

print()
print('2.')
def kelulusan(nilai):
    if nilai <= 60:
        print(nilai, 'Gagal')
    elif nilai <= 70:
        print(nilai, 'Baik')
    elif nilai <= 80:
        print(nilai, 'Sangat Baik')
    elif nilai <= 100:
        print(nilai, 'Istimewa')
    else:
        print('Nilai terlalu besar')
kelulusan(60)

print()
print('3.')
def nilai(x):
    for i in range(x):
        if i%2 == 1:
            print(i,  end=' ')
nilai(100)