# cara 1 (default)
import matematika
matematika.tambah(4,5)
matematika.kurang(4,5)

print()

# cara 2 (inisial)
import matematika as math
math.tambah(1,3)
math.kurang(1,3)

print()

# cara 3 (individual)
from matematika import tambah,kurang
tambah(2,5)
kurang(5,2)

print()

# cara 4 (individual take all)
from matematika import *
tambah(3,4)
kurang(4,3)

print()

# cara 5 (individual and inisial)
from matematika import kurang as k
k(100,99)