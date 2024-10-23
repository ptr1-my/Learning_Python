def trapesium():
    a = int(input('\033[0;33mMasukkan Sisi AB : '))
    b = int(input('Masukkan Sisi BC : '))
    c = int(input('Masukkan Sisi CD : '))
    d = int(input('Masukkan Sisi DA : '))
    tinggi = int(input('Masukkan Tinggi : '))
    
    luas = lambda a,c,t: 0.5*t*(a+c)
    keliling = lambda a,b,c,d: a+b+c+d
    
    print(f'Luas Jajar Genjang : {luas(tinggi,a,c)} cm2 \nKeliling : {keliling(a,b,c,d)} cm')
    
trapesium()
trapesium()
trapesium()