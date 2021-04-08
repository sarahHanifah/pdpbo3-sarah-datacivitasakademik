from CivitasAkademik import CivitasAkademik


class Mahasiswa(CivitasAkademik):
    def __init__(self, nama, no_induk, jk, foto, semester, ipk_terakhir):
        super().__init__("Mahasiswa", nama, no_induk, jk, foto)
        self.semester = semester
        self.ipk_terakhir = ipk_terakhir

    def get_semester(self):
        return self.semester

    def get_ipk_terakhir(self):
        return self.ipk_terakhir

    def get_summary2(self):
        return super().get_summary() + "\nSemester : " + self.semester + "\nIPK terakhir : " + self.ipk_terakhir

# Saya Sarah Hanifah mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah Desain dan Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
