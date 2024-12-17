def a(c):
    return ord(c) - ord('0')
def b(c):
    if '0' <= '9':
        return ord(c) - ord('0')
    else:
        return -99
    
c = int(input('Masukkan Karakter Digit: '))

print ('Hasil Konversi A:', a(c))
print ('Hasil Konversi B:', b(c))
