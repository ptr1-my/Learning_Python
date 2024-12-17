huruf = input('Masukkan Huruf : ')

if huruf in 'AIUEOaiueo':
    print(f'{huruf} adalah huruf vokal')
elif huruf.isdigit():
    print('Ini merupakan Angka')
else:
    print(f'{huruf} adalah huruf konsonan')