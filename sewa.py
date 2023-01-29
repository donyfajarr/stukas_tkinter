from tkinter import *
from tkinter import ttk
from datetime import date
from tkcalendar import DateEntry

jenis = ["Motor", "Mobil"]
kendaraan = [ "LCGC", "SUV", "Sedan", "Minivan", "Elf", "Minibus", "Bus"]
kendaraan1 = ["Matic", "Manual", "Sport"]
fullkendaraan = ["Matic", "Manual", "Sport", "LCGC", "SUV", "Sedan", "Minivan", "Elf", "Minibus", "Bus"]
harga = [150000, 100000, 200000, 300000, 450000, 500000, 650000, 800000, 950000, 1300000]
jenisdatadiri = ["KTP", "SIM", "PASSPORT", "KARTU PELAJAR"]
 
userpass = {'admin' : '123'}
jenischoosen = []
idpelanggan = []
kendaraanchoosen = []
tanggalpelanggan = []
pembeli = []


window = Tk()
window.geometry('300x250')
window.title('Admin Login')
login_frame = Frame(window)
login_frame.pack(padx=25, pady=25)

dashboardlogin = ttk.Label(
    login_frame,
    text="Admin Login",
    font=('Montserrat', 12, 'bold')
)
dashboardlogin.pack()

#1. username
username = Label(login_frame, text='Username')
username.pack(padx=10, fill='x', expand=True)

## masukkan username
inputusername = Entry(login_frame)
inputusername.pack(padx=10,pady=10, fill='x', expand=True)

#2. Password
password = Label(login_frame, text='Password')
password.pack(padx=10, fill='x', expand=True)

## masukkan Password
inputpassword = Entry(login_frame, show='*')
inputpassword.pack(padx=10,pady=10, fill='x', expand=True)

button1 = Button(login_frame, text='Login', command= lambda: [login1()], padx=20, pady=2.5)
button1.pack()

def hitung():
    global jenis, kendaraan, harga, jenisdatadiri
    main_window = Tk()
    main_window.title('Penyewaan Kendaraan')
    frame = Frame(main_window)
    frame.pack()

    framesewa = LabelFrame(frame, padx=25, pady=25)
    framesewa.grid(row=1, column=0, padx=20, pady=5)
    
    #LABEL
    lblinfo = Label(framesewa, font=( 'aria' ,12, 'bold' ),text="Sistem Penyewaan",bd=10,anchor=N)
    lblinfo.grid(row=0,column=1)


    labeljenis= Label(framesewa, text="Jenis Kendaraan :")
    labeljenis.grid(row=2, column=0)
    
    sel= StringVar()

    jenis1 = ttk.Combobox(framesewa, values= jenis, textvariable=sel)
    jenis1.grid(row=2, column =1)

    def my_updt(*args):
        if sel.get() == "Motor":
            tipekendaraan.config(value=kendaraan1)
        else:
            tipekendaraan.config(value= kendaraan)
    sel.trace('w', my_updt)

    labelkendaraan = Label(framesewa, text="Tipe Kendaraan :", anchor=W)
    labelkendaraan.grid(row=3, column=0)
    tipekendaraan = ttk.Combobox(framesewa,)
    tipekendaraan.grid(row=3, column =1)
 
    labeltanggal = Label(framesewa, text="Tanggal Sewa")
    labeltanggal.grid(row=4,column=0)

    cal = DateEntry(framesewa, selectmode='day')
    cal.grid(row=4, column=1, pady=10)

    labellama = Label(framesewa, text="Lama Sewa")
    labellama.grid(row=5, column=0)
    lamasewa = Spinbox(framesewa, from_=1, to=100)
    lamasewa.grid(row=5, column=1, pady=10)

    
 
    labeljenisdata = ttk.Label(framesewa, text="Jenis Data Diri")
    labeljenisdata.grid(row=6, column=0)
    jenisdatadiri1 = ttk.Combobox(framesewa, values= jenisdatadiri)
    jenisdatadiri1.grid(row=6, column=1)

    labeliddata = Label(framesewa, text="Nomor Identitas")
    labeliddata.grid(row=7, column=0)
    iddatadiri = Entry(framesewa)
    iddatadiri.grid(row=7, column=1, pady=10)

    
    frame1 = LabelFrame(frame, padx=25, pady=25)
    frame1.grid(row=2, column=0, padx=20, pady=5)

    label = Label(frame1, text="List Sewa Kendaraan", font=( 'aria' ,12, 'bold' ), bd=10, anchor=N)
    label.grid(row=0, column=2)

    identitas = Label(frame1, text=iddatadiri.get())
    identitas.grid(row=1, column=0)

    no = Label(frame1, text='No')
    no.grid(row=2, column=0, )

    barang = Label(frame1, text='Tipe Kendaraan')
    barang.grid(row=2, column=1, )

    quantity = Label(frame1, text='Lama Sewa')
    quantity.grid(row=2, column=2, )

    harga = Label(frame1, text='Harga')
    harga.grid(row=2, column=3, )

    Total = Label(frame1, text='Total')
    Total.grid(row=2, column=4, )

    for i in frame1.winfo_children():
        i.grid_configure(padx= 15, pady=2)
    for i in framesewa.winfo_children():
        i.grid_configure(padx= 15, pady=2)


    def append():
        jenisdatadiri1.config(state='disabled')
        iddatadiri.config(state='disabled')

        global kendaraan, harga
        p = iddatadiri.get()
        
        # idpelanggan.append(p)
        # jenischoosen.append(jenis1.get())
        # jenischoosen.append(tipekendaraan.get())
        # jenischoosen.append(cal.get())

        # # lamahari = int(lamasewa.get())
        # kendaraanchoosen.append(jenischoosen)

        # idpelanggan.append(kendaraanchoosen)

    
        # idpelanggan.append(kendaraanchoosen)
        # idpelanggan.append(tanggalpelanggan)
        if any(iddatadiri.get() in s for s in pembeli):
            jenischoosen.append(jenis1.get())
            jenischoosen.append(tipekendaraan.get())
            jenischoosen.append(cal.get())
            pembeli.append(jenischoosen)
            
        else:
            pembeli.append(p)
            jenischoosen.append(jenis1.get())
            jenischoosen.append(tipekendaraan.get())
            jenischoosen.append(cal.get())
            pembeli.append(jenischoosen)
            
        
        
        # pembeli.append(kendaraanchoosen)

        print(pembeli)
        # idpelanggan.clear()
        # jenischoosen.clear()
        # print(pembeli)
        # print(pembeli)
        # NESTED LIST MASIH ERROR


        # print(kendaraanchoosen)
        # print(idpelanggan)
        
        
        i = 0
        while i < len(pembeli):
            a1 = fullkendaraan.index(tipekendaraan.get())
            print(a1)
            b1 = (harga[a1])
            print(b1)
            labelno = Label(frame1, text=i+1)
            labelno.grid(row=i+3, column = 0)

            labelbarang = Label(frame1, text=pembeli[i])
            labelbarang.grid(row=i+3, column = 1)

            labellamasewa = Label(frame1, text=lamasewa.get())
            labellamasewa.grid(row=i+3, column = 2)

            labelharga = Label(frame1, text=b1)
            labelharga.grid(row=i+3, column = 3)
            print(pembeli[0])
            i+=1

            #MASIH ERROR HARGA


    checkbutton = Button(framesewa, text='Sewa', command= lambda:[append()], padx= 20, pady=2.5)
    checkbutton.grid(row=8, column=1)
    

    
def login1():
    username = inputusername.get()
    password = inputpassword.get()

    if username in userpass and password == userpass[username]:
        login_frame.destroy()
        window.destroy()
        hitung()
    else:
        pass





login_frame.mainloop()
