tb = float(int(input("Masukkan Tinggi Badan Anda: ")))
bb = float(int(input("Masukkan Berat Badan Anda: ")))

r1 = tb-100
s10 = 10/100
r2 = s10*r1
bb_ideal = r1-r2

if (bb_ideal-2) <= bb <= (bb_ideal+2):
    print (f'Berat badan ideal')
else:
    print (f'Berat badan tidak ideal, Berat badan ideal yang seharusnya {bb_ideal}')
