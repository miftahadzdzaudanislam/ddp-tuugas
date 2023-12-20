class gempa:
    # Variabel
    tempat = ''
    skala = 0
    laporan = 'Laporan Gempa!'

    # Konstruktor
    def __init__(self, lokasi, skala):
        self.tempat = lokasi
        self.skala = skala

    # Method
    def dampak(self):
        if self.skala < 2:
            print('Dampak gempa\t:  Tidak terasa')
            print()
        elif self.skala > 2 and self.skala < 4:
            print('Dampak gempa\t:  Bangunan retak-retak')
            print()
        elif self.skala >= 4 and self.skala < 6:
            print('Dampak gempa\t:  Bangunan roboh')
            print()
        else:
            print('Dampak gampa\t:  Bangunan roboh dan berpotensi tsunami')
            print()

    def cetak(self):
        print('--------------------------\n',
              gempa.laporan,
              '\n===========================',
              '\nLokasi\t\t: ', self.tempat,
              '\nSkala gempa\t: ', self.skala,)