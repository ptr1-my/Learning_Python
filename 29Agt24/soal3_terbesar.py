# mengurutkan nilai terbesar ke terkecil

a = int(input("Masukkan Bilangan Bulat Pertama: "))
b = int(input("Masukkan Bilangan Bulat Kedua: "))
c = int(input("Masukkan Bilangan Bulat Ketiga: "))

if a>b and b>c:
    print (f'Bilangan bulat dari Terbesar - Terkecil : {a},{b},{c}')
elif a>c and c>b:
    print (f'Bilangan bulat dari Terbesar - Terkecil : {a},{c},{b}')
elif b>a and a>c:
    print (f'Bilangan bulat dari Terbesar - Terkecil : {b},{a},{c}')
elif b>c and c>a:
    print (f'Bilangan bulat dari Terbesar - Terkecil : {b},{c},{a}')
elif c>a and a>b:
    print (f'Bilangan bulat dari Terbesar - Terkecil : {c},{a},{b}')
elif c>b and b>a:
    print (f'Bilangan bulat dari Terbesar - Terkecil : {c},{b},{a}')