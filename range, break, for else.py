#Range
for i in range (0,11,2): #for merupakan perulangan, format nya: for <variabel> in range (awal,akhir,jarak)
    print(i)
print()

#break dalam logika(if)
number = 4
for x in range (0,11):
    print(x)
    if x is 4:
        print('angka',number,'ditemukan\n')
        break#mengakhiri loop for dengan jika logika sudah tercapai

#else dalam perulangan(looping)
Number = 12

for y in range (0,11):
    print(y)
    if y is Number:#tidak tereksekusi karena angka 12 atau bariable Number tidak ditemukan
        print('angka',Number,'ditemukan')
        break
else:#letak nya sejajar dengan for supaya tereksekusi setelah 'print(y)' berjalan
    print('angka tidak ditemukan')#else akan di eksekusi jika variable number tidak ditemukan