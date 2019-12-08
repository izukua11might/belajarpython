#fungsi dan argumen sederhana
def fungsi(argumen):
    print('ini adalah fungsi sederhana dan', argumen, 'nya','\n')

fungsi('input')

#fungsi dan keyword argumen
def guru(nama,pelajaran):
    print('nama gurunya:',nama)
    print('pelajarannya :',pelajaran,'\n')

guru(nama='maman',pelajaran='matematika')#keyword argumen nya
guru(pelajaran='seni budaya',nama='udin')#boleh dibalik hasil tetap berurutan
guru('olahraga','mimin')#hasil akan terbalik
guru('maman','yoga')#parameter/input tanpa keyword

#fungsi dan argumen default
def penjagaSekolah(nama,shift='pagi',galak='tidak'):
    print('nama penjaga sekolah:',nama)
    print('jam kerja nya:',shift)
    print('galak kah?:',galak,'\n')

penjagaSekolah('asyrof')#hasil shiift dan galak akan default terPrint
penjagaSekolah('agung',shift='siang',galak='Sangad')#dapat di ubah
penjagaSekolah(shift='malam',galak='iya')#akan gagal karena tidak ada inpput namanya