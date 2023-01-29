from tkinter import *
from tkinter import ttk
from datetime import date


jenis = ["Motor", "Mobil"]
kendaraan = ["Matic", "Manual", "Sport", "LCGC", "SUV", "Sedan", "Minivan", "Elf", "Minibus", "Bus"]
harga = [150000, 100000, 200000, 300000, 450000, 500000, 650000, 800000, 950000, 1300000]
jenisdatadiri = ["KTP", "SIM", "PASSPORT", "KARTU PELAJAR"]
 
userpass = {'admin' : '123'}
idpelanggan = []
kendaraanchoosen = []
hargapelanggan = []
tenggatpelanggan = []
# NANTI ISINYA LIST DALAM LIST BUAT TAMPIL DI GUI
tampilsewa = []
rincian = []
def login1():
    username = inputusername.get()
    password = inputpassword.get()

    if username in userpass and password == userpass[username]:
        login_frame.destroy()
        window.destroy()
        
        main_window = Tk()
        main_window.title('Penyewaan Kendaraan')
        frame = Frame(main_window)
        frame.pack()

        framesewa = LabelFrame(frame, padx=25, pady=25)
        framesewa.grid(row=0, column=0, padx=20, pady=5)

        framerincian = LabelFrame(frame, padx=25, pady=25)
        framerincian.grid(row=1, column=0, padx=20, pady=5)

        today = date.today()
        d1 = today.strftime("%d")
        d2 = today.strftime("%m")
        d3 = today.strftime("%Y")
        d4 = today.strftime("%B %d, %Y")


        #LABEL
        lblinfo = Label(framesewa, font=( 'aria' ,30, 'bold' ),text="Sistem Penyewaan",bd=10,anchor=N)
        lblinfo.grid(row=0,column=0)
        lblinfo = Label(framesewa, font=( 'aria' ,12, ),text=d4,anchor=N)
        lblinfo.grid(row=1,column=0)

        labeljenis= Label(framesewa, text="Jenis Kendaraan :")
        labeljenis.grid(row=2, column=0)
        entryjenis = ttk.Combobox(framesewa, values= jenis)
        entryjenis.grid(row=2, column =1)

        labelkendaraan = Label(framesewa, text="Tipe Kendaraan :", anchor=W)
        labelkendaraan.grid(row=3, column=0)
        tipekendaraan = ttk.Combobox(framesewa, values= kendaraan, text="Jenis Ruangan :")
        tipekendaraan.grid(row=3, column =1)

        labeltanggal = Label(framesewa, text="Tanggal Sewa")
        labeltanggal.grid(row=4,column=0)

        harisewa = ttk.Combobox(framesewa, width=3)
        bulansewa = ttk.Combobox(framesewa, width=3)
        tahunsewa = ttk.Combobox(framesewa, width=4)



        dayl = [str(i) for i in range(32)]
        dayl[0]=d1
        harisewa['values'] = dayl


        bulansewa['values'] = (d2,
                                ' January',  
                                ' February', 
                                ' March', 
                                ' April', 
                                ' May', 
                                ' June', 
                                ' July', 
                                ' August', 
                                ' September', 
                                ' October', 
                                ' November', 
                                ' December') 

        yearl = [str(i) for i in range(2022 ,2222)]
        yearl[0]=d3
        tahunsewa['values'] = yearl

        harisewa.current(0)
        harisewa.place(x=378, y=138)
        bulansewa.current(0)
        bulansewa.place(x=425, y=138)
        tahunsewa.current(0)
        tahunsewa.place(x=474, y=138)



        labellama = Label(framesewa, text="Lama Sewa")
        labellama.grid(row=5, column=0)
        lamasewa = Spinbox(framesewa, from_=1, to=100)
        lamasewa.grid(row=5, column=1, pady=10)

        labeljenisdata = ttk.Label(framesewa, text="Jenis Data Diri")
        labeljenisdata.grid(row=6, column=0)
        entryjenisdatadiri = ttk.Combobox(framesewa, values=jenisdatadiri)
        entryjenisdatadiri.grid(row=6, column=1)

        labeliddata = Label(framesewa, text="Nomor Identitas")
        labeliddata.grid(row=7, column=0)
        iddatadiri = Entry(framesewa)
        iddatadiri.grid(row=7, column=1, pady=10)

        def hitung():
            global rincian, idpelanggan
            entryjenisdatadiri.config(state='disabled')
            iddatadiri.config(state="disabled") #PROHIBIT ENTRY DIGANTI


            label = Label(framerincian, text="List Sewa Kendaraan")
            label.grid(row=0, column=2)

            no = Label(framerincian, text='No')
            no.grid(row=1, column=0, )

            id = Label(framerincian, text='ID Pelanggan')
            id.grid(row=1, column = 1)

            barang = Label(framerincian, text='Tipe Kendaraan')
            barang.grid(row=1, column=2, )

            quantity = Label(framerincian, text='Lama Sewa')
            quantity.grid(row=1, column=3, )

            hargas = Label(framerincian, text='Harga')
            hargas.grid(row=1, column=4, )

            Total = Label(framerincian, text='Total')
            Total.grid(row=1, column=5, )

            for i in framerincian.winfo_children():
                i.grid_configure(padx= 15, pady=2)

            # p = entryjenisdatadiri.get() + " " + iddatadiri.get()
        
            kendaraanchoosen.append(tipekendaraan.get())
            # idpelanggan.append(p)
            lamahari = int(lamasewa.get()) + int(harisewa.get())
            z = str(lamahari)
            tenggat = z + "-" + bulansewa.get() + "-" + tahunsewa.get()
            tenggatpelanggan.append(tenggat)

            f = kendaraanchoosen[-1]
            a = kendaraan.index(f)
            
            totalbayar = harga[a] * lamahari
            hargapelanggan.append(totalbayar)

            if any(iddatadiri.get() in s for s in rincian):
                tampilsewa.append(tipekendaraan.get())
                tampilsewa.append(entryjenis.get())
                tampilsewa.append(totalbayar)
                tampilsewa.append(tenggat)
                idpelanggan.append(tampilsewa)
                rincian.append(idpelanggan)
                print(tampilsewa)
                print(idpelanggan)
            else:
                idpelanggan.append(iddatadiri.get())
                tampilsewa.append(tipekendaraan.get())
                tampilsewa.append(entryjenis.get())
                tampilsewa.append(totalbayar)
                tampilsewa.append(tenggat)
                idpelanggan.append(tampilsewa)
                rincian.append(idpelanggan)
                print(tampilsewa)
                print(idpelanggan)
            
            tampilsewa.clear()
            print(rincian)
            # [[id[asdas,asasd,asdasd][adas,asda,asda,]]]
            
            # print(totalbayar)
            # print(tenggatpelanggan)
            
            # print(kendaraanchoosen)
            # print(tampilsewa)


        checkbutton = Button(framesewa, text='Sewa', command= lambda: [hitung()], padx= 20, pady=2.5)
        checkbutton.grid(row=8, column=1)



    else:
        pass


# def hitung():
#     global jenis, kendaraan, harga, jenisdatadiri
    

#     def append():
#         global kendaraan, harga
#         # kendaraan.get()
#         # iddatadiri.get()
#         # lamasewa = lamasewa.get()
#         # harisewa = harisewa.get()
#         # bulansewa = bulansewa.get()
#         # tahunsewa = tahunsewa.get()
#         
        
#         framesewa.destroy()
#         window.destroy()

#         window = Toplevel()
        

#         frame0 = Frame(window)
#         frame0.grid(row=0, column=0, sticky='news', padx=20, pady=5)
        
#         identitas = Label(frame0, text=idpelanggan[-1])
#         identitas.grid(row=0, column=0)

#         frame1 = Frame(window)
#         frame1.grid(row=1, column=0, sticky='news', padx=20, pady=5)
        
#         

        # def keranjang():
        #     global no1, barang, quantity, harga, Total
        #     i= 0
        #     while i < len(listsewa):

        #         no1 = Label(frame1, text= 1 + i)
        #         no1.grid(row=i+1, column=0,)

        #         barang = Label(frame1, text= kendaraan[i])
        #         barang.grid(row=i+1, column=1, )

        #         quantity = Label(frame1, text= [i])
        #         quantity.grid(row=i+1, column=2, )

        #         harga = Label(frame1, text= '{:,.2f}'.format(listharganow[i]))
        #         harga.grid(row=i+1, column=3, )

        #         Total = Label(frame1, text='{:,.2f}'.format(listtotalharga[i]))
        #         Total.grid(row=i+1, column=4, )

        #         listlabel.append(no1)
        #         listlabel.append(barang)
        #         listlabel.append(quantity)
        #         listlabel.append(harga)
        #         listlabel.append(Total)

        #         i += 1

        # listbox = Listbox(frame1)
        # listbox.pack(side = LEFT, fill=BOTH)
        # scrollbar = Scrollbar(frame1)
        # scrollbar.pack(side = RIGHT, fill=BOTH)
        # listbox.insert(END,kendaraanchoosen)
        # listbox.config(yscrollcommand=scrollbar.set)
        # scrollbar.config(command = listbox.yview)

        


    

    



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







login_frame.mainloop()
