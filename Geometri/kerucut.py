def kerucut():
    jari2 = int(input('\033[0;33mMasukkan Jari-jari Kerucut : '))
    garis_pelukis = int(input('Masukkan Garis Pelukis Kerucut : '))
    tinggi = int(input('Masukkan Tinggi Kerucut : '))
    
    phi = 3.14
    lp = lambda r,s : phi*r*(r+s)
    ls = lambda r,s : phi*r*s
    la = lambda r : phi*r*r
    
    print(f'''Luas Permukaan Kerucut : {lp(jari2,garis_pelukis)} 
Luas Selimut Kerucut : {ls(jari2,garis_pelukis)} 
Luas Alas Kerucut : {la(jari2)}''')
    
kerucut()
kerucut()
kerucut()