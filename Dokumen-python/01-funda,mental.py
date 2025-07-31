# string = "Wellcome sir"
# print(len(string))
# fungsi len() unutk menegbalikan panjang char string dari variabel yg ada di dlm parameternya
# print(string[- 12])
# akan mengembalikan nilai dgn dibalik jadi index -1 adala r
# print(string[0:2])
# the patterm : Start:Stop:Step, akan mengembalikan  nilai dari index 0 hingga sebelem 2
# print(string[0:])
# mengembalikan nilai daru index 0 sampai akhor index
# print(string[:])
# mengembalikan nilai dari index 0 sampai akhor index

#  \"
#  \'
#  \\
# \n

# eks = "going \nplane"
# print(eks)

# Type data
# inT
integer = 4
# print(type(integer))

# # loat atau desimal
float = 0.7
# print(type(float))

# Boolea= Data Biner
boolean = True
# print(type(boolean))

# String
string = "ini string"
# print(type(string))
full = "fathor"
name = "rossi"
Id = full + " " + name
id = f"{full} {name}"
# print(id)

# List= kumpulan element/object  yg dapat dimodifikasi isinya
list = ["liat1", "list2", "list3", 58, 45.7]
# print(type(list))

# Tuple= kumpulan element /object yg TIDAK dapat dimodifkasi isinya
tuple = ("inituple1", "initiple2", "initiple3", 1, "hai")
# print(type(tuple))

# set = kumpulan data yg UNIK dan TIDAK BERURUTAN
set = {20, 10, 1, 4, 3, 4, 6, 87}
# print(set)
# print(type(set))

# dictionary= kumpulan pasangan key-value/kunci-nilai
dictionary = {"eat": "makan", "minum": "beer"}
# print(type(dictionary))


# Method
course = "    hai i course"
# upper() untuk merubah menjadi kapital semua
print(course.upper())
# lower() untuk merubah menjadi kecil semua
print(course.lower())
# title() untuk merubah menjadi format 
print(course.title())
# strip() untuk mengahpus beberapa spasi yg ada di sebalah kiri, bisa jg dgn (lstrip() / rstrip())
print(course.strip())  
# find() untuk menemukan indeks yg ada dlm methode
print(course.find("hai"))
#  replace() untuk merubah huruf/ kata
print(course.replace("i", "u"))
# # untuk mengecheck, apakah ada kata " " di variable...(boolean)
print("hai" in course)
# #
# # untuk mengecheck, apakah ada kata " " di variable...(boolean)
print("hai" not in course)
