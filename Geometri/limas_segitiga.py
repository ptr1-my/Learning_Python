def limas_segitiga():
    tinggi = int(input('\033[0;36mMasukkan Tinggi : '))
    alas = int(input('Masukkan Alas : '))
    miring = int(input('Masukkan Sisi Miring : '))
    
    lp = lambda a,b,c: (1/2*(a*b))+(3/2*(b*c))
    
    print(f'Luas Pemukaan Limas Segitiga : {lp(tinggi,alas,miring)}')
    
limas_segitiga()