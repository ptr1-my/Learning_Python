def persegi_panjang():
    panjang = int(input('\033[0;33mMasukkan Panjang : '))
    lebar = int(input('Masukkan Lebar : '))
    
    luas = lambda p,l: p*l
    keliling = lambda p,l: 2*p*l
    
    print(f'Luas Persegi Panjang : {luas(panjang,lebar)} cm2 \nKeliling Persegi Panjang : {keliling(panjang,lebar)} cm')
    
persegi_panjang()
persegi_panjang()
persegi_panjang()