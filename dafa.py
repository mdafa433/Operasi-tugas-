from datetime import datetime


def Penjualan():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("""
    ==============================

    Ananda Coffe
    List Menu Minuman Kopi

    ==============================
    A. ES Kopi Susu : Rp 11.000
    B. ES Kopi Coklat : Rp 12.000
    C. ES Kopi Hitam : Rp 11.000
    D. Ice Americano : Rp 14.000
    ==============================
    """)
    pesan = str(input("masukkan list abjad menu kopi ="))
    jumlahpesan = int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama = "ES Kopi Susu"
        harga = (11000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga = int(harga+ppn)
    elif pesan == "b":
        listnama = "ES Kopi Coklat"
        harga = (12000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga = int(harga+ppn)
    elif pesan == "c":
        listnama = "ES Kopi Hitam"
        harga = int(11000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    elif pesan == "d":
        listnama = "ES Americano"
        harga = int(14000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan = input(
            "menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")

    print("--------------------------")
    print("Ananda Coffe")
    print(dt_string)
    print("--------------------------")
    print("Menu :", listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    tanya()


def main_menu():
    print('=' * 10, 'MAIN MENU APLIKASI PENJUALAN', '=' * 10)
    print('selamat datang di aplikasi PENJUALAN')
    print('=' * 20, 'masukan input aplikasi', '=' * 20)
    print('1. Program Hitung Penjualan')
    print('2. exit program')

    pilihan = input('pilih menu: ')

    if pilihan == '1':
        Penjualan()
    elif pilihan == '2':
        print('program exit')
        exit()


def get_login():
    print('=' * 20)
    print('halaman login Penjualan')
    username = input('masukan username anda: ')
    password = input('masukan password: ')

    if username == 'dafa' and password == '123':
        print('login berhasil...\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        get_login()


def tanya():
    tanya = input('kembali ke menu utama..? (y/n) : ')
    if tanya == 'y' or 'Y':
        main_menu()
    elif tanya == 'n':
        exit()
    else:
        print('input salah')
        print('masukan input dengan benar')


if __name__ == '__main__':
    get_login()
