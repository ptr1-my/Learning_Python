def bola():
    jari2 = int(input('\033[0;35mMasukkan jari-jari : '))
    
    r2 = jari2*jari2
    phi = 3.14
    luas = lambda r: 4*phi*r2
    keliling = lambda r: 4/3*phi*r2
    
    print(f'Luas Permukaan Lingkaran : {luas(jari2)} cm2 \nKeliling : {keliling(jari2)} cm')
    
bola()
bola()
bola()