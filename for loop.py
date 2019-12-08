# list sebagai iterable
gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']

for g in gorengan:# g yang di depan for merupakan variable baru
    print (g)     #yang mengakses data di variable gorengan oleh command for
    print(len(g)) #yang di aplikasikan dengan menprint g
                  #Command len untuk menghitung panjang atau jumlah kata dalam satu kata di dalam data variable

print()
# string sebagai iterable(penerapan looping)
Gorengan = 'bakwan'
for i in Gorengan:
    print(i)

print()
# for di dalam for
buah = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','wortel','tomat','kentang']

Daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in  Daftar_belanja:#for pertama menjabarkan list Dalam variaabel Dafta_belanja
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:#for kedua menguraikan list per komponen kata
        print(komponen)
        for lagi in komponen:#for ketiga lebih membedah data dan lebih menguraikan nya satu persatu dari list nya
            print(lagi)
