# Induk class
class animal:
    def __init__(self, nama, makanan, hidup, berkembangBiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak

    def cetak(self):
        print('=======================================================================================================')
        print(f'{self.nama} adalah hewan {self.makanan} yang hidup di {self.hidup} dan berkembang biak dengan cara {self.berkembangBiak}.')

# child class 1
class monyet(animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, kesukaan, sifat):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.kesukaan = kesukaan
        self.sifat = sifat

    def mnyt(self):
        super().cetak()
        print(f'{self.nama} sangat menyukai {self.kesukaan} dan memiliki sifat yang {self.sifat}.')

# child class 2
class platipus(animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, famili, wilayah):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.famili = famili
        self.wilayah = wilayah

    def pltps(self):
        super().cetak()
        print(f'{self.nama} bersasal dari keluarga {self.famili} dan banyak ditemukan di {self.wilayah}.')

# child class 3
class lumba2(animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, kelas, keunikan):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.kelas = kelas
        self.keunikan = keunikan

    def lmb(self):
        super().cetak()
        print(f'{self.nama} termasuk hewan {self.kelas} dan memiliki {self.keunikan}.')

# panggil objek induk
ayam = animal('Ayam', 'omnivora', 'daratan', 'Ovipar')
ayam.cetak()

# panggil child 1
hewan1 = monyet('Monyet', 'Omnivora', 'hutan', 'Vivipar', 'pisang', 'agresif')
hewan1.mnyt()

# panggil child 2
hewan2 = platipus('Platipus', 'Karnivora', 'sungai', 'Ovovipipar', 'Ornithorhynchidae', 'bagian timur benua Australia')
hewan2.pltps()

# panggil child 3
hewan3 = lumba2('Lumba-lumba', 'Karnivora', 'Lautan', 'Vivipar', 'Mamalia', 'otak yang sangat besar')
hewan3.lmb()