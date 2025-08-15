# menggabungkan opersi dg string / manipulasi string (1)
#1. menyambung string (concataate)
name1 = "oci"
name2 = "lord"
merge = name1 + " " + name2
print(merge)
name1 = name1 + "'" + name2
print(name1)#akan menimpa variabel sebelumnya

# 2. menghitung panjang string (length)
hasil = len(name1) #memakai perhitung sistem manusia, len: helper function dari python
print(str(hasil), " " + "char")

# 3. operator untuk string

# mengechek apakah
o = "o"
genjutsu = o in name1
print(f"string {o} yg ada di {int(genjutsu)} = {genjutsu} ")

f = "g"
genjutsu = f not in name1
print(f"string {f} tidak ada di = {genjutsu} ")


# indexing
print(f'index ke-(-2) {name1[-2]}')
# metode slicing : sampai sbvlm 7
# start:stop:step
print(f'index ke-[2-7] dgn pola lompat 2 {name1[2:7:2]} ')

# item paling kecil(urutan abjad)
print(f"ini item paling kecil: {min(name1)}")

# item paling besar(urutan abjad)
print(f"ini item paling besar: {max(name1)}")

# output: mengetahui posisi object dalam perhitungan abjad
asci_code = ord(" ")
print(f"ASCII code untuk spasi adlaah: {str(asci_code)}")

data = 200
print(f"char untuk ASCII 200 adlaah: {chr(data)}")


# 4. operator dalam bentuk method

prove = "Aku maba Fasilkom UNEJ"
jumlah = prove.count("a")# ada brp banyak si huruf a di variabel prove
print(f"jumlah a pd {prove} adalah: {str(jumlah)}") 
# di sini ada kekurangannya saat menghitung huruf a, huruf kapital ga kehitung


# menggabungkan opersi dg string / manipulasi string (1)
# operator dalam bentuk metode

##merubah case dari string
# merubah semua ke upper case

hai = "helo"
print(f"{hai} oci")