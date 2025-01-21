nota1 = float(input("nforme sua primeira nota :"))
nota2 = float(input("Informe sua segunda nota :"))
nota3 = float(input("Informe sua terseira nota :"))

total = nota1 + nota2 + nota3
media = total / 3

print("sua primeir nota foi de {}, sua segunda foi {}, ja sua terceira foi de {}".format(nota1, nota2, nota3))
print("então sua media fica em {}".format(media))

if media >= 7:
    print("parabens você amaçou a prova ")

elif media >= 9:
    print("QUE ISSO AMIGO, deixa o professor brincar também ")

else:
    print("Calma, na proxima você consegue ")      