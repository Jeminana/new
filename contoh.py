class Murid:
    def __init__(self, nama, kelas, nilai):
        self.nama = nama
        self.kelas = kelas
        self.nilai = nilai
    
    def cetak(self):
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        print("Nilai : ", self.nilai)
    
    