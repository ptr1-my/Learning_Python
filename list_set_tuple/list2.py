data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frekuensi = {item: data.count(item) for item in set(data)}
print("Frekuensi setiap elemen:", frekuensi)