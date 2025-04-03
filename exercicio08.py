g= 5.8
e=4.9
total= 0
Combustivel = input ("Qual tipo de combustivel você abasteceu:\n"
                     "g  para gasolina\n"
                     "e para etanoln")
litros = float (input ("Quantos litros você abasteceu:"))

if Combustivel == "g" or Combustivel == "G":
    total = litros*g

elif Combustivel == "e" or Combustivel == "E":
    total = litros*e
else:
    print ("Tipo de combustivel invalido!")

print (f"você gastou: R${total}")




