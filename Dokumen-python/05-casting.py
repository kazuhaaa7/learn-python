# Casting = merubah type satu menjadi type yg lain
# contoh, dri string ke int menggunakan int() 
#  type data: str, int, bool, float

data = 0
print("data = ", data, "type= ", type(data))

# # to int
data_int = int(data )
print("data_int = ", data, "type= ", type(data_int)) #bila variable berisi float maka akan dibulatkan, type string ga bisa diubah menjadi int begituu jg dghn float

# # to str
data_str = str(data )
print("data_str = ", data, "type= ", type(data_str))

# # to float
data_float = float(data )
print("data_float = ", data, "type= ", type(data_float))  

# to bool
data_bool = bool(data )
print("data_bool = ", data ,"type =", type(data_bool) )#akan false jika data berisi 0 dan jika string kosong