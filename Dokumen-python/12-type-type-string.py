hai = "ini type-type string"
print(hai)
print(type(hai))

# cara membuat string

'''
    1. ini menggunakan single quote '...'
    2. ini menggunakan double quote '...'
'''

str = 'ini menggunakan single quote'
print(str)

str = "ini menggunakan double quote"
print(str) 

# bila ingin buat program memetik ungkapan seseorang, bisa gunakan seperti ini
kutip = '"Hai, namaku rossi. who are u?"'
print(kutip)

# bila ingin buat program membuat suatu ungkapan yg memiliki makna berbeda
makna =  "'amplop'"
print(makna)

'''
    ini menggunakan \
    membuat tanda ' menjadi string
'''

print('ayo sholat jum\'at')
print ('I\'ve be someone, isn\' it ')

# backslash
# print('C:\user\py')# \ dianggap karakter khusus, bila ingin membuat output yg mengandung karakter backslash perlu tambahkan menjadi 2 backslash
print('C:\\user\\py')# nothing bug

# tab
print('oci\tlord. memberikan bebrapa space')# akan memberikan output jarak bebrp spasi

#backspace
print('oci   \blord')# menghapus 1 spasi ke belakang

# newline
print('line number one\n line number two')#==> LV :line feed #otomatis memberikan enter ke bawah, ->unic, macos, linux
print('line number one\r line number two')#==> CR : carriage return, -> old language :commodore, lisp, acorn
print('line number one\r\n line number two')#==> CTRL : line feed carriage return, -> windows

# without raw string
print('C:\new folder')

# use raw string
print(r'C\new folder')# akan dibaca tetap string

# multiline literal string
print("""
    today i'm done ospek day-3
    and tomorrow i will papermob exercise at four o'clock
""")

# menggabungkan antara rwa string dgn multiline literal string
print(r"""
file oci di
      c:\user\desktop
""")