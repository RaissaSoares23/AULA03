g= 5.8
e=4.9
Combustivel = input ("Qual tipo de combustivel você abasteceu:\n"
                     "g para gasolina\n"
                     "e para etanoln")
litros = float (input ("Quantos litros você abasteceu:"))

if Combustivel == "g":
    total = litros*g
else:
    total = litros*e

print (f"você gastou: R${total}")




