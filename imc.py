peso = float(input("informe seu pesso em (kg) :"))
altura = float(input("informe sua altura em (m) :"))

imc = peso / (altura ** 2)

print("seu imc e igual a {}".format(imc))

if imc < 18.5 :
    print ("abaixo do peso")

else:
    print ("acima do peso")