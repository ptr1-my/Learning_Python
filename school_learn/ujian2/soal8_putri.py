n = int(input('Masukkan Nilai Angka : '))

if n > 100 and n < 1000:
    print('Nilai Tersebut Adalah Ratusan')
if n > 1000 and n < 1000000 :
    print('Nilai Tersebut Adalah Ribuan')
if n > 1000000 :
    print('Nilai Tersebut Adalah Jutaan')