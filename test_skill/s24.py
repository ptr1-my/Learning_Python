def hasil(kalimat):  
    kalimat = kalimat.strip()
    
    if not kalimat.lower().startswith("apakah"):  
        kalimat = "Apakah " + kalimat   
    return kalimat + '?' if kalimat not in '?' else kalimat 

print(hasil(input("Masukkan kalimat: "))) 