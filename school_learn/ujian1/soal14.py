huruf = input("Masukkan Huruf : ")

if huruf in "aiueoAIUEO":
    print (f'Huruf {huruf} merupakan Huruf VOKAL')
elif huruf.isdigit():
    print ("ini merupakan angka")
else:
    print (f'Huruf {huruf} merupakan Huruf KONSONAN')