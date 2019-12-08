# menggunanakan tuples dan membandingkan dengan list
data_list = [1,2,3,4,5,6,7,8,9,10] #menggunkan kurung siku
data_tuple = (1,2,3,4,5,6,7,8,9,10) #menggunkan kurung biasa

#membaca jenis class
print(type(data_list))
print(type(data_tuple))

#fitur tuple
print(dir(data_tuple))#melihat kegunaan yang tersedia pada commad (berlaku untuk semua)
print(data_tuple.count(2))#menghitung banyak data 2 (isi dalam kurung tergantung kegunaan)
print(data_tuple.index(2))#mencari posisi 2 dalam data (isi dalam kurung tergantung kegunaan)

# Meskipun  tuple lebih kecil ukuran nya, lebih Cepat, dan lebih Ringan
# Tetapi tuple data nya baku dan bersifat Imutable yaitu tidak bisa di Rubah di Kurang maupun di Tambah