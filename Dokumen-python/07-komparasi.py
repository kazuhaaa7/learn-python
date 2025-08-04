#  operasi komparasi

# setiap hasil dari komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

x = 5
y = 1

# lebih dari (>)
# sub
# materi = "INI LEBIH DARI (>)"
# print('=' * 7, materi, '=' * 7)
hasil = x > 2
# print(x, ">", 2, "=", hasil )
hasil = y > 2
# print(y, ">", 2, "=", hasil )
hasil = y > 6
# print(x, ">", 6, "=", hasil )


# kurang dari (<)
# materi1 = "INI KURANG DARI (<)"
# print('=' * 7, materi1, '=' * 7)
hasil = x < 2
# print(x, "<", 2, "=", hasil )
hasil = y < 2
# print(y, "<", 2, "=", hasil )
hasil = y < 6
# print(y, "<", 6, "=", hasil )


# kurang atau sama dengan dari (<=)
# materi2 = "INI KURANG DARI ATAU SAMA DENGAN (<=)"
# print('=' * 7, materi2, '=' * 7)
hasil = x <= 2
# print(x, "<=", 2, "=", hasil )
hasil = y <= 2
# print(y, "<=", 2, "=", hasil )
hasil = y <= 1
# print(y, "<=", 1, "=", hasil )


# lebih atau sama dengan dari (>=)
# materi3 = "INI LEBIH DARI ATAU SAMA DENGAN (>=)"
# print('=' * 7, materi3, '=' * 7)
hasil = x >= 2
# print(x, ">=", 2, "=", hasil )
hasil = y >= 2
# print(y, ">=", 2, "=", hasil )
hasil = y >= 1
# print(y, ">=", 1, "=", hasil )


#  sama dengan (==)
materi4 = "INI SAMA DENGAN(==)"
# print('=' * 7, materi4, '=' * 7)
hasil = x == 2
# print(x, "==", 2, "=", hasil )
hasil = y == 1
# print(y, "==", 1, "=", hasil )


#  tidak sama dengan (!=)
materi5 = "INI TIDAK SAMA DENGAN(!=)"
# print('=' * 7, materi5, '=' * 7)
hasil = x != 2
# print(x, "!=", 2, "=", hasil )
hasil = y != 1
# print(y, "!=", 1, "=", hasil )

# 'is' sbg komprasi object identity
materi6 = "KOMPARASI/ PERBANDINGAN OBJECT(IS)"
print('=' * 7, materi6, '=' * 7)
a = 5  # ini sbg assignment membuat object
b = 5
hasil = a is b
print(hasil)


# 'is' sbg komprasi object identity
materi6 = "KOMPARASI/ PERBANDINGAN OBJECT(IS)"
print('=' * 7, materi6, '=' * 7)
a = 5  # ini sbg assignment membuat object
b = 6
hasil = a is b
print(hasil)
# imo: 'is' ini membangdikan 2 variable. bila salah satu variable bernilai tida sm dgn variable lain, maka result False. when kedua var bernilai sama, maka result akan True


# 'is not'
isi = "IS NOT"
# print('=' * 7, isi, '=' * 7)
a = 5  # ini sbg assignment membuat object
b = 7
hasil = a is not b
# print(hasil)
# imo: ini kebalikan dari si 'is' klo diubah jadi bahasa manusia tu gini: x tidak sama dgn y, klo iya berarti true kalo ngga false


# 'is not'
isi = "IS NOT"
# print('=' * 7, isi, '=' * 7)
a = 5  # ini sbg assignment membuat object
b = 5
hasil = a is not b
# print(hasil)
# imo: ini kebalikan dari si 'is' klo diubah jadi bahasa manusia tu gini: x tidak sama dgn y, klo iya berarti true kalo ngga false
