import sys

#membandingkan ukuran list dan tuple
data_list = [1,2,3,4,5,6,7,8,9,'pisang goreng','nasi uduk',3.15]
data_tuple = (1,2,3,4,5,6,7,8,9,'pisang goreng','nasi uduk',3.15)

totaldatalist = sys.getsizeof(data_list)
totaldatatuple = sys.getsizeof(data_tuple)

print('besar ukuran data list:', totaldatalist)
print('besar ukuran data taple:', totaldatatuple)

print(10*'=','terbukti tuple lebih sedikit memakan ukuran',10*'=')