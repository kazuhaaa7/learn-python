
# Angka = 9

# if Angka == 10:
#     print(f"yap Angkamu {Angka}")
# else:
#     print(f''' Yah sayang banget angkamu bukan {Angka}''')


# lower() berfungsi untuk mengecilkan huruf yg typenya string
# library bawaan python
import random   # << LIBRARY UNTUK BISA MENGGUNAKAN random.randit()
import time  # << LIBRARY UNTUK ADD JEDA
possition = random.randint(1, 4)
# yes = "Y"
# noo = "N"

print("mini project")
user_name = input("Masukan nama kamu: ")

goa_shape ="|_|"
empty_goa  = [goa_shape] * 4 #empty_goa original
goa_no_array = " ".join(empty_goa)
goa = empty_goa.copy() # oa original fungsion .copy() hanya untuk mengcopy lalu dirubah dgn syntax dibawah, jika tidak goa orihinal akan tercopy juga

goa[possition - 1] = "|0_0|"
goa_without_array = " ".join(goa) #Join array atau .join() adalah proses menggabungkan elemen-elemen dalam array (atau list) menjadi satu string menggunakan pemisah tertentu.

print(f''' Halo {user_name}! Coba perhatikan goa di bawah ini
{goa_no_array}''')
# variable di bawah berupa tipe string, tugasnya ubah jadi int agar sm dengan tipe varible position
# user_memilih = input("Coba tebak di dalam goa ada seekor hewan, di goa manakah dia berada? [1/ 2/ 3/ 4] ")

# cara convert string ke int
user_memilih = int(input("Coba tebak di dalam goa ada seekor hewan, di goa manakah dia berada? [1/ 2/ 3/ 4] "))

# TUgas: saat sudah mengisi jawban diperlukan untuk verifikasi, jadi ga langsung ke if else yg ada di bawah
user_verifikasi = input(f'''Yakin kamu ingin menjawab {user_memilih}?  [y/n] ''')
 
#  Program oci
# if user_verifikasi == 'y':
#    if user_memilih == possition:
#     #  harusnya disini dikasih jeda beberapa detik baru print jawaban
#      print("Okei.. Segera di prosess...") 
#      time.sleep(2) # << MEMBERI JEDA DISINI  
#      print(f"CONGRATS INTUISI {user_name} BAGUS, posisi goa ada di nomor {possition} sedangkan yang kamu pilih adalah goa nomor {user_memilih} ")
#    else:
#      print("Okei.. Segera di prosess...") 
#      time.sleep(2)  # << MEMBERI JEDA DISINI  
#      print(f'''SORRY,KAMU PERLU MENGASAH INTUISIMU. posisi goa yang sebenarnya ada di nomor {possition} sedangkan yang kamu pilih adalah goa nomor {user_memilih}  ''')
#  #  elif adalah singkatan dari "else if".
# # Fungsinya adalah untuk menambahkan kondisi alternatif setelah if, tanpa harus menulis banyak if terpisah
# elif user_verifikasi == 'n':
#   print("Baik, silakan coba lagi kapan-kapan ya.")
# else:
#   print("Input verifikasi tidak dikenali. Harap masukkan 'y' atau 'n'.")


# Program dea
if user_verifikasi == "n":
    print("Program akan segera dihentikan...")
    time.sleep(2)
    exit()
    # supaya program kembali ke tahapan awal, perlu sythax exit()

elif user_verifikasi == "y":
    if user_memilih == possition:
     print("Okei.. Segera di prosess...") 
     time.sleep(2) # << MEMBERI JEDA DISINI  
     print(f" {goa_without_array} \n CONGRATS... INTUISI {user_name} BAGUS, posisi goa ada di nomor {possition} sedangkan yang kamu pilih adalah goa nomor {user_memilih}")
    else:
      print("Okei.. Segera di prosess...") 
      time.sleep(2)  # << MEMBERI JEDA DISINI  
      print(f''' {goa_without_array} \n SORRY,KAMU PERLU MENGASAH INTUISIMU. posisi goa yang sebenarnya ada di nomor {possition} sedangkan yang kamu pilih adalah goa nomor {user_memilih} ''')
else:
    print("Silahkan ulangi program")
    exit()



# if user_memilih == possition:
#  print(f"CONGRATS INTUISI {user_name} BAGUS, posisi goa ada di nomor {possition} sedangkan yang kamu pilih adalah goa nomor {user_memilih} ")
# else:
#  print(f"SORRY,KAMU PERLU MENGASAH INTUISIMU. posisi goa yang sebenarnya ada di nomor {possition} sedangkan yang kamu pilih adalah goa nomor {user_memilih}  ")
