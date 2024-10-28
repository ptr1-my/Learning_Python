# PERCEPATAN RATA RATA
# a = V2 - V1 / T2 - T1

print ("\033[1;35m============================")
print ("\033[1;37mPERCEPATAN RATA-RATA")
print ("\033[1;35m============================")

v1 = float(input("\033[1;36mMasukan nilai v1: "))
v2 = float(input("Masukan nilai v2: "))
t1 = float(input("Masukan nilai t1: "))
t2 = float(input("Masukan nilai t2: "))

percepatan = v2 - v1 / t2 - t1

print ("\033[1;31m----------------------------")
print (f'Perecepatan rata rata ialah :{round(percepatan,2)} m/s2')
print ("----------------------------")

