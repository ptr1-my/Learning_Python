# Membaca Nomor Bulan, Nomor Tahun, dan Jumlah hari

def j(bulan, tahun):
    h = [31, 28, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]

    def is_kabisat(t):
        return (t % 4 == 0 and t % 100 != 0) or (t % 400 == 0)

    if b < 1 or b > 12:
        return "Buan tidak tersedia"

    j = h [b - 1]
    if b == 2 and is_kabisat(tahun):
        j = 29
        
    return j

try:
    b = int(input('Masukkan Nomor Bulan 1-12 : '))
    t = int(input('Masukkan Tahun : '))
    print(f'jumlah hari dalam bulan {b} tahun {t} adalah {j(b, t)}')
    
except:
    print("Input tidak valid, harap masukkan angka yg benar")

