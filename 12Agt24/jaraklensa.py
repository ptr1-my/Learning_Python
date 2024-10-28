# d = f_ob + 4f_p + f_ok

print ("\033[1;34m============================")
print ("\033[0,33mMENGHITUNG JARAK LENSA OBEJEKTIF DAN LENSA OKULER")
print ("\033[1;34m============================")

f_ob = float(input("\033[0;32mMasukan Lensa Objektif: "))
f_p = float(input("Masukan Lensa Pembalik: "))
f_ok = float(input("Masukan Lensa Okuler: "))

#  jarak lensa objektif
d = f_ob + (4*f_p) + f_ok

print(f"\033[1;33mPanjang Teropong : {round(d,2)}")




