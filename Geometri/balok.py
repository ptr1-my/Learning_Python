def balok():
    panjang = int(input('\033[0;34mMasukkan Panjang Balok : '))
    lebar = int(input('Masukkan Lebar Balok : '))
    tinggi = int(input('Masukkan Tinggi Balok : '))
    
    lp = lambda p,l,t: 4*(p+l+t)
    k = lambda p,l,t: 2*((p*l)+(p*t)+(l*t))
    
    print(f'Luas Permukaan Balok : {lp(panjang,lebar,tinggi)} \nKeliling : {k(panjang,lebar,tinggi)}')
    
balok()
balok()
balok() 