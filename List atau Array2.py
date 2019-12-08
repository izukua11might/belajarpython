#|1|4|9|16|25|36|49|64|
#| | | |  |  |  |  |  |
#0 1 2 3  4  5  6  7  8

Data  = [1,4,9,16,25,36,49,64] #list normal
Data2 = [2,4,6,8,10,12,14,16]
Data3 = [100,200,300,400,500,600,700,800]

#method pada list
Data.append(30)
Data2.append(Data3)

print(Data, '"ini Variable Data yg angka 30 tertambahkan berkat command append"')
print(Data2, '\"ini Variable Data2 tergabung dgn Data3\"')
print('harusnya gini Variable Data nya : \n'
      '[1,4,9,25,36,49,64]')
print('harusnya gini variable Data2 nya : \n'
      '[2,4,6,8,10,12,14,16 \n')
#fungsi append iayalah untuk menambahkan data dalam list
#sebagai contoh angka 30 tertambahkan melalui command method 'append'
#begitu juga dengan dengan Data3 tergabung dalam list Data2 karena method 'append' tersebut

#fungction yang bisa digunakan pada list
panjang_list = len(Data)

print(Data, '<<variable yang dihitung si command \'len\'')
print(panjang_list, '   <<ini hasil command dari "len"')
#"panjang_list" sama halnya seperti variable biasa
#bagian ini menunjukkan fungsi dari command 'len' yang berfungsi sebagai
#pengTotal semua data yang tersaji dalam list sebuah variabel