#scope bersifat global dan local
namaKucing = 'antonio'#tidak terubah
makananKucing = 'royal cis'#berubah

def rubahnama(nama):
    namaKucing = nama #localscope

def rubahmakanan(makanan):
    global makananKucing
    makananKucing= makanan #global scope karena ada keyword globalnya

rubahnama('asyrof')
rubahmakanan('mamam')
print('nama kucing saya',namaKucing,'makannya',makananKucing)
