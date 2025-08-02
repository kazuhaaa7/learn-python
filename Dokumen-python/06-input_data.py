# Input User

# data yg dimasukkan pasti typ string
# data = input("Masukan data: ")
# print("data = ", data, "type = ", type(data))

#jika data yg diinginkan bertyp int/flot 
# angka = float(input("Masukkan angka: "))
# print("data = ", angka, "type = ", type(angka))

# kalo ingin output false, maka lakukan casting 2 kali: int lalu ke bool
# boo = bool(int(input("Masukkan angka: ")))
# print("data = ", boo, "type = ", type(boo))

# bisa juga dgn str
boo = bool(str(input("Masukkan angka: ")))
print("data = ", boo, "type = ", type(boo))

