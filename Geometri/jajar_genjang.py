def jajar_genjang():
    alas = int(input('\033[0;30mMasukkan Alas : '))
    tinggi = int(input('Masukkan Tinggi : '))
    
    luas = lambda a,t: a*t
    keliling = lambda a,t: 2*(a*t)
    
    print(f'Luas Jajar Genjang : {luas(alas,tinggi)} cm2\nKelilig Jajar Genjang : {keliling(alas,tinggi)} cm')
    
jajar_genjang()
jajar_genjang()
jajar_genjang()