d1 = int(input("Days 1 : "))
m1 = int(input("Month 1 : "))
y1 = int(input("Year 1 : "))
d2 = int(input("Days 2 : "))
m2 = int(input("Month 2 : "))
y2 = int(input("Year 2 : "))

tgl1 = (y1*365)+(m1*30)+d1
tgl2 = (y2*365)+(m2*30)+d2

if tgl1 > tgl2:
    selisih = tgl1-tgl2
elif tgl2 > tgl1:
    selisih = tgl2-tgl1
    
tahun = int(selisih/365)
sisa_hari = int(selisih%365)
bulan = int(sisa_hari/30)
hari = int(sisa_hari%30)

print (f'Selisih Dari Kedua Tanggal : {tahun} tahun, {bulan} bulan, {hari} hari')
