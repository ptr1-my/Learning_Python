detik = int(input('Detik: '))

HARI_DETIK = 60*60*24
JAM_DETIK = 60*60
# hari, jam, menit, detik
# pakai sisa bagi
hari = int(detik/HARI_DETIK)
sisa_detik = detik%HARI_DETIK
jam = int(sisa_detik/JAM_DETIK)
sisa_detik = detik % JAM_DETIK
menit = int(sisa_detik/60)
detik = (sisa_detik%60)

print(f'hari {hari}, jam {jam}, menit {menit}, detik {detik}')