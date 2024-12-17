nu = int(input("Masukkan nilai uang rupiah : "))

p1 = int(nu/1000)
sisa = (nu%1000)
p2 = int(sisa/500)
sisa = (sisa%500)
p3 = int(sisa/100)
sisa = (sisa%100)
p4 = int (sisa/50)
sisa = (sisa%50)
p5 = int (sisa/25)

print (f''' {nu} setara dengan :
{p1} buah pecahan Rp.1000
{p2} buah pecahan Rp.500
{p3} buah pecahan Rp.100
{p4} buah pecahan Rp.50
{p5} buah pecahan Rp.25''')