from CivitasAkademik import CivitasAkademik


class Alumni(CivitasAkademik):
    def __init__(self, nama, no_induk, jk, foto, status_bekerja, tahun_lulus):
        super().__init__("Alumni", nama, no_induk, jk, foto)
        self.status_bekerja = status_bekerja
        self.tahun_lulus = tahun_lulus

    def get_status_bekerja(self):
        return self.status_bekerja

    def get_tahun_lulus(self):
        return self.tahun_lulus

    def get_summary2(self):
        return super().get_summary() + "\nTahun lulus : " + self.tahun_lulus + "\nStatus bekerja : " + self.status_bekerja

# Saya Sarah Hanifah mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah Desain dan Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
