import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning

#Window Login
windowlogin = tk.Tk()
windowlogin.title('LOGIN')
windowlogin.configure(bg='red')
windowlogin.geometry("500x500")

#FRAME Login
login_frame = ttk.Frame(windowlogin)
login_frame.pack(padx=10, fill='x', expand=True)

#KOMPONEN
#0. Dashboard Login
dashboardlogin = ttk.Label(
    login_frame,
    text="SILAHKAN LOGIN",
    font=('Algerian', 15, 'bold')
)
dashboardlogin.pack()

#1. username
username = ttk.Label(login_frame, text='Username')
username.pack(padx=10, fill='x', expand=True)

## masukkan username
inputusername = ttk.Entry(login_frame)
inputusername.pack(padx=10,pady=10, fill='x', expand=True)

#2. Password
password = ttk.Label(login_frame, text='Password')
password.pack(padx=10, fill='x', expand=True)

## masukkan Password
inputpassword = ttk.Entry(login_frame, show='*')
inputpassword.pack(padx=10,pady=10, fill='x', expand=True)



#LOGIKA LOGIN
userpass = {'admin' : '123'}
def login():
    username = inputusername.get()
    password = inputpassword.get()

    if username in userpass and password == userpass[username]:
        windowlogin.destroy()
        window = tk.Tk()
        window.title('Kalkulator NIOSH LE')
        window.configure(bg='pink')
        window.geometry("750x750")

        # LOGIKA
        LC = 23
        def niosh():
            beratobjek = int(inputberatobjek.get())

            H = int(inputhm.get())
            HM = 25 / H
            V = int(inputvm.get())
            VV = abs(V-75)
            VM = 1 - (0.003*VV)
            D = int(inputdm.get())
            DM = 0.82 + (4.5/D)
            A = int(inputam.get())
            if A > 135:
                A = 0
            else:
                A=A
            AM = 1 - (0.0032*A)
            LamaKerja = int(inputlamakerja.get())
            angkatmenit = int(inputangkatmenit.get())
            if LamaKerja <= 60:
                if angkatmenit <= 0.2:
                    FM = 1
                elif angkatmenit < 0.5:
                    FM = 0.97
                elif angkatmenit == 1:
                    FM = 0.94
                elif angkatmenit == 2:
                    FM = 0.91
                elif angkatmenit == 3:
                    FM = 0.88
                elif angkatmenit == 4:
                    FM = 0.84
                elif angkatmenit == 5:
                    FM = 0.80
                elif angkatmenit == 6:
                    FM = 0.75
                elif angkatmenit == 7:
                    FM = 0.70
                elif angkatmenit == 8:
                    FM = 0.60
                elif  angkatmenit == 9:
                    FM = 0.52
                elif angkatmenit == 10:
                    FM = 0.45
                elif angkatmenit == 11:
                    FM = 0.41
                elif angkatmenit == 12:
                    FM = 0.37
                elif  angkatmenit == 13:
                    if V < 30:
                        FM = 0
                    else:
                        FM = 0.34
                elif  angkatmenit == 14:
                    if V < 30:
                        FM = 0
                    else:
                        FM = 0.31
                elif  angkatmenit == 15:
                    if V < 30:
                        FM = 0
                    else:
                        FM = 0.28
                else: 
                    FM = 0  
            #yang elif 1-2 jam 
            elif 60 < LamaKerja <= 120:
                if angkatmenit <= 0.2:
                    FM = 0.95
                elif angkatmenit < 0.5:
                    FM = 0.92
                elif angkatmenit == 1:
                    FM = 0.88
                elif angkatmenit == 2:
                    FM = 0.84
                elif angkatmenit == 3:
                    FM = 0.79
                elif angkatmenit == 4:
                    FM = 0.72
                elif angkatmenit == 5:
                    FM = 0.60
                elif angkatmenit == 6:
                    FM = 0.50
                elif angkatmenit == 7:
                    FM = 0.42
                elif angkatmenit == 8:
                    FM = 0.35
                elif  angkatmenit == 9:
                    FM = 0.30
                elif angkatmenit == 10:
                    FM = 0.26
                elif angkatmenit ==11:
                    if V<30:
                        FM=0
                    else:
                        FM=0.23
                elif angkatmenit ==12:
                    if V<30:
                        FM=0
                    else:
                        FM=0.21
                elif angkatmenit >12:
                    FM = 0.00
            #yang elif >2 jam
            elif  LamaKerja > 120:
                if angkatmenit <= 0.2:
                    FM = 0.85
                elif angkatmenit < 0.5:
                    FM = 0.81
                elif angkatmenit == 1:
                    FM = 0.75
                elif angkatmenit == 2:
                    FM = 0.65
                elif angkatmenit == 3:
                    FM = 0.55
                elif angkatmenit == 4:
                    FM = 0.45
                elif angkatmenit == 5:
                    FM = 0.35
                elif angkatmenit == 6:
                    FM = 0.27
                elif angkatmenit == 7:
                    FM = 0.22
                elif angkatmenit == 8:
                    FM = 0.18
                elif angkatmenit == 9:
                    if V<30:
                        FM=0
                    else:
                        FM=0.15
                elif angkatmenit == 10:
                    if V<30:
                        FM=0
                    else:
                        FM=0.13
                elif angkatmenit >10:
                    FM = 0.00        
            

            C = inputcm.get().lower()
            while True:
                if C == 'good':
                    CM = 1
                    False
                    break
                elif C == 'fair':
                    if V < 30:
                        CM = 0.95
                        False
                    else:
                        CM = 1
                        False
                    break
                elif C == 'poor':
                    CM = 0.90
                    break
                else:
                    True
                    break


            tes = round(LC*HM*VM*DM*AM*CM*FM,3)
            LI = round(beratobjek / tes,3)

            #Simsalabim Muncul windowhasil ----
            window.destroy()
            windowhasil = tk.Tk()

            #FRAME Login
            hasil_frame = ttk.Frame(windowhasil)
            hasil_frame.pack(padx=10, fill='x', expand=True)

            dashboardhasil = tk.Label(
                hasil_frame, text= "Hasil Perhitungan", font=('Algerian', 15, 'bold')
            )

            dashboardhasil.pack(padx=10, fill='x', expand=True)
            hasil = tk.Label(
                hasil_frame,
                text="Nilai RWL anda adalah " + str(tes),
                font= ('Times New Roman', 13)
            )
            hasil.pack()

            hasilli = tk.Label(
                hasil_frame,
                text="Nilai LI adalah sebesar = " + str(LI),
                font= ('Times New Roman', 13))
            hasilli.pack()

            if LI>=1:
                hasilprint = tk.Label(
                    hasil_frame,
                    text="Pekerjaan berisiko menimbulkan cidera tulang belakang",
                    font= ('Times New Roman', 13, 'bold')
                )
                hasilprint.pack()
            else:
                hasilprint1 = tk.Label(
                    hasil_frame,
                    text = "Pekerjaan tidak berisiko menimbulkan cidera tulang belakang",
                    font= ('Times New Roman', 13, 'bold')
                )
                hasilprint1.pack()
                    # ---- Formatting Windowhasil
            windowhasil.title('Hasil Perhitungan')
            windowhasil.configure(bg='yellow')
            windowhasil.geometry('500x500')

            # #FRAME Login
            # hasil_frame = ttk.Frame(windowhasil)
            # hasil_frame.pack(padx=10, fill='x', expand=True)

            # back = tk.Button(
            #     windowhasil,
            #     text="Hitung kembali", command=login)
            # back.pack()
            # inputberatobjek.forget()
            # inputhm.forget()
            # inputvm.forget()
            # inputdm.forget()
            # inputam.forget()
            # inputlamakerja.forget()    
            # inputangkatmenit.forget()
            # inputcm.forget()

            # inputberatobjek.delete(0,tk.END)
            # inputhm.delete(0,tk.END)
            # inputvm.delete(0,tk.END)
            # inputdm.delete(0,tk.END)
            # inputam.delete(0,tk.END)
            # inputlamakerja.delete(0,tk.END)    
            # inputangkatmenit.delete(0,tk.END)
            # inputcm.delete(0,tk.END)



            # quit = tk.Button(
            #     windowhasil,
            #     text="Keluar program"
            # )
            # quit.pack()
            

            windowhasil.mainloop()
    else: 
        inputusername.delete(0,tk.END)
        inputpassword.delete(0,tk.END)        
        showwarning("Warning!", message= "Username Atau Password salah")

    


    #FRAME
    anjay_frame = ttk.Frame(window)
    anjay_frame.pack(padx=10, fill='x', expand=True)

    #KOMPONEN
    #0. Dashboard
    dashboard = ttk.Label(
        anjay_frame,
        text="MASUKKAN DATA",
        font=('Algerian', 15, 'bold')
    )
    dashboard.pack()
    #(0<x<1). Berat Objek

    beratobjek1 = ttk.Label(anjay_frame, text='Berat Objek')
    beratobjek1.pack(padx=10, fill='x', expand=True)

    ## masukkan Berat Objek
    inputberatobjek = ttk.Entry(anjay_frame)
    inputberatobjek.pack(padx=10,pady=10, fill='x', expand=True)


    #1. HM
    hm = ttk.Label(anjay_frame, text='Horizontal (H)')
    hm.pack(padx=10, fill='x', expand=True)

    ## masukkan H
    inputhm = ttk.Entry(anjay_frame)
    inputhm.pack(padx=10,pady=10, fill='x', expand=True)

    #2. VM
    vm = ttk.Label(anjay_frame, text='Vertical (V)')
    vm.pack(padx=10, fill='x', expand=True)

    ## masukkan V
    inputvm = ttk.Entry(anjay_frame)
    inputvm.pack(padx=10,pady=10, fill='x', expand=True)

    #3. DM
    dm = ttk.Label(anjay_frame, text='Distance (D)')
    dm.pack(padx=10, fill='x', expand=True)

    ## masukkan D
    inputdm = ttk.Entry(anjay_frame)
    inputdm.pack(padx=10,pady=10, fill='x', expand=True)

    #4. AM
    am = ttk.Label(anjay_frame, text='Asymmetric (A)')
    am.pack(padx=10, fill='x', expand=True)

    ## masukkan V
    inputam = ttk.Entry(anjay_frame)
    inputam.pack(padx=10,pady=10, fill='x', expand=True)

    #5. Lama Kerja
    lamakerja = ttk.Label(anjay_frame, text='Lama Kerja (Menit)')
    lamakerja.pack(padx=10, fill='x', expand=True)

    ## masukkan Lama Kerja
    inputlamakerja = ttk.Entry(anjay_frame)
    inputlamakerja.pack(padx=10,pady=10, fill='x', expand=True)

    #6. Angkat/menit
    angkatmenit = ttk.Label(anjay_frame, text='Jumlah Angkat/Menit')
    angkatmenit.pack(padx=10, fill='x', expand=True)

    ## masukkan V
    inputangkatmenit = ttk.Entry(anjay_frame)
    inputangkatmenit.pack(padx=10,pady=10, fill='x', expand=True)

    #7. CM
    cm = ttk.Label(anjay_frame, text='Kualitas Coupling (Poor, Fair, Good)')
    cm.pack(padx=10, fill='x', expand=True)

    ## masukkan C
    inputcm = ttk.Entry(anjay_frame)
    inputcm.pack(padx=10,pady=10, fill='x', expand=True)

    #8. Button Submit
    button1 = ttk.Button(anjay_frame, text='Submit', command=niosh)
    button1.pack()
    window.mainloop()
    
#3. Button Login
button1 = ttk.Button(login_frame, text='Login',  command= login)
button1.pack()



windowlogin.mainloop()