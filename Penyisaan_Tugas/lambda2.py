panjang = int(input('Masukkan Panjang: '))
lebar = int(input('Masukkan Lebar: '))

luas = lambda p,l: p*l
keliling = lambda p,l: 2*p*l

print (f'Luas : {luas(panjang,lebar)} cm2 \nKeliling : {keliling(panjang,lebar)}cm2')