beli = "y" or "Y"
while beli == "y" or "Y":
 print(" ========================================")
 print(" Selamat Datang di Pasar Cibinong")
 


 print("=========================================")
 brt=int(input("berat telur=")) 
 hrg=int(input("harga telur="))
 ongkos=int(input("transport="))
 uang =int(input("uang ibu="))
 sisauang=uang-ongkos*2-hrg*brt
 print("Sisa uang ibu adalah Rp %s " % (sisauang))
 print("==============================================")
 beli=input("Mau beli lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")