#  operator bitwise, operasi biner,binery

a = 8
b = 7

# bitwise OR (|)
c = a | b
print('\n', '-' * 5, 'OR','-' * 5 )
print('nilai :',a,', binary : ', format(a, '08b'))#b for binery
print('nilai :',b,', binary : ', format(b, '08b'))
print('-' * 25, '(|)')
print('nilai :',c,', binary : ', format(c, '08b'))

# bitwise AND (&)
c = a & b
print('\n', '-' * 5, 'AND','-' * 5 )
print('nilai :',a,', binary : ', format(a, '08b'))
print('nilai :',b,', binary : ', format(b, '08b'))
print('-' * 25, '(&)')
print('nilai :',c,', binary : ', format(c, '08b'))

# bitwise XOR (^)
c = a ^ b
print('\n', '-' * 5, 'XOR','-' * 5 )
print('nilai :',a,', binary : ', format(a, '08b'))
print('nilai :',b,', binary : ', format(b, '08b'))
print('-' * 25, '(^)')
print('nilai :',c,', binary : ', format(c, '08b'))

# bitwise NOT (~)
# blm bisa dipahami