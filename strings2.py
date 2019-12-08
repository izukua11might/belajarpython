# Penjelasan jenis a = text[0:10]
#|p|i|s|a|n|g| |g|o|r| e| n| g|
#| | | | | | | | |   |  |  |  |
#0 1 2 3 4 5 6 7 8 9 10 11 12 13

text = "pisang goreng"

a = text[0]
b = text[5]
c = text[0:5]
d = text[0:6]
e = text[7:13]
f = text[-4]
g = text[7:]

print(a + ' | kalo nulis 0')
print(b + ' | kalo nulis 5')
print(c + ' | kalo nulis 0:5 atau 0 sampai 5')
print(d + ' | kalo nulis 0:6 atau 0 sampai 6, ini baru bener jika ingin hasilnya pisang')
print('ee'+ e + ' (kalo ini kompinasi nya)')
print(f + ' | minus kebelakang alfabet dari huruf pertama jadi majunya ke depan')
print(g + " | dari nomor huruf pertama sampai habis kata")

#lebih jelasnya : menggunakan [] untuk range
#                 menggunakan  : untuk sampai mana atau sama dengan (-)
#                 0 = p untuk awal kata dan 5 = g dan 6 untuk akhir kata
#                 harusnya spasi tapi itu lah ketentuan nya