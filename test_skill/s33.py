
nama = [None] * 5
pembayaran = [0] * 5

for i in range(5):
    print(f"Data siswa ke-{i + 1}:")
    nama[i] = input("Masukkan nama siswa: ")
    pembayaran[i] = int(input("Masukkan jumlah pembayaran UDT: "))

print("\nRekapan Pembayaran:")
total_pembayaran = 0
for i in range(5):
    print(f"{i + 1}. {nama[i]:<15}: {pembayaran[i]}")
    total_pembayaran += pembayaran[i]

print("\nTotal Pembayaran Semua Siswa:", total_pembayaran)
