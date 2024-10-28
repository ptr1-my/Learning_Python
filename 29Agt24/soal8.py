p = float(input('Masukkan nilai pixel: '))

def n_pixel(p):
    if p > 255:
        return 255
    elif p < 0:
        return 0
    else:
        return p
    
print(f'Nilai {p} = {n_pixel(p)} pixel')