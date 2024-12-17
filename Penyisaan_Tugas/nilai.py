nilai = []
jml = int(input('Jumlah data yang akan di input: '))

for i in range(jml):
    nilai.append(float(input(f'Nilai ke-{i+1} : ')))
    
    # perhitungan data list
    total=max=min = 0
    for data in nilai:
        total+= data
        if data > max:
            max = data
            
        min = data
        if data < min:
            min = data
            
    print(total)
    print(f'Rata - rata : {total/jml}')
    print(f'Nilai Terbesar : {max}')
    print(f'Nilai Terkecil : {min}')