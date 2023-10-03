D = { "Alface" : 0.45,
      "Batata" : 1.20,
      "Tomate" : 2.30,
      "Feijão" : 5.50 }

Dici = {"Maycon" : (20, 30,1.15),
        "Mariana" : (10,15,1.8)}

#print(f"Preço do Feijão R${D['Feijão']:.2f}")
#print(D)
#D["Cebola"] = 1.35
#print(D)
print(Dici["Maycon"][2])

if Dici["Maycon"][1] == 30:
    print("Certo")