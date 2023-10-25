print("1.")
listKendaraan = ["Revo", "Motor", 150, "merah", 2]
print(listKendaraan)

listKendaraan.append("Rp 18.000.000-")
listKendaraan.append("matic")
print(listKendaraan)

listKendaraan.insert(2,"Honda")
print(listKendaraan)

print()

print("2.")
pilih = int (input("""Menghitng luas bangun datar
pilih 1 untuk menghitung luas persegi
pilih 2 untuk menghitung luas lingkaran
pilih 3 untuk menghitung luas segitiga

ingin Menghitung luas bangun datar nomor """))

match pilih:
    case 1:
        print("kamu memilih 1 untuk persegi ")
        s = int(input("masukan sisi "))
        persegi = s * s
        print("Luas persegi",persegi)
    case 2:
        print("kamu memilih 2 untuk lingkaran ")
        r = int(input("masukan jari-jari "))
        phi = 3.14
        lingkaran = phi * r * r
        print("Luas lingkaran",lingkaran)
    case 3:
        print("kamu memilih 3 untuk segitiga: ")
        a = int(input("masukan alas "))
        t = int(input("masukan tinggi "))
        segitiga = 1/2 * a * t
        print("Luas segitiga",segitiga)
    case _:
        print("anda salah memasukan angka")