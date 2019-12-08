import timeit

# membandingkan kecepatan generate tuple dan list
list = timeit.timeit(stmt='[1,2,3,4,5,6,7,8,9,10]',number=10000)
tuple= timeit.timeit(stmt='(1,2,3,4,5,6,7,8,9,10)',number=10000)

print('hasil kecepatan generate list:',list)
print('hasil kecepatan generate tuple',tuple)
print(10*'=','terbukti tuple lebih cepat',10*'=')