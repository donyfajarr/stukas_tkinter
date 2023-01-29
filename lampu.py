from tkinter import *
from tkinter import ttk

dict = {
    "teras" : 60,
    "ruang tamu" : 200,
    "ruang makan" : 200,
    "ruang kerja" : 200,
    "kamar tidur" : 200,
    "kamar mandi" : 250,
    "dapur": 250,
    "garasi": 60
} 
jenisjenis = ["Teras", "Ruang Tamu", "Ruang Makan", "Ruang Kerja", "Kamar Tidur", "Kamar Mandi", "Dapur", "Garasi"]
product = ["Lampu LED 5 Watt 300 Lumen","Lampu LED 8 Watt 480 Lumen","Lampu LED 12 Watt 660 Lumen","Lampu LED 15 Watt 900 Lumen","Lampu LED 20 Watt 1230 Lumen","Lampu LED 23 Watt 1450 Lumen"]
nilailumen = [300,480,660,900,1230,1450]

userpass = {'admin' : '123'}

def login():
    window = Toplevel()
    window.geometry('300x300')
    login_frame = Frame(window)
    login_frame.pack(padx=25, pady=25)
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

    
    def login1():
        username = inputusername.get()
        password = inputpassword.get()

        if username in userpass and password == userpass[username]:
            window.destroy()
            
            tes = Tk()
            tes.title("Admin Dashboard")
            tis = Frame(tes)
            tis.pack()
            list = LabelFrame(tis, padx=50, pady=50)
            list.grid(row=0, column=0, padx=20, pady=5)

            tampil = Label(list)
            tampil.grid(row=3, column =0)
            listprod = Label(list, text='List Product:')
            listprod.grid(row=0, column=0)
            listprod = ttk.Combobox(list, values= product)
            listprod.grid(row=0, column =1)
            def delete():
                t = listprod.get()
                ba = product.index(t)
                product.pop(ba)
                nilailumen.pop(ba)
                print(product)
                print(besarlumen)
                tes.destroy()
                window.destroy()
            buttondel = Button(list, text="Delete", command=lambda: [delete()], padx=20, pady=2.5)
            buttondel.grid(row=0, column=2)


            namaentry = Label(list, text='Nama Product:')
            namaentry.grid(row=1, column=0)
            entryprod = Entry(list)
            entryprod.grid(row=1,column=1)

            labellumen = Label(list, text='Besar Lumen:')
            labellumen.grid(row=2, column=0)
            besarlumen = Entry(list)
            besarlumen.grid(row=2,column=1)

            #dropdown product
            #pilih product pencet delete
            #ada entry untuk tambah product
            def tambah():
                prodkey = entryprod.get()
                prodvalue = besarlumen.get()
                product.append(prodkey)
                nilailumen.append(prodvalue)
                print(product)
                print(nilailumen)
                tes.destroy()
                window.destroy()
            buttonadmin = Button(list, text="Tambah", command= lambda: [tambah()], padx=20, pady=2.5)
            buttonadmin.grid(row=1, column=2)
        else:
            pass



def hitung ():
    window = Toplevel()
    window.geometry('500x200')
    frame1 = Frame(window)
    frame1.pack(padx=25, pady=25)
    
    print(jenisruangan)
    t = jenisruangan.get()
    f = t.lower()
    p = int(inputpanjang.get())
    l = int(inputlebar.get())
    tl = int(inputtitik.get())
    if jenisruangan.get() in jenisjenis:
        print(t)
        e = dict[f]
        print(e)
        llf = 0.7
        cu = 0.5
        lumen = round((e*p*l)/(tl*llf*cu*1))
        print(lumen)
        

        print(lumen)
        res_val = min(nilailumen, key=lambda x:abs(x-lumen))
        bagi = round(lumen/res_val)


        t = nilailumen.index(min(nilailumen, key=lambda x:abs(x-lumen)))
        res_key = product[t]




        print("Anda membutuhkan",bagi,"product", res_key, sep=', ')
        
        label1 = Label(frame1, text='Besar nilai lumen rekomendasi anda sebesar',)
        label1.grid(row=0, column=0)
        showhasil = Label(frame1, text=lumen)
        showhasil.grid(row = 0, column=1)
        
        
        label2 = Label(frame1, text="Produk yang direkomendasikan ialah")
        label2.grid(row=1, column=0)
        label3 = Label(frame1, text=bagi)
        label3.grid(row=1, column=1)
        # label4 = Label(frame1, text="buah, produk")
        # label4.grid(row=2, column=1)
        label5 = Label(frame1, text=res_key )
        label5.grid(row=1, column=2)
        
        def destroy():
            window.destroy()
            inputlebar.delete(0,END)
            inputpanjang.delete(0,END)
            inputtitik.delete(0,END)
            jenisruangan.delete(0,END)
        button2 = Button(frame1, text="Hitung Ulang", command=lambda: [destroy()])
        button2.grid(row=3, column=0, columnspan=4)
    else:
        pass

main_window = Tk()
main_window.title('Perhitungan Lampu')


frame = Frame(main_window)
frame.pack()

frameadmin = LabelFrame(frame, padx=25, pady=25)
frameadmin.grid(row=1, column=0, padx=20, pady=5)


frameruangan = LabelFrame(frame, padx=25, pady=25)
frameruangan.grid(row=0, column=0, padx=20, pady=5)

#PACK
labeljenis = Label(frameruangan, text='Jenis Ruangan:')
labeljenis.grid(row=0, column=0)

jenisruangan = ttk.Combobox(frameruangan, values= jenisjenis, text="Jenis Ruangan :")
jenisruangan.grid(row=0, column =1)

labelpanjang = Label(frameruangan, text="Panjang Ruangan (m): ")
labelpanjang.grid(row=1, column=0)

inputpanjang = Entry(frameruangan)
inputpanjang.grid(row=1, column=1, pady=10)

labellebar = Label(frameruangan, text="Lebar Ruangan (m):")
labellebar.grid(row=2, column=0)

inputlebar = Entry(frameruangan)
inputlebar.grid(row=2, column=1, pady=10)



jumlahtitik = Label(frameruangan, text="Titik Lampu : ")
jumlahtitik.grid(row=3, column=0)

inputtitik = Entry(frameruangan)
inputtitik.grid(row=3, column=1, pady=10)

buttonhitung = Button(frameadmin, text="Hitung", command= lambda: [hitung()], padx=20, pady=2.5)
buttonhitung.grid(row=0, column=0)

buttonadmin = Button(frameadmin, text="Admin", command= lambda: [login()], padx=20, pady=2.5)
buttonadmin.grid(row=2, column=0)
# NEW FRAME



main_window.mainloop()