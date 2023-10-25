nama = 'Khairul Azmi Huzaifah'
umur = 13

if(umur < 18):
    ket = 'Anak-Anak'
elif(umur >= 18 and umur <= 65):
    ket = 'Dewasa'
elif(umur > 65):
    ket = 'Lanjut Usia'

print('Nama \t\t:', nama, '\nUmur \t\t:', umur, '\nKategori \t:', ket)

print()

x = 38
y = 5

if(x > y):
    ket = 'x lebih besar dari y'
else:
    ket = 'x lebih kecil dari y'

print('x \t\t:', x, '\ny \t\t:', y, '\nKeterangan \t:', ket)