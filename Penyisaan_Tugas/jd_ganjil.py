n = int(input("Masukan Nilai : "))

deret_ganjil = [i for i in range(1, n+1) if i % 2 != 0]
j = sum(deret_ganjil)

print(f"Deret Nilai Ganjil : {deret_ganjil} \nJumlah Deret Bilangan Ganjil : {j}")