# stack atau tumpukan
tumpukan = [1, 2, 3, 4, 5, 6]
print('data sekarang:', tumpukan)

# menambahkan data pada stack
tumpukan.append(7)
print('dta masuk:', 7)

tumpukan.append(8)
print('data masuk:', 8)
print('data sekarang:', tumpukan)

# menggunakan stack/tumpukan dalam variabel
out = tumpukan.pop()
print('data keluar:', out)
print('data sekarang:', tumpukan)

print(20*'"', 'queues', 20*'"')

# queues atau antrian
from collections import deque  # modul untuk mengambil source kode lain ke kode kita
antrian = deque([1, 2, 3, 4, 5])
print('data sekarang:', antrian)

# menambahkan data pada queues
antrian.append(6)
print('data masuk:', 6)
print('data sekarang:', antrian)

antrian.append(7)
print('data masuk:', 7)
print('data sekarang:', 7)

# menggunakan queus
out = antrian.popleft()
print('data keluar:', out)
print('data sekarang:', antrian)

out = antrian.popleft()
print('data keluar:', out)
print('data sekarang:', antrian)
