def segitiga():
    alas = int(input('\033[0;34mMasukkan Alas : '))
    tinggi = int(input('Masukkan Tinggi : '))
    lebar = int(input('Masukkan Lebar : '))
    
    luas = lambda a,t: 0.5*a*t
    keliling = lambda a,t,l: a+t+l
    
    print(f'Luas Segitiga : {luas(alas,tinggi)} cm2 \nKeliling Segitiga : {keliling(alas,tinggi,lebar)} cm')
    
segitiga()
segitiga()
segitiga()