nilai = float(input('Masukkan Nilai Siswa Untuk Melihat Grade : '))

if nilai >= 90 :
    print(f'Siswa dengan nilai : {nilai} MEndapatkan Grade : A')
elif nilai >= 80 :
    print(f'Siswa dengan nilai : {nilai} MEndapatkan Grade : B')
elif nilai >= 70 :
    print(f'Siswa dengan nilai : {nilai} MEndapatkan Grade : C')
elif nilai >= 60 :
    print(f'Siswa dengan nilai : {nilai} MEndapatkan Grade : D')
else:
    print(f'Siswa dengan nilai : {nilai} MEndapatkan Grade : E')