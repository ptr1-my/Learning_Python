o1 = float(input("Masukkan Operand 1: "))
opr = input("Masukkan operator (+, -, *, /) : ")
o2 = float(input("Masukkan Operand 2: "))

if opr == '+':
    print(f'Hasil : {o1 + o2} (yaitu {o1}{opr}{o2})')
elif opr == '-':
    print(f'Hasil : {o1 - o2} (yaitu {o1}{opr}{o2})')
elif opr == '*':
    print(f'Hasil : {o1 * o2} (yaitu {o1}{opr}{o2})')
elif opr == '/':
    print(f'Hasil : {o1 / o2} (yaitu {o1}{opr}{o2})')