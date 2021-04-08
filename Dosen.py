from CivitasAkademik import CivitasAkademik


class Dosen(CivitasAkademik):
    def __init__(self, nama, no_induk, jk, foto, pendidikan_terakhir, tingkatan_mahasiswa_yg_dibimbing):
        super().__init__("Dosen", nama, no_induk, jk, foto)
        self.pendidikan_terakhir = pendidikan_terakhir
        self.tingkatan_mahasiswa_yg_dibimbing = tingkatan_mahasiswa_yg_dibimbing

    def get_pendidikan_terakhir(self):
        return self.pendidikan_terakhir

    def get_tingkatan_mahasiswa_yg_dibimbing(self):
        return self.tingkatan_mahasiswa_yg_dibimbing

    def get_summary2(self):
        return super().get_summary() + "\nPendidikan terakhir : " + self.pendidikan_terakhir + "\nTingkatan mahasiswa yang dibimbing : " + self.tingkatan_mahasiswa_yg_dibimbing

# Saya Sarah Hanifah mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah Desain dan Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
