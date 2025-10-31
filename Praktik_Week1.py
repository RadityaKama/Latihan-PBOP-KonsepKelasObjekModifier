# class Mahasiswa:
#     def __init__(self, nama, nim):
#         self.nama = nama
#         self.nim = nim

#     def tampilkaninfo(self):
#         return f"Nama saya adalah {self.nama}, NPM saya adalah {self.nim}"


# mahasiswa1 = Mahasiswa("Raditya Kama Cahyadewa", "5240411098")
# print(mahasiswa1.nama)
# print(mahasiswa1.nim)
# print(mahasiswa1.tampilkaninfo())

class Pemain:
    def __init__(self, nama, posisi, nomor_punggung):
        self.nama = nama
        self.posisi = posisi
        self.nomor = nomor_punggung
        
        print(f"Pemain {self.nama} dengan nomor punggung {self.nomor}, resmi bergabung!")

    def tampilkan_profil(self):
        print(f"- Profil MU -\nNama: {self.nama}\nPosisi: {self.posisi}\nNomor Punggung: {self.nomor}")

    def __del__(self):
        print(f"Pemain {self.nama} telah hengkang dari MU!")

print("\n[BREAKING NEWS! NEW TRANSFER!]")
Sesko = Pemain("Benjamin Sesko", "Penyerang", 30)
Sesko.tampilkan_profil()

print("\n[BREAKING NEWS! OUT!]")
del Sesko