#fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print('hasil dari pangkat',argumen,'adalah:',total)
    return total #total dapat digunakan kembali

a = kuadrat(3)
print(a)#dapat di gunakan kembali dalam prtint
print(50*'=')
#fungsi dan multiple return value
def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,'+',argumen2,'=',total)
    return total

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,'x',argumen2,'=',total)
    return total

b = kali(4,tambah(4,6))#dapat digunakan kembali sebagai pemanggil di dalam pemanggil fungsi dan pemanggil yang di dalam nya akan di eksekusi terlebih dahulu
print(20*'=','hasil variabel B',20*'=')
print(b)#menampilkan hasil akhir si pemanggil di dalam pemanggil