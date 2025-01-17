while True:
    nome = input("Informe seu nome de usuario :")
    senha = input("Informe sua senha :")

    if len(nome) < 5:
        print("O nome deve ter pelomenos 10 caracteres")
        continue

    if len(senha) < 8:
        print("A senha deve ter no minimo 8 carcteres")
        continue

    print("Cdastro feito com sucesso")
    break