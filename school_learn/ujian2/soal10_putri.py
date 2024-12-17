k = input("Masukkan kalimat: ")  

def hasil(kalimat):  
    kalimat = kalimat.strip()  

    if kalimat.endswith('.'):  
        kalimat = kalimat[:-1] 
    elif kalimat.endswith('!'):  
        kalimat = kalimat[:-1]    
    if not kalimat.lower().startswith("apakah"):  
        kalimat = "Apakah " + kalimat     
    kalimat += '?'  

    return kalimat   
hasil = hasil(k) 

# def hasil(kalimat):  
#     kalimat = kalimat.strip()
    
#     if not kalimat.lower().startswith("apakah"):  
#         kalimat = "Apakah " + kalimat   
#     return kalimat[:-1] + '?' if kalimat[-1] not in '?' else kalimat 

# print(hasil(input("Masukkan kalimat: "))) 