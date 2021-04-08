class CivitasAkademik():
    def __init__(self, jenis, nama, no_induk, jk, foto):
        self.jenis = jenis
        self.nama = nama
        self.no_induk = no_induk
        self.jk = jk
        self.foto = foto

    def get_no_induk(self):
        return self.no_induk

    def get_jk(self):
        return self.jk

    def get_jenis(self):
        return self.jenis

    def get_nama(self):
        return self.nama

    def get_foto(self):
        return self.foto

    def get_summary(self):
        return "Nama : " + self.nama + "\nNo. Induk : " + self.no_induk + "\nJenis kelamin : " + self.jk

# Saya Sarah Hanifah mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah Desain dan Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
