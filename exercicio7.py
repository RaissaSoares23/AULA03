time1 = input ("Qual o primeiro time:")
gols1 = int(input (f"Quantos gols:{time1}"))
time2 = input ("Qual o segundo time:")
gols2 = int(input (f"Quantos gols:{time2}"))

if gols1 > gols2:
    print("Vencedor time 1")
else:
    if gols1 == gols2:
        print ("Empate")
    else:
     print ("Vencedor time 2")

