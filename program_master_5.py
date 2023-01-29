from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# LIST
userpass = {'admin' : '123'}
barangjualan = ['Sabun Cair', 'Sabun Cuci', 'Sampo', 'Sikat Gigi', 'Minuman Dingin', 'Makanan Ringan', 'Mi Instan', 'Air Mineral']
listharga = [200000, 120000, 190000, 180000, 210000, 170000, 110000, 220000]
listmetode = ['CASH', 'DEBIT', 'E-WALLET']
listbarangdibeli = []
listharganow = []
listtotalharga = []
listkuantitas = []
listlabel = []


# FUNCTION
coba = 0
def login():
    global coba
    username1 = inputusername.get()
    password1 = inputpassword.get()
    
    if username1 in userpass and password1 == userpass[username1]:
        window_login.destroy()
        main_window.deiconify()
    elif coba == 3:
        showwarning(message='Terminated')
        
        main_window.destroy()
        window_login.destroy
    else:
        showerror(message='Username / Password salah')
        inputusername.delete(0,END)
        inputpassword.delete(0,END)
    coba += 1


def tambah():
    if not inputbarang.get():
        showerror(title='Error', message='Silahkan Masukkan Barang', )
    elif not inputjumlah.get():
        showerror(title='Error', message='Silahkan Masukkan Jumlah Barang yang akan dibeli', )

    else:
        if inputbarang.get() in listbarangdibeli:
            i = 0
            while i < len(listbarangdibeli):
                if listbarangdibeli[i] == inputbarang.get():
                    x = i
                    listtotalharga[x] += (listharga[x]*int(inputjumlah.get()))
                    listkuantitas[x] += int(inputjumlah.get())
                i += 1
        else:            
            inputjumlah.get()
            listbarangdibeli.append(inputbarang.get())
            listkuantitas.append(int(inputjumlah.get()))
            i = 0
            while i < len(barangjualan):
                if barangjualan[i] == inputbarang.get():
                    x = i 
                    listharganow.append(listharga[x])
                    listtotalharga.append(listharga[x]*int(inputjumlah.get()))
                i +=1
        inputbarang.delete(0,END)
        inputjumlah.delete(0,END)

    
    print(listbarangdibeli)
    print(listtotalharga)
    print(listkuantitas)

# Menampilkan Keranjang

value = 1
def keranjang():
    global value, no1, barang, quantity, harga, Total
    value -= 1

    if value == 0:
        i= 0
        while i < len(listbarangdibeli):

            no1 = Label(framerincian, text= 1 + i)
            no1.grid(row=i+1, column=0,)

            barang = Label(framerincian, text= listbarangdibeli[i])
            barang.grid(row=i+1, column=1, )

            quantity = Label(framerincian, text= listkuantitas[i])
            quantity.grid(row=i+1, column=2, )

            harga = Label(framerincian, text= '{:,.2f}'.format(listharganow[i]))
            harga.grid(row=i+1, column=3, )

            Total = Label(framerincian, text='{:,.2f}'.format(listtotalharga[i]))
            Total.grid(row=i+1, column=4, )

            listlabel.append(no1)
            listlabel.append(barang)
            listlabel.append(quantity)
            listlabel.append(harga)
            listlabel.append(Total)

            i += 1
    
        value = 1
    else:
        pass  

#Pembayaran
           
def pembayaran():
    global nilaipembelian, nilaidiskon, nilaitotal, nilaibayar, nilaikembali
    if not inputmetodebayar.get():
        showerror(title='Error', message='Silahkan Pilih Metode Bayar', )
    else:

        if inputmetodebayar.get() != 'CASH':

            if inputmetodebayar.get() == 'DEBIT':
                totalbayar = int(sum(listtotalharga)*0.95)
                kembalian = 0
                nominalbayar = totalbayar

            elif inputmetodebayar.get() == 'E-WALLET':
                totalbayar = int(sum(listtotalharga)*0.97)
                kembalian = 0
                nominalbayar = totalbayar
            else:
                pass

            if sum(listtotalharga) >= 500000:
                totalbayar -= 20000
            
            nilaipembelian = Label(framenota, text=': Rp. {:,.2f} '.format(sum(listtotalharga)))
            nilaipembelian.grid(row=0,column=1)
            
            totaldiskon = sum(listtotalharga) - totalbayar
            nilaidiskon = Label(framenota, text=': Rp. {:,.2f} '.format(totaldiskon))
            nilaidiskon.grid(row=1,column=1, sticky='ew')

            nilaitotal = Label(framenota, text=': Rp. {:,.2f}'.format(totalbayar))
            nilaitotal.grid(row=2,column=1, sticky='ew')

            nilaibayar = Label(framenota, text=': Rp. {:,.2f}'.format(nominalbayar))
            nilaibayar.grid(row=3,column=1, sticky='ew')

            nilaikembali = Label(framenota, text=': Rp. {:,.2f}'.format(kembalian))
            nilaikembali.grid(row=4,column=1, sticky='ew')
        
        elif inputmetodebayar.get() == 'CASH':
            def bayarcash():
                global nilaipembelian, nilaidiskon, nilaitotal, nilaibayar, nilaikembali
                totaldiskon = sum(listtotalharga) - totalbayar
                nominalbayar = inputbayar2.get()
                kembalian = int(inputbayar2.get()) - totalbayar

                nilaipembelian = Label(framenota, text=': Rp. {:,.2f} '.format(sum(listtotalharga)))
                nilaipembelian.grid(row=0,column=1)

                
                nilaidiskon = Label(framenota, text=': Rp. {} '.format(totaldiskon))
                nilaidiskon.grid(row=1,column=1, sticky='ew')

                nilaitotal = Label(framenota, text=': Rp. {:,.2f}'.format(totalbayar))
                nilaitotal.grid(row=2,column=1, sticky='ew')

                nilaibayar = Label(framenota, text=': Rp. {:,.2f}'.format(int(nominalbayar)))
                nilaibayar.grid(row=3,column=1, sticky='ew')

                nilaikembali = Label(framenota, text=': Rp. {:,.2f}'.format(kembalian))
                nilaikembali.grid(row=4,column=1, sticky='ew')
                

            def destroy():
                window.destroy()

            window = Toplevel()
            window.geometry('300x300')

            frame1 = Frame(window, )
            frame1.pack(padx=25, pady=25)

            totalbayar = sum(listtotalharga)
            
            totalakhir2 = Label(frame1, text='TOTAL')
            totalakhir2.grid(row=0, column=0)

            showtotalakhir2 = Label(frame1, text= ': {:,.2f}'.format(totalbayar))
            showtotalakhir2.grid(row=0, column=1)

            bayar2 = Label(frame1, text='BAYAR')
            bayar2.grid(row=1, column=0)

            inputbayar2 = Spinbox(frame1, from_=0, to=10**10)
            inputbayar2.grid(row=1, column=1)

            buttonbayar2 = Button(frame1, text='BAYAR', bg='#7ED957', command=lambda: [bayarcash(), destroy()])
            buttonbayar2.grid(row=2, column=0, columnspan=2)

        else:
            pass

        if sum(listtotalharga) >= 500000:
            totalbayar -= 20000
    
   

    buttoninput['state'] = DISABLED
    buttonpay['state'] = DISABLED

def selesai():

    for i in listlabel:
        i.destroy()

    listbarangdibeli.clear()
    listtotalharga.clear()
    listharganow.clear()
    listkuantitas.clear()

    nilaipembelian.destroy()
    nilaidiskon.destroy()
    nilaitotal.destroy() 
    nilaibayar.destroy() 
    nilaikembali.destroy()

    inputmetodebayar.delete(0,END)

    buttoninput['state'] = ACTIVE
    buttonpay['state'] = ACTIVE

    inputbarang.current(0)
    inputmetodebayar.current(0)
    

# WINDOW
main_window = Tk()
main_window.title('Kasir LOSIK GROCERY')
# main_window.iconbitmap("D:\Serba-serbi Kuliah\Lain-lain\Desain tanpa judul.ico")
main_window.withdraw()


# FRAME
frame = Frame(main_window)
frame.pack()

framebarang = LabelFrame(frame,  padx=25, pady=25)
framebarang.grid(row=0, column=0, padx=20, pady=5)

framerincian = LabelFrame(frame)
framerincian.grid(row=1, column=0,sticky='news', padx=20, pady=5)

framebayar = LabelFrame(frame)
framebayar.grid(row=2, column=0 ,sticky='news', padx=20, pady=5)

framenota = LabelFrame(frame)
framenota.grid(row=3, column=0,sticky='news', padx=20, pady=5)

frmaeselesai = LabelFrame(frame)
frmaeselesai.grid(row=4, column=0,sticky='news', padx=20, pady=5)

# WIDGET
namabarang = Label(framebarang, text='Nama Barang : ')
namabarang.grid(row=0, column=0)

inputbarang = ttk.Combobox(framebarang, values= barangjualan)
inputbarang.current(0)
inputbarang.grid(row=0,column=1, )

jumlahbarang = Label(framebarang, text='Jumlah Barang : ')
jumlahbarang.grid(row=1, column=0)

inputjumlah = Spinbox(framebarang, from_=1, to=100)
inputjumlah.grid(row=1, column=1, pady=10)

buttoninput = Button(framebarang, text='Input',command= lambda: [tambah(), keranjang()], bg='#7ED957',  padx=20, pady=2.5, )
buttoninput.grid(row=0, column=2, rowspan=2,  padx=25)

no = Label(framerincian, text='No')
no.grid(row=0, column=0, )

barang = Label(framerincian, text='Nama Barang')
barang.grid(row=0, column=1, )

quantity = Label(framerincian, text='Quantity')
quantity.grid(row=0, column=2, )

harga = Label(framerincian, text='Harga')
harga.grid(row=0, column=3, )

Total = Label(framerincian, text='Total')
Total.grid(row=0, column=4, )

for i in framerincian.winfo_children():
    i.grid_configure(padx= 15, pady=2)

# btn1 = Button(framebayar, text= 'btn1' , padx=10, bg='red')
# btn1.grid(row=0, column=0, rowspan=2)

metodebayar = Label(framebayar, text='Metode Pembayaran : ', font=("Arial", 10))
metodebayar.grid(row=0, column=1, )

inputmetodebayar = ttk.Combobox(framebayar, values= listmetode)
inputmetodebayar.current(0)
inputmetodebayar.grid(row=0,column=2)

buttonpay = Button(framebayar, text= 'Bayar', padx=10, bg='#7ED957', command= lambda: [pembayaran(),])
buttonpay.grid(row=1, column=2)

for i in framebayar.winfo_children():
    i.grid_configure(padx= 10, pady=2)

pembelian = Label(framenota, text='PEMBELIAN ')
pembelian.grid(row=0,column=0, sticky='ew')

diskon = Label(framenota, text='DISKON ')
diskon.grid(row=1,column=0, sticky='ew')

totalakhir = Label(framenota, text='TOTAL AKHIR ')
totalakhir.grid(row=2,column=0, sticky='ew')

bayar = Label(framenota, text='BAYAR ')
bayar.grid(row=3,column=0, sticky='ew')

kembali = Label(framenota, text='KEMBALIAN ')
kembali.grid(row=4,column=0, sticky='ew')

for i in framenota.winfo_children():
    i.grid_configure(padx= 20, pady=2)

frmaeselesai.grid_columnconfigure(1,weight=1)
buttonselesai = Button(frmaeselesai, text= 'SELESAI', padx=10, bg='#6297FF',command=selesai )
buttonselesai.grid(row=0,column=0, sticky='news', columnspan=4)


#Login
window_login= Toplevel()

framelogin = Frame(window_login)
framelogin.pack(fill='x')

username = Label(framelogin, text='Username')
username.grid(row=0,column=0)

inputusername = Entry(framelogin)
inputusername.grid(row=0, column=1)

password = Label(framelogin, text='Password')
password.grid(row=1,column=0)

inputpassword = Entry(framelogin, show='*')
inputpassword.grid(row=1,column=1)

buttonlogin= Button(framelogin, text='Login', command= lambda: login())
buttonlogin.grid(row=2,column=1,columnspan=2, sticky='we',)


# END OF WINDOW
main_window.mainloop()

