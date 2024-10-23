def persegi():
    sisi = int(input('\033[0;31mMasukkan Sisi : '))
    luas = lambda s: s*s
    keliling = lambda s: 4*s
    
    print(f'Luas Persegi : {luas(sisi)} cm2 \nKeliling Persegi : {keliling(sisi)} cm')
    
persegi()
persegi()
persegi()
