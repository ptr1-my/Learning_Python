mapel = input("Mata Pelajaran : ")
uas = int(input("Masukkan Nilai Uas : "))
tugas = int(input("Masukkan Nilai Tugas : "))

n = uas+tugas
r = n/2

if r >= 85 :
    print ("Grade A")
elif r >= 70 and r < 85 :
    print ("Grade B")
elif r >= 60 and r < 70 :
    print("Grade C")
elif r <= 59 :
    print("Grade D")
