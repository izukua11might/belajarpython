nama_band = ['payung teduh',
             'fourtwenty',
             'dialog dini hari',
             'para hyena']
kumpulan_lagu = ['akad',
                 'zona nyaman',
                 'rumahku',
                 'sindoro']

# looping biasa
for i in nama_band:
    print (i)
print()

# looping biasa dengan angka
literasi = 0;
for i in nama_band:
    print('no:', literasi, i)
    literasi += 1
print()

# enumerate (khusus angka tanpa ribet)
for index,band in enumerate(nama_band):
    print('no', index,'nama band', band)
print()

# zip (menggabungkan 2 variabel berbeda)
for i,v in zip(nama_band,kumpulan_lagu): # inisial harus sejajar sesuai keinginan outputnya
    print('band', i, 'akan menyanyikan lagu', v)
print()

#looping pada tipe data set
playlist = {'memories','when we were young', 'senorita', 'i dont care'}
for i in sorted(playlist):
    print(i)
print()

#looping pada dictionary
playlist2 = {'maroon 5':'memories',
             'adele':'when we were young',
             'shawn mendes and camila camelo':'senorita',
             'ed sheeran and justin bieber': 'i dont care'}
for i in playlist2.keys():
    print('penyanyi malam ini', i) # menampilkan key saja

print()
for i in playlist2.values():
    print('deretan lagu malam ini', i) # menampilkan value saja

print()
for i,v in playlist2.items():
    print(i, 'menyanyikan lagu', v)

print()

# looping angka terbalik
for i in reversed(range(1,10,1)):
    print(i)




