Looping For

#  Cerdas ke samping
for i in range(3):
    print('Cerdas', end=' ')
    
# Cerdas ke bawah
for i in range(3):
    print('Cerdas')
    
# ABCD Cerdas ke bawah
    for w in ('ABCD'): 
        # kalo string berarti ga pake range
    print(w,'. Cerdas')
    
# 1 2 3 4 5 = 15 ke samping
total = 0

for n in range(1, 6):
    total += n
    if n != 5:
        # print 1 - 4
        print(f'{n} ', end=' ')
    else:
        # print 5 dan total (15)
        print (f'{n} = {total}')

# 1+2+3+4+5 = 15 ke samping
total = 0

for n in range(1, 6):
    total += n
    if n != 5:
        # print 1 - 4
        print(f'{n} +', end=' ')
    else:
        # print 5 dan total (15)
        print (f'{n} = {total}')