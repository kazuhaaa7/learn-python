
# menggabungkan opersi dg string / manipulasi string (1)
# operator dalam bentuk metode

##merubah case dari string
# merubah semua ke upper case

hai = "helo"
print(f"sebelum diberi method = {hai} ")
hai = hai.upper()
print(f"{hai} <-- ini upper")

# merubah semua ke lower case

salam = "WASSAP BROHG"
print(f"SEBELUM DIBERI METHOD = {salam} ")
salam = salam.lower()
print(f"{salam} <-- ini upper")

## pengechekan dengan isX method
morning = "pagi ninoku"
isThis_lower = morning.islower() #memberikan output type class bool
print(f"{morning} is lower = {str(isThis_lower)}")
isThis_upper = morning.isupper() #memberikan output type class bool
print(f"{morning} is upper = {str(isThis_upper)}")
