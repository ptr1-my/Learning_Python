def lingkaran():
    jari2 = int(input('\033[0;32mMasukkan Jari-Jari : '))
    
    phi = 3.14
    luas = lambda r,x: phi*jari2*jari2
    keliling = lambda r,x: 2*jari2*phi
    
    print(f'Luas Lingkaran : {luas(jari2,phi)} cm2 \nKeliling Lingkaran {keliling(jari2,phi)} cm')
    
lingkaran()
lingkaran()
lingkaran()