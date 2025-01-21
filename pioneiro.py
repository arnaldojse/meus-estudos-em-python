
def ler_numero(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Erro: entrada não é um número.")

maça = ler_numero("quantas maças foram vendidadas : ")
banana = ler_numero("quantas bananas foram vendidas : ")

if banana > maça :
    print("foram vendidas mais bananas que maças")

elif banana < maça :
    print("foram vendidas mais maçãs que bananas")

else:
    print ("foi vendida a mesma quantidade de ambos")