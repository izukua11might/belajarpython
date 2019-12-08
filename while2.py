#while dan else
Angka = 0
while Angka < 10:
    print(Angka)
    Angka += 1
else:#terjadi saat while habis terpenuhi
    print('angka',Angka,'ditemukan','\n' )

#while if dan break
ANgka = 0
while ANgka < 10:
    print(ANgka)
    ANgka += 1
    if ANgka is 5:
        print('angka',ANgka,'ditemukan')#berhenti saat ini dipenuhi
        print('\n')
        break
else:
    print("batas")

#while if dan continue
angka = 0
while angka < 10:
    print(angka)
    if angka is 5:
        print('angka 5 ditemukan')
        angka += 1 #wajib jika melakukan berulangan kontinue supaya tidak terjadi looping
        continue
    angka +=1
else:
    print('batas')