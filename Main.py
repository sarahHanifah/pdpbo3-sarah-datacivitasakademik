from CivitasAkademik import CivitasAkademik
from Mahasiswa import Mahasiswa
from Alumni import Alumni
from Dosen import Dosen

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Saya Sarah Hanifah mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah Desain dan Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.


class path():  # untuk menyimpan path foto dari openfiledialog
    def __init__(self, path):
        self.path = path

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path


def open_file():  # openfiledialog
    file = filedialog.askopenfilename(title="Select file", filetypes=(
        ("jpeg images", ".jpg"), ("png images", ".png"), ("all files", "*.*")))
    if file is not None:
        path.set_path(str(file))


def AddMahasiswa(nama, no_induk, jk, foto, semester, ipk):  # menambah data mahasiswa ke list
    # memastikan bahwa tidak ada isian form yang kosong
    if nama == "" or no_induk == "" or jk == 0 or foto == "" or semester == "" or ipk == "":
        messagebox.showerror(
            title="Hayoloh", message="Isi data dengan lengkap!")
    else:
        if jk == 1:
            jenis_kelamin = "Laki laki"
        else:
            jenis_kelamin = "Perempuan"

        CivitasAkademik.append(
            Mahasiswa(nama, no_induk, jenis_kelamin, foto, semester, ipk))
        messagebox.showinfo(title="Success yeay",
                            message="Data mahasiswa telah ditambakan!")


def AddAlumni(nama, no_induk, jk, foto, tahun_lulus, status_bekerja):  # menambah data alumni ke list
    # memastikan bahwa tidak ada isian form yang kosong
    if nama == "" or no_induk == "" or jk == 0 or foto == "" or tahun_lulus == "" or status_bekerja == 0:
        messagebox.showerror(
            title="Hayoloh", message="Isi data dengan lengkap!")
    else:
        if jk == 1:
            jenis_kelamin = "Laki laki"
        else:
            jenis_kelamin = "Perempuan"
        if status_bekerja == 1:
            sb = "Sudah bekerja"
        else:
            sb = "Belum bekerja"
        CivitasAkademik.append(
            Alumni(nama, no_induk, jenis_kelamin, foto, sb, tahun_lulus))
        messagebox.showinfo(title="Success yeay",
                            message="Data alumni telah ditambakan!")


def AddDosen(nama, no_induk, jk, foto, pt, tmb1, tmb2, tmb3):  # menambah dosen ke list
    # memastikan bahwa tidak ada isian form yang kosong
    if nama == "" or no_induk == "" or jk == 0 or foto == "" or pt == "" or (tmb1 == 0 and tmb2 == 0 and tmb3 == 0):
        messagebox.showerror(
            title="Hayoloh", message="Isi data dengan lengkap!")
    else:
        if jk == 1:
            jenis_kelamin = "Laki laki"
        else:
            jenis_kelamin = "Perempuan"
        mhs = []
        if tmb1 == 1:
            mhs.append("S1")
        if tmb2 == 1:
            mhs.append("S2")
        if tmb3 == 1:
            mhs.append("S3")
        mhs_final = ', '.join(mhs)
        CivitasAkademik.append(
            Dosen(nama, no_induk, jenis_kelamin, foto, pt, mhs_final))
        messagebox.showinfo(title="Success yeay",
                            message="Data dosen telah ditambakan!")


def populate(frame):  # mengisikan data data yg ada di list ke frame
    label_judul = Label(frame, text="Data Civitas Akademik",
                        font=("Calibri", 18, "bold"))
    label_judul.grid(row=0, column=0, columnspan=2)
    j = 1
    ada = 0
    for i, h in enumerate(CivitasAkademik):
        ada = 1
        label_jenis = Label(frame, text=h.get_nama() + " (" + h.get_jenis() + ")",
                            font=("Calibri", 13, "bold"))
        label_jenis.grid(row=j, column=0, columnspan=2)
        j = j+1
        image = Image.open(h.get_foto())
        w = int(image.size[0]/(image.size[1]/130))
        image = ImageTk.PhotoImage(Image.open(
            h.get_foto()).resize((w, 130), Image.ANTIALIAS))
        # load image
        panel = Label(frame, image=image)
        panel.image = image
        panel.grid(row=j, column=0, sticky="w")
        label_isi = Label(frame, text=h.get_summary2(), justify=LEFT)
        label_isi.grid(row=j, column=1, sticky="nw")
        j = j+1

    if ada == 0:  # bila tidak ada data
        label_ket = Label(frame, text="Tidak ada data :(")
        label_ket.grid(row=j, column=0, columnspan=2)


def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))


def view():  # window melihat data civitas akademik
    view = Toplevel()
    view.title("View Data")
    view.update()
    view.minsize(view.winfo_width(), view.winfo_height())
    canvas = Canvas(view)
    frame = Frame(canvas)
    # menambahkan scrollbar pada window
    vsb = Scrollbar(view, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event,
               canvas=canvas: onFrameConfigure(canvas))

    # mengisikan data civitas akademik ke frame melalui fungsi populate
    populate(frame)


def clear():  # fungsi untuk menghapus data yang ada di list
    mb = messagebox.askquestion(
        title="Clear Data", message="Apakah anda yakin untuk menghapus semua data?")
    if mb == "yes":
        CivitasAkademik.clear()
        messagebox.showinfo(
            title="Success", message="Data berhasil dihapus :)")


def about():  # about aplikasi
    about = Toplevel()
    about.title("About")
    frame_about = Frame(about, padx=10, pady=10)
    frame_about.grid(row=0, column=0)
    label_judul = Label(frame_about, text="About", font=(
        "Calibri", 18, "bold")).grid(row=0, column=0)
    label_nama = Label(
        frame_about, text="Nama aplikasi : Data Civitas Akademik").grid(row=1, column=0, sticky="w")
    label_deskripsi = Label(
        frame_about, text="Deskripsi : Aplikasi untuk input data civitas akademik berupa dosen, alumni maupun mahasiswa").grid(row=2, column=0, sticky="w")
    label_pembuat = Label(
        frame_about, text="Pembuat aplikasi : Sarah Hanifah 1909331 C1 Ilmu Komputer").grid(row=3, column=0, sticky="w")


def ask_exit():
    mb = messagebox.askquestion(
        title="Exit", message="Apakah anda yakin untuk keluar aplikasi?")
    if mb == "yes":
        exit()


CivitasAkademik = []

root = Tk()
root.title("1909331 | Sarah Hanifah | C1")
root.update()
root.minsize(root.winfo_width(), root.winfo_height())

frame = Frame(root, padx=10, pady=10)
frame.grid(row=0, column=0)
frame2 = Frame(root, padx=10, pady=10)
frame2.grid(row=0, column=1)

label_judul = Label(
    frame2, text="Data Civitas Akademik\n2020/2021", font=("Calibri", 18, "bold"), anchor="n")
label_judul.grid(row=0, column=0)

button_view = Button(frame2, text="View Data",
                     command=view, width=20, bg="#2c4db0", fg="white")
button_view.grid(row=1, column=0)
button_clear = Button(frame2, text="Clear Data",
                      command=clear, width=20, bg="#2c4db0", fg="white")
button_clear.grid(row=2, column=0)
button_about = Button(frame2, text="About",
                      command=about, width=20, bg="#2c4db0", fg="white")
button_about.grid(row=3, column=0)
button_exit = Button(frame2, text="Exit",
                     command=ask_exit, width=20, bg="#2c4db0", fg="white")
button_exit.grid(row=4, column=0)

# ------------------- FORM ----------------------
OptionList = [
    "Mahasiswa",
    "Alumni",
    "Dosen"
]

variable = StringVar(frame)
variable.set(OptionList[0])

opt = OptionMenu(frame, variable, *OptionList).grid(row=0, column=0)
path = path("")

frame_form = Frame(frame, padx=10, pady=10)  # membuat frame untuk form
frame_form.grid(row=1, column=0)


def callback(*args):  # mengisikan isian form sesuai jenis civitas akademik yang dipilih

    for widget in frame_form.winfo_children():  # direset agar setiap ganti jenis, widget tidak bertumpukan
        widget.destroy()

    label_nama = Label(frame_form, text="Nama : ")
    label_nama.grid(
        row=1, column=0, sticky="w")
    label_noinduk = Label(frame_form, text="No. Induk : ")
    label_noinduk.grid(
        row=2, column=0, sticky="w")
    label_jk = Label(frame_form, text="Jenis kelamin : ")
    label_jk.grid(
        row=3, column=0, sticky="w")
    label_foto = Label(frame_form, text="Foto : ")
    label_foto.grid(
        row=4, column=0, sticky="w")

    entry_nama = Entry(frame_form)
    entry_nama.grid(
        row=1, column=1, sticky="w")
    entry_noinduk = Entry(frame_form)
    entry_noinduk.grid(
        row=2, column=1, sticky="w")

    jk = IntVar()
    rb_l = Radiobutton(frame_form, text="Laki laki", variable=jk,
                       value=1)
    rb_l.grid(row=3, column=1, sticky="w")
    rb_p = Radiobutton(frame_form, text="Perempuan", variable=jk,
                       value=2)
    rb_p.grid(row=3, column=2, sticky="w")

    button_foto = Button(frame_form, text="Select file",
                         command=open_file)
    button_foto.grid(row=4, column=1, sticky="w")

    if variable.get() == "Mahasiswa":
        label_semester = Label(frame_form, text="Semester : ")
        label_semester.grid(
            row=5, column=0, sticky="w")
        label_ipk = Label(frame_form, text="IPK terakhir : ")
        label_ipk.grid(
            row=6, column=0, sticky="w")
        entry_semester = Entry(frame_form)
        entry_semester.grid(row=5, column=1, sticky="w")
        entry_ipk = Entry(frame_form)
        entry_ipk.grid(row=6, column=1, sticky="w")
        button_submit = Button(frame_form, text="Submit", bg="#2c4db0", fg="white", command=lambda: AddMahasiswa(
            entry_nama.get(), entry_noinduk.get(), jk.get(), path.get_path(), entry_semester.get(), entry_ipk.get()))
        button_submit.grid(row=7, column=1)
    elif variable.get() == "Alumni":
        label_sb = Label(frame_form, text="Status bekerja : ")
        label_sb.grid(row=5, column=0, sticky="w")
        label_tl = Label(frame_form, text="Tahun lulus : ")
        label_tl.grid(row=6, column=0, sticky="w")
        k = IntVar()
        rb_sudah = Radiobutton(frame_form, text="Sudah bekerja", variable=k,
                               value=1)
        rb_sudah.grid(row=5, column=1, sticky="w")
        rb_belum = Radiobutton(frame_form, text="Belum bekerja", variable=k,
                               value=2)
        rb_belum.grid(row=5, column=2, sticky="w")
        entry_tl = Entry(frame_form)
        entry_tl.grid(row=6, column=1, sticky="w")
        button_submit = Button(frame_form, text="Submit", bg="#2c4db0", fg="white", command=lambda: AddAlumni(
            entry_nama.get(), entry_noinduk.get(), jk.get(), path.get_path(), entry_tl.get(), k.get()))
        button_submit.grid(row=7, column=1)
    else:
        label_pt = Label(frame_form, text="Pendidikan terakhir : ")
        label_pt.grid(row=5, column=0, sticky="w")
        label_tm = Label(
            frame_form, text="Tingkatan mahasiswa yang dibimbing : ")
        label_tm.grid(row=6, column=0, sticky="w")
        entry_pt = Entry(frame_form)
        entry_pt.grid(row=5, column=1, sticky="w")
        tm1 = IntVar()
        tm2 = IntVar()
        tm3 = IntVar()
        checkbutton_s1 = Checkbutton(
            frame_form, text="S1", variable=tm1, onvalue=1, offvalue=0)
        checkbutton_s1.grid(row=6, column=1, sticky="w")
        checkbutton_s2 = Checkbutton(
            frame_form, text="S2", variable=tm2, onvalue=1, offvalue=0)
        checkbutton_s2.grid(row=6, column=2, sticky="w")
        checkbutton_s3 = Checkbutton(
            frame_form, text="S3", variable=tm3, onvalue=1, offvalue=0)
        checkbutton_s3.grid(row=6, column=3, sticky="w")
        button_submit = Button(frame_form, text="Submit", bg="#2c4db0", fg="white", command=lambda: AddDosen(
            entry_nama.get(), entry_noinduk.get(), jk.get(), path.get_path(), entry_pt.get(), tm1.get(), tm2.get(), tm3.get()))
        button_submit.grid(row=7, column=1)


variable.trace("w", callback)
root.mainloop()
