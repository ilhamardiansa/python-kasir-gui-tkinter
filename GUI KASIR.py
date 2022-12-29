from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector

mydb = mysql.connector.connect( # untuk mengkonekan python ke database
  host="localhost", # nama host
  user="root", # username database
  password="", # password database
  database="pythohlears" #nama database
)
mycursor = mydb.cursor()

total = [200]

root = Tk()
#root.geometry("250x200")

page_check = 0
def daftar_barang():
    global lblframe01,page_check,entry1,listcombo

    listcombo = []

    if page_check == 0:
        pass
        listcombo.clear()
    elif page_check == 2:
        lblframe02.grid_forget()
    elif page_check == 3:
        lblframe03.grid_forget()
    elif page_check == 4:
        lblframe04.grid_forget()
    lblframe01 = LabelFrame(root)
    lblframe01.grid()

    def OptionCallBack(*args):
        global hargabrg
        option = monthchoosen.get()
        ss = option.split("-")[0]
        mycursor.execute("SELECT * FROM barang WHERE id = %s", (ss,))
        rows = mycursor.fetchall()
        for brg in rows:
            hargabrg = brg[2]

        
    mycursor.execute("SELECT * FROM barang") # kode di ambil dari user input atau masukan
    for brg in mycursor:
        listcombo.append(str(brg[0])+" - "+brg[1]+" - Rp "+brg[2])
    
    monthchoosen = ttk.Combobox(lblframe01, 
    width = 27, values=listcombo)
    monthchoosen.set("Pilih Barang")
    monthchoosen.current()
    monthchoosen.pack()
    monthchoosen.bind("<<ComboboxSelected>>", OptionCallBack)
    
    lbl1 = Label(lblframe01,text="Jumlah Barang :   ")
    lbl1.pack()
    entry1 = Entry(lblframe01, width= 40)
    entry1.pack()
    entry1.bind('<Return>') 
    lbl2 = Label(lblframe01,text="")
    lbl2.pack()
    btn = Button(lblframe01, text='Order', command=tanya)
    btn.pack()
    lbl3 = Label(lblframe01,text="")
    lbl3.pack()

def tanya():
    lblframe01.grid_forget()
    global lblframe02,page_check

    page_check = 2

    if page_check == 0:
        lblframe01.grid_forget()
    elif page_check == 2:
        pass
    elif page_check == 3:
        lblframe03.grid_forget()
    elif page_check == 4:
        lblframe04.grid_forget()
    lblframe02 = LabelFrame(root)
    lblframe02.grid()
    try:
        se = int(entry1.get())
    except ValueError:
        print("Salah")
        messagebox.showinfo("ERROR", "INPUT HARUS BERUPA ANGKA")
        return daftar_barang()
    try:
        total1 = int(hargabrg) * int(se)
    except:
        messagebox.showinfo("ERROR", "OPSI HARUS DI PILIH")
        return daftar_barang()
    print(total1)
    total.append(total1)
    sum(total)
    a = sum(total)
    lbl1 = Label(lblframe02,text=f"TOTAL BELANJA    : {a}")
    lbl1.pack()
    lbl2 = Label(lblframe02,text="INGIN TAMBAH BARANG LAGI ?")
    lbl2.pack()

    lbl4 = Label(lblframe02,text="")
    lbl4.pack()
    btn1 = Button(lblframe02, text='LANJUT', command=akhir)
    btn1.pack()
    btn2 = Button(lblframe02, text='KEMBALI', command=daftar_barang)
    btn2.pack()
    lbl3 = Label(lblframe02,text="")
    lbl3.pack()

def akhir():
    lblframe02.grid_forget()
    global lblframe03,page_check,entry2,totalakhir
    page_check = 3
    
    if page_check == 0:
        lblframe01.grid_forget()
    elif page_check == 2:
        lblframe02.grid_forget()
    elif page_check == 3:
        pass
    elif page_check == 4:
        lblframe04.grid_forget()

    lblframe03 = LabelFrame(root)
    lblframe03.grid()
    lbl1 = Label(lblframe03,text="="*30)
    lbl1.pack()
    lbl2 = Label(lblframe03,text="KASIR AA")
    lbl2.pack()
    lbl3 = Label(lblframe03,text="="*30)
    lbl3.pack()
    lbl4 = Label(lblframe03,text="")
    lbl4.pack()
    sum(total)
    a = sum(total)
    lbl5 = Label(lblframe03,text=f"SUB TOTAL    : {a}")
    lbl5.pack()
    if a > 50000:
        diskon = a * 1/100
    elif a > 70000:
        diskon = a * 3/100
    elif a > 90000:
        diskon = a * 5/100
    elif a > 100000:
        diskon = a * 8/100
    else:
        diskon = 0
    lbl6 = Label(lblframe03,text=f"POTONGAN HARGA    : {diskon}")
    lbl6.pack()
    totalakhir = a - diskon
    lbl7 = Label(lblframe03,text=f"TOTAL AKHIR    : {totalakhir}")
    lbl7.pack()
    lbl8 = Label(lblframe03,text="")
    lbl8.pack()

    lbl9 = Label(lblframe03,text="MASUKAN JUMLAH BAYAR :   ")
    lbl9.pack()
    entry2 = Entry(lblframe03, width= 40)
    entry2.pack()
    entry2.bind('<Return>') 
    lbl10 = Label(lblframe03,text="")
    lbl10.pack()
    lbl12 = Label(lblframe03,text=f"")
    lbl12.pack()
    btn2 = Button(lblframe03, text='LANJUT', command=kembalians)
    btn2.pack()
    lbl11 = Label(lblframe03,text="")
    lbl11.pack()
    
def kembalians():
    lblframe03.grid_forget()
    global lblframe04,page_check
    page_check = 4
    if page_check == 0:
        lblframe01.grid_forget()
    elif page_check == 2:
        lblframe02.grid_forget()
    elif page_check == 3:
        lblframe03.grid_forget()
    elif page_check == 4:
        pass
    lblframe04 = LabelFrame(root)
    lblframe04.grid()
    try:
        ses = int(entry2.get())
    except ValueError:
        messagebox.showinfo("ERROR", "INPUT HARUS BERUPA ANGKA")
        return akhir()
    if ses < totalakhir:
        messagebox.showinfo("INFO", "PEMBAYARAN KURANG")
        return akhir()
    else:
        kembalianss = int(ses) - int(totalakhir)
    lbl1 = Label(lblframe04,text="="*30)
    lbl1.pack()
    lbl2 = Label(lblframe04,text="KASIR AA")
    lbl2.pack()
    lbl3 = Label(lblframe04,text="="*30)
    lbl3.pack()
    lbl4 = Label(lblframe04,text="")
    lbl4.pack()
    lbl5 = Label(lblframe04,text=f"KEMBALIAN    : {kembalianss}")
    lbl5.pack()

daftar_barang()

root.mainloop()