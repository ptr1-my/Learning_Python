x = float(input('Masukkan Nilai X : '))
y = float(input('Masukkan Nilai Y : '))
z = float(input('Masukkan Nilai Z : '))

# nilai terbesar
if x > y and x > z:
    print(f'Nilai Terbesar Adalah X : {x}')
elif y > x and y > z:
    print(f'Nilai Terbesar Adalah Y : {y}')
elif z > y and z > x:
    print(f'Nilai Terbesar Adalah z : {z}')
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
