temperatura = float(input("Informe a temperatura atual da sala :"))

if temperatura  < 25 and temperatura > 21:
    print("Esta proximo do limite")

elif temperatura <= 20 :
    print ("A temperatura esta ideal")

else:
    print ("tempetarura acima do esperado")