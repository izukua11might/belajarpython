#|1|4|9|16|25|36|49|64|
#| | | |  |  |  |  |  |
#0 1 2 3  4  5  6  7  8

Data = [1,4,9,16,25,36,49,64]
Data2 = [2,4,6,8,10,12,14,16]

#mengakses list
Subdata = Data[3]
Subdata2 = Data[-3]

print('mengakses list')
print(Subdata)
print(Subdata2, "\n")

#memotong list
Subdata3 = Data[0:4]
Subdata4 = Data[:2]
Subdata5 = Data[2:]
Subdata6 = Data[:-5]

print('memotong list')
print(Subdata3)
print(Subdata4)
print(Subdata5)
print(Subdata6, '\n')

#menambah list
Data3 = [100,200,300,400,500,600,700,800]
Data4 = Data + Data3

print('menambah list')
print(Data4, "\n")

#mengcopy list ke variable baru
a = Data[:]
a[4] = 87 # merubah variable Data nomor 4 yaitu 25 menjadi 87

print('mengcopy list ke variable baru')
print(Data, 'data normal')
print(a, 'data stelah dirubah 25 menjadi 87 \n')

#merubah content list dengan menggunakan metode slashing
Data2[3:5] = [11,12]

print('merubah list dengan metode slashing')
print('[2,4,6,8,10,12,14,16]', 'harusnya seperti ini')
print(Data2, 'stelah di rubah \n')

#list dalam list
x = [Data,Data3]

print('list di dalam list')
print(x, '\n')

#mengakses list di dalam multi dimensional list
y = x[1][4] #kurung pertama([]) yang berisi angka 1 untuk memilih list
            #kurung kedua yang  berisi angka 4 untuk memilih Data dalam list tersebut
            #maka terambillah angka 500 yang merupakan data dari list kedua atau list identity '1'

print('mengakses list dalam multidimensional list')
print(x)
print(y,'\n')
# ----------------------gambaran-----------------------------
# [[1,4,9,11,12,36,49,64], [100,200,300,400,500,600,700,800]]
#  || | |  |  |  |  |  | |  |  |   |   |   |   |   |   |   |
#  01 2 3  4  5  6  7  8 9  0  1   2   3   4   5   6   7   8
#  |                        |                              |
#  0                        1                              2

