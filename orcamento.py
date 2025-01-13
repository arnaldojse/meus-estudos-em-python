total = 0.0  # Variável para acumular o total das despesas

while True:
    entrada = input("Quais foram as despesas do mês? (se quiser parar, digite 'sair'): ")
    
    if entrada == "sair":  # Verifica se o usuário quer parar
        break  # Sai do loop
    
    try:
        despesas = float(entrada)  # Converte a entrada para float
        total += despesas  # Adiciona ao total
    except ValueError:  # Se a entrada não for um número válido
        print("Entrada inválida! Digite um número ou 'sair' para parar.")

print("Finalizando cálculo... Aguarde...")
print(f"Suas despesas mensais foram: R$ {total:.2f}")