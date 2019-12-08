# type 1 (biasa)
text1 = 'jalan - jalan di hari minggu (type 1)'
print(text1)

# type 2 (memakai \ untuk mengaktifkan kutip)
text2 = 'jalan - jalan di hari jum\'at (type 2)'
print(text2)

# type 3 pemakaian double kutip("") untuk memakai kutip biasa(')
text3 = "jalan - jalan di hari jum'at (type 3)"
print(text3)

# type 4 contoh integer dialog dengan ('') diluar dan ("") di dalam
text4 = 'Mahmuy berkata, "kemaren kemana broh?" (type 4)'
print(text4)

# type 5 memakai (\) untuk pembuka dan penutup dengan ("") diluarnya
text5 = "Hobloh menjawab, \"jalan - jalan bro!\" (type 5)"
print(text5)

# type 6 stirng baris baru dengan (\n)
text6 = "(type 6 \'pakai baris\')\n|Mahmuy: \"kemaren kemana bro?\" \n|Hobloh: \"jalan - jalan bro!\""
print(text6)
text6simple = '(type 6 \'pakai baris simple dengan kutip satu('')\')\n|Mahmuy: "kemaren kemana bro?"\n|Hobloh: "jalan - jalan bro!"' #dengan kutip ('') dan sedikit /n
print(text6simple)

# type 7 mengunakan tiple kutip (""") dan Enter saja untuk membuat baris baru otomastis
text7 = """
mahmuy: "Kemaren kemana bro?"
hobloh: "jalan - jalan bro!
mahmuy: "jalan - jalan kemana bro?"
hobloh: "ke Mang Uing bro!!!!"
"""
print(text7)

# type 8  untuk mengakses deriktory mengunakan (r')
text8 = r'C:\Mycomputer (akses directory)'
print(text8)

# type 9 macam - macam Print strings
print(5*'wk') # perulangan pakai kali(*)
print(text1 + text2 +"(menggabungkan text1 dan 2)") # menggabungkan type data pakai tambah(+)
print('kue' "pukis""(text nyambung rangka berbeda)" ) # print biasa text nyambung
print("kue pukis""(text terpisah karena satu rangka)") #print satu rangka

#selesai nyambung di strings2