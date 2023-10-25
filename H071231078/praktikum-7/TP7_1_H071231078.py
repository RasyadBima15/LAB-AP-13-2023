import os
import random

#Head
folder_name = "invoices"

def char_fml(a):
    if len(a) > 2:
        if len(a) % 2 == 0:   
            b = int((len(a))/2)
            c = a[0],a[b-1],a[b],a[-1]
            return "".join(c)
        else:
            b = int(1+(len(a))/2)
            c = a[0],a[b-1],a[-1]
            return "".join(c)
    else:
        return "error"

def random_angka(min, max):
  angka = random.randint(min, max)
  if angka < 10:
    angka = "0" + str(angka)
  return angka

def history_head():
    global path_route_1
    path_route_1 = os.path.join(folder_name,"trx_history" + ".txt")
    history = open(path_route_1,"w")
    history.write(73*"=" + "\n")
    history.write('|' +27*" " + "RIWAYAT TRANSAKSI" +27*" "+"|\n")
    history.write(73*"=" + "\n")
    history.write("|"+8*" "+"Waktu"+8*" "+"|"+4*" "+"ID Transaksi"+4*" "+"|"+4*" "+"Nominal Transaksi"+7*" "+"|\n")
    history.write(73*"=" + "\n")
    
def option_head():
    global daftar_harga_barang,daftar_jumlah_barang,daftar_nama_barang,tanggal,jam,mnt_dtk
    daftar_nama_barang.clear()
    daftar_harga_barang.clear()
    daftar_jumlah_barang.clear()
    total_belanja_invoice.clear()
    tanggal = str((random_angka(1, 31)))
    jam = str((random_angka(1, 23)))
    mnt_dtk = str((random_angka(1, 59)))

def option_body():
    global id_name,path_route,nama_produk,harga_produk,jumlah_produk
    waktu_transaksi = jam + mnt_dtk
    rn = str(random.randint(100,999))
    id_name = (f"{char_fml(nama_kasir_kapital)}"+"2310"+tanggal + waktu_transaksi+rn)
    path_route    = os.path.join(folder_name, id_name + ".txt")
    nama_produk   = input("masukkan nama produk     : ")
    harga_produk  = input("masukkan harga produk    : ")
    jumlah_produk = input("masukkan jumlah produk   : ")
    daftar_nama_barang.append(nama_produk)
    daftar_harga_barang.append(harga_produk)
    daftar_jumlah_barang.append(jumlah_produk)

def invoices_write():   
    global invoice_file,total_harga,total_belanja,total_belanja_invoice,c,d
    invoice_file = open(path_route, "a")
    invoice_file.write("\n"+ 30*" " + f"TOKO {nama_kasir}\n\n")
    invoice_file.write(73*"="+"\n")
    invoice_file.write(f"nama kasir      : {nama_kasir}\n")
    invoice_file.write(f"waktu transaksi : {tanggal}/10/23  {jam}:{mnt_dtk}\n")
    invoice_file.write(73*"="+"\n\n")
    invoice_file.write(29*" " + f"DAFTAR PRODUK\n\n")
    invoice_file.write(73*"="+"\n")
    invoice_file.write("|"+8*" "+"nama"+8*" "+"|"+7*" "+"harga"+7*" "+"|"+1*" "+"jumlah"+1*" "+"|"+8*" "+"total"+8*" "+"|\n")
    invoice_file.write(73*"="+"\n")
    for x, y, z in zip(daftar_nama_barang, daftar_harga_barang, daftar_jumlah_barang):
        total_harga = int(z) * int(y)
        total_belanja = []
        total_belanja.clear()
        total_belanja.append(total_harga)
        total_belanja_invoice.append(total_harga)
        a = (f"{(int(y)):,}")
        b = (f"{(int(total_harga)):,}")
        e = [sum(total_belanja_invoice)]
        d = []
        c = [f"{x:,}". format(e).replace(",", ".") for x in e]
        for i in c:
            d.append(i)
        if len(x) > 16:
            invoice_file.write(f"| {x[:16]+'...'}{' '*(19-len(x))}| {' '*(14-len(a)+2)}Rp{a}| {' '*3}{z}{' '*(4-len(z))}| {' '*(18 - len(str(b)))}Rp{b}|\n". format(y).replace(",", "."))
        else:
            invoice_file.write(f"| {x}{' '*(19-len(x))}| {' '*(14-len(a)+2)}Rp{a}| {' '*3}{z}{' '*(4-len(z))}| {' '*(18 - len(str(b)))}Rp{b}|\n". format(y).replace(",", "."))
    invoice_file.write(73*"="+"\n")
    invoice_file.write(f"|{8*' '} TOTAL {33*' '} | {' '*(18-len(str((d[0]))))}Rp{(d[0])}|\n")
    invoice_file.write(73*"="+"\n\n")
    invoice_file.write(73*"="+"\n")
    invoice_file.write(23*" " + "TERIMAKASIH TELAH BELANJA\n")
    invoice_file.write(73*"="+"\n")

def history_body():
    global history,Waktu
    history = open(path_route_1,"a")
    Waktu = str(f"{tanggal}/10/23  {jam}:{mnt_dtk}")
    history.write(f"| {Waktu}{' '*(20-len(Waktu))}|  {id_name}{' '*(18-len(id_name))}| {' '*(25-len(str(d[0])))}Rp{d[0]}|\n")
    history.write(73*"="+"\n")

print(50*"=")
print(18*" " + "SELAMAT DATANG")
print(50*"=")
nama_kasir = input("masukkan nama kasir : ")
nama_kasir_kapital = nama_kasir.upper()


#list_head
daftar_nama_barang = []
daftar_harga_barang = []
daftar_jumlah_barang = []
total_belanja_invoice = []

#Body
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    history_head()
    #main loop 1
    while True: 
        print(50*"=")
        print("PILIH OPSI : \n1. Transaksi baru\n2. cari transaksi\n3. keluar")
        print(50*"=")
        opsi = input("masukkan pilihan opsi : ")
        print(50*"=")

        if opsi == "1":
            option_head()
            while True:
                option_body()
                closer = input("Tambah produk? (y/t) : ")
                if closer == "t":
                    invoices_write()
                    history_body()
                    break
            
        elif opsi == "2":
            cari_trnsksi = input("masukkan ID : ")
            files = os.listdir("invoices")
            for file in files:
                if cari_trnsksi in file:
                    n = open("invoices"+"\\"+cari_trnsksi+".txt")
                    print(n.read())
        elif opsi == "3":
            break

else:
    if os.path.exists(folder_name):
        history_head()
        #main loop 2
        while True: 
            print(50*"=")
            print("PILIH OPSI : \n1. Transaksi baru\n2. cari transaksi\n3. keluar")
            print(50*"=")
            opsi = input("masukkan pilihan opsi : ")
            print(50*"=")

            if opsi == "1":
                option_head()
                while True:
                    option_body()
                    closer = input("Tambah produk? (y/t) : ")
                    if closer == "t":
                        invoices_write()
                        history_body()
                        break
                
            elif opsi == "2":
                cari_trnsksi = input("masukkan ID : ")
                files = os.listdir("invoices")
                for file in files:
                    if cari_trnsksi in file:
                        n = open("invoices"+"\\"+cari_trnsksi+".txt")
                        print(n.read())
            elif opsi == "3":
                break

    

