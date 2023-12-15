print(f"Bem-vindo ao nosso Sistema Bancário")
print("_" * 35)

menu = """
        Qual operação deseja realizar em nosso atendimento?

            [d] - Depositar
            [s] - Sacar
            [e] - Extrato
            [q] - Sair

=> Sua opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\nQuanto você deseja depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito de R$ {valor:.2f} concluído com sucesso!")

        else:
            print("\nOperação falhou, pois o valor está inválido!")
    
    elif opcao == "s":
        valor = float(input("\nQuanto você deseja sacar? "))
        print(f"\nSaque de R$ {valor:.2f} concluído com sucesso!")

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("\nFalha! Saldo insuficiente!")
        
        elif excedeu_limite:
            print("\nFalha! Valores acima de R$ 500,00 não poderão ser sacados!")
        
        elif excedeu_saques:
            print("\nFalha! Número de saques excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("\nFalha! O valor informado é inválido!")
    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        print("\nObrigado e até logo!")
        break

    else:
        print("\nPor favor, selecione um valor válido!")
