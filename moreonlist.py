barang = ['kunci','sepatu','ikat pinggang','motor']
print(barang)

#menambahkan list
barang.append('sepeda')
print(barang)

#menambahkan perkata
barang.extend("dompet")
print(barang)

#merubah per baris
barang.insert(3,'sepeda')
print(barang)

#menghitung baris
jumlahalfabet = barang.count('a')
jumlahkata = barang.count('sepeda')
print(jumlahalfabet)
print(jumlahkata)

#menghapus data dalam list
barang.remove("sepeda")
print(barang)

#memutarbalikan data dalam list
barang.reverse()
print(barang)

print(50*'=')

#mengcopy list dalam variable
stuff = barang.copy()
stuff.append('batang')
print(stuff)

print(barang)