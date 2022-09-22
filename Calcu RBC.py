angka1=int(input("masukkan bilangan pertama"))
sis = input("masukkan +, -, x, :..")
angka2= int(input("masukkan bilangan kedua:"))

if sis == 'x':
    print('Hasilnya adalah...', angka1 * angka2)

elif sis == '-':
    print('Hasilnya  adalah...', angka1 - angka2)

elif sis == ':':
    print('Hasilnya Adalah...', angka1 / angka2)

elif sis == '+':
    print('Hasilnya Adalah...', angka1 + angka2)