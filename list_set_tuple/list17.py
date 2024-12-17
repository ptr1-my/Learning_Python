kalimat1 = "saya suka belajar python"
kalimat2 = "python sangat menyenangkan untuk belajar"

kata1 = set(kalimat1.split())
kata2 = set(kalimat2.split())

sama = kata1 & kata2
print("Kata yang sama:", sama)