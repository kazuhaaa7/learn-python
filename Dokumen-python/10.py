print('-----0+++++5-----10+++++15-----')
userMenginput = float(input('Masukkan angka: '))

# Interval 1: (0, 5)
Hp1 = userMenginput > 0 and userMenginput < 5

# Interval 2: (10, 15)
Hp2 = userMenginput > 10 and userMenginput < 15

# Gabungan dua himpunan
hasil = Hp1 or Hp2

print('Apakah angka masuk ke dalam himpunan? =', hasil)
