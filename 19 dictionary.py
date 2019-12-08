# syntax dictionary : variable = { key:value, key:value}

# contoh 1 dictionary
member = {'id':101,
          'nama':'kang pukis',
          'pekerjaan':'mahasiswa'}
print(member['id']) # key nya yang di index
print(member.keys()) # melihat key variabel dictionary
print(member.values()) # melihat value variabel dicionary
print(member.items()) # melihat key dan value variabel dictionary

print()

# contoh 2 dictionary
member1 = {'id':101,
           'nama':'agung abdullah fajri',
           'pekerjaan':'freelancer'}
member2 = {'id':102,
           'nama':'gian rhamadhan',
           'pekerjaan':'employee'}
memberlist = {101:member1,102:member2}
print(memberlist[101])
