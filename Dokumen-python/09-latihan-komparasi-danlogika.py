# membuat himpunan dgn contoh garis bilangan
##kasus 1
## cari hp yg +
# ++++++++5--------10+++++++

# print('++++++++5--------10+++++++')
# inputUser =  float(input('silahkan masukkan\n angka yg tepat\n menurutmu: '))

# ++++++++5---------------
# memeriksa angka kurang dari 5
# iniKurangDari = (inputUser < 5)
# print('Kurang dari 5 =', iniKurangDari)

# ---------------10+++++++
# memeriksa angka lebih dari 10
# iniLebihDari = (inputUser > 10)
# print('Lebih dari 10 =', iniLebihDari)

# ++++++++5--------10+++++++
# inReesult = (iniKurangDari or iniLebihDari)
# print('angka yg anda masukkan: ', inReesult)

# variabel inReesult akan False bila himpunan sm dgn batas yg ada pd garis bilangan



## kasus 2, irisan
## cari hp yg +
# -----5++++++++++++++++10-----
# print('\n',7* '*', 'kasus 2', '*' * 5,'\n') #perhatikan syntax
# print('-----5++++++++++++++++10-----')
# Userinput = float(input('Masukkan angka\n yg ada dlm garis\n bilang di atas: '))

#-----5+++++++++++++++
# memeriksa angka lebih dari 5
# lebihdari = (Userinput > 5)
# print('Lebih dari 5 = ', lebihdari)


#++++++++++++++10-----
# memeriksa angka kurang dari 10
# kurangdari = (Userinput < 10)
# print('Kurang dari 10 = ', kurangdari)

# -----5++++++++++++++++10-----
# result = (lebihdari and kurangdari)
# print('Angka yg anda masukkan: ', result)


## tugas 1
## cari hp yg +
# -----0+++++5-----10+++++15-----

#-----0++++++++++
# memeriksa angka lebih dari 0
# print('-----0+++++5-----10+++++15-----')
# userMenginput = float(input('Masukkan angka: '))
# Hp1 = (userMenginput > 0)
# print('lebih besar dari 0 = ', Hp1)

# +++++5----------
# memeriksa angka kurang dari 5
# Hp2 = (userMenginput < 5)
# print('kurang dari 5 =', Hp2)

# -----10++++++++++
# memeriksa angka lebih dari 10
# Hp3 = (userMenginput > 10)
# print('lebih dari 10 =', Hp3)

# +++++15----------
# memeriksa angka kurang dari 10
# Hp4 = (userMenginput < 15)
# print('kurang dari 10 =', Hp4)

# hasil = (Hp1 or Hp2 and Hp3 or Hp4 )
# print('angka yg anda masukkan =', hasil)

## clean code by chtgpt
# print('-----0+++++5-----10+++++15-----')
# userMenginput = float(input('Masukkan angka: '))

# Interval 1: (0, 5)
# Hp1 = userMenginput > 0 and userMenginput < 5

# Interval 2: (10, 15)
# Hp2 = userMenginput > 10 and userMenginput < 15

# Gabungan dua himpunan
# hasil = Hp1 or Hp2

# print('Apakah angka masuk ke dalam himpunan? =', hasil)


##tugas 2
# +++++0-----5+++++10-----15+++++
print('+++++0-----5+++++10-----15+++++')
userMenginput = float(input('Masukkan angka: '))

# Interval 1: ( ,0)
HP1 = userMenginput < 0 

# Interval 2: (5, 10)
HP2 = userMenginput > 5 and userMenginput < 10

# interval 3: (15, )
HP3 = userMenginput > 15 

# Gabungan dua himpunan
Hasil = HP1 or HP2 or HP3
print('Apakah angka\n masuk ke dalam\n himpunan? =', Hasil)

#✅ akai and untuk interval tunggal seperti (5, 10)
#✅ Pakai or untuk gabungan beberapa himpunan terpisah

