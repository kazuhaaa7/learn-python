# Operation Logic or Boolean

# not
Not = "NOT"
print('\n','=' * 7, Not, '=' * 7,'\n')
a = True
c = not a
print('data a =',a)
print('-' *7 ,'NOT')
print('data c =', c)

# or \BERLAKU 3 VAR ATAU LEBIH\
print('\n','-' * 7 ,'OR','-' * 7,'\n')
print('False + False')
x = False
y = False
z = x or y
print(x, 'OR',y, '=', z)

print('False + True')
x = False
y = True
z = x or y
print(x, 'OR',y, '=', z)

print('True + False')
x = True
y = False
z = x or y
print(x, 'OR',y, '=', z)

print('True + True')
x = True
y = True
z = x or y
print(x, 'OR',y, '=', z)
# imo: ini perbadingan 3 var. bila ada salah satu yg True, maka hasilnya akan true. begitu juga dgn keduanta True maka hasilnya akan True. when ada 2 False, maka hasilnya akan False 

# and \BERLAKU 3 VAR ATAU LEBIH\
print('-' * 7 ,'AND', '-' * 7, '\n' )
print('False + False')
x = False
y = False
z = x and y
print(x, 'AND',y, '=', z)

print('False + True')
x = False
y = True
z = x and y
print(x, 'AND',y, '=', z)

print('True + False')
x = True
y = False
z = x and y
print(x, 'AND',y, '=', z)

print('True + True')
x = True
y = True
z = x and y
print(x, 'AND',y, '=', z)
# imo: ini kebalikan dari

# xor \BERLAKU 3 VAR ATAU LEBIH\
# (akan true bila salah satu true. false bila keduanya true atau false)
print('\n','-' * 7 ,'XOR', '-' * 7, '\n')
print('False + False')
x = False
y = False
z = x ^ y
print(x, 'XOR',y, '=', z)

print('False + True')
x = False
y = True
z = x ^ y
print(x, 'XOR',y, '=', z)

print('True + False')
x = True
y = False
z = x ^ y
print(x, 'XOR',y, '=', z)

print('True + True')
x = True
y = True
z = x ^ y
print(x, 'XOR',y, '=', z)
# imo: bila ad 2 var dgn nilai bool yg sama, maka hasilnya akan false. when ada 2 var dgn nilai bool tidak sama, maka hasilnya true