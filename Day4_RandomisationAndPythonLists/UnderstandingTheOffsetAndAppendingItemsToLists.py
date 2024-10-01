#We're learning List today hahaha
Indonesia = ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Banten", "DKI Jakarta", "DI Yogyakarta", "Aceh",
             "Sumatera Utara", "Sumatera Barat", "Sumatera Selatan", "Jambi", "Lampung", "Bengkulu", "Bali"]
print(len(Indonesia))
print(Indonesia[3])
print(Indonesia[-2]) #to read from behind
print(Indonesia)
Indonesia[1] = "Jateng" #to change value/item Jawa Tengah to Jateng
print(Indonesia)
Indonesia.append("Kalimantan  Utara") #to add one value/item inside the List.
print(Indonesia)
Indonesia.extend(["Kalimantan Barat", "NTT"]) #to add more than one value/item to the List.
print(Indonesia)
