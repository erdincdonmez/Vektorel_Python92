# secim in ["1","2","3"]
["1","2","3"]
print(["1","2","4",4,5])
print(2 in ["1","2","4",4,5])
print("2" in ["1","2","4",4,5])

gun = input("Gün nedir?")
if gun in ["Cumartesi","Pazar"]: print("Tatil günü girdin")
else: print("Tatil günü değil")

# -----------------------------------------
a = 5
b = 7
# if a>b : print("Birinci sayı büyük")
# else: print("Birinci sayı ile ikinci eşit yada ikinci büyük")
print("Birinci sayı büyük" if a>b else "Birinci sayı ile \
ikinci eşit yada ikinci büyük")
