x = int(input("Masukkan Nilai X : "))
y = int(input("Masukkan Nilai Y : "))
z = int(input("Masukkan Nilai Z : "))

# nilai tebesar
if x > y and x > z :
    print (f'Nilai Terbesar Adalah Nilai X, yaitu : {x}')
elif y > x and y > z :
    print (f'Nilai Terbesar Adalah Nilai Y, yaitu : {y}')
elif z > y and z > x :
    print (f'Nilai Terbesar Adalah Nilai Z, yaitu : {z}')
    
# nilai terkecil
if x < y and x < z :
    print (f'Nilai Terkecil Adalah Nilai X, yaitu : {x}')
elif y < x and y < z :
    print (f'Nilai Terkecil Adalah Nilai Y, yaitu : {y}')
elif z < y and z < x :
    print (f'Nilai Terkecil Adalah Nilai Z, yaitu : {z}')
    
# nilai sama
if x == y and y == z and y == x :
    print (f'Nilai Sama Tidak Ada Yang Terkecil dan Tidak Ada Yang Terbesar')

# or
# nilai_terbesar = max(x, y,z)
# nilai_terkecil = min(x, y, z)

# print('''Nilai terbesar : {nilai_terbesar}
# Nilai Terkecil : {nilai_terkecil}''')
