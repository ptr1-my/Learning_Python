def tabung():
    jari2 = int(input('\033[0;31mMasukkan Jari-Jari Tabung : '))
    tinggi = int(input('Masukkan tinggi Tabung : '))
    
    phi = 3.14
    la =  lambda r: phi*r*r
    k = lambda r: 2*phi*r
    ls = lambda r,t: 2*r*t
    lp = lambda r,t: 2*phi*r*(r+t)
    
    print(f'''Luas Permukaan Tabung : {lp(jari2,tinggi)}
Keliling Tabung : {k(jari2)}
Luas Selimut Tabung : {ls(jari2,tinggi)}
Luas Alas : {la(jari2)}''')
    
tabung()
tabung()
tabung()