# contoh tipe data set 1
superman = {'wiro sableng', 'gundala', 'sarah 008', 'si buta dari gua hantu','akua man'}
superman.add('gundala') # gak muncul karena data sudah ada
superman.add('mak lampir') # muncul karena data baru
print(superman) # data akan acak

# contok tipe data set 2
Superman = set()
superman.add('wiro sableng')
superman.add('mak lampir')
superman.add('gundala')
print(sorted(superman)) # data akan tersusun sesuai abjad karena perintah sorted

# contoh tipe data set 3
ganjil = {1,3,5,7,9,} # selain string set juga mendukung angka
genap = {2,4,6,8,10}
prima = {2,3,5,7}
print(ganjil.union(genap)) # data akan tergabung
print(ganjil.intersection(prima)) # data akan ter iris