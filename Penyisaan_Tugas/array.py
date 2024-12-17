# yang dalam kurung namanya element
buah = ['apel','mangga','melon','anggur','manggis']
# yang dalam kurung namanya indeks
print (buah[1])
# untuk mengubah buah
buah[2] = 'rambutan'
# untuk menambahkan buah
buah.append ('lemon')
print (buah)

# memunculkan data sebanyak jumlah list
for data in buah:
    # kalo pakai id hasinya bakal id/ angka
    # kalo ga pake id akan muncul nya buah yang sejajar 
    print(id(data))