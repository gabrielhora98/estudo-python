print("===== Caixa Eletrônico =====")
saldo = 1000.0
print(F"Seu saldo atual é: R$ {saldo}")

historico = []

while True:
    print("1 - Consultar saldo.")
    print("2 - Depositar.")
    print("3 - Sacar.")
    print("4 - Historico de transações.")
    print("5 - Sair.")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(F"Seu saldo atual é: R$ {saldo}")
    elif opcao == 2:
        print("Quanto deseja depositar?")
        deposito = float(input("R$: "))
        if deposito <= 0:
            print("Valor invalido. Tente novamente.")
        else:
            saldo = deposito + saldo
            historico.append(f"Depósito: R$ {deposito}")
            print(F"Seu saldo atual é: R$ {saldo}")
    elif opcao == 3:
        print("Quanto deseja sacar?")
        saque = float(input("R$: "))
        if saque <= 0:
            print("Valor invalido. Tente novamente.")
        elif saque <= saldo: 
            print("Tem certeza que deseja sacar esse valor? (S/N)")
            confirmaçao = str(input())
            if confirmaçao == "S" or confirmaçao == "s":
                saldo = saldo - saque
                historico.append(f"Saque: R$ {saque}")
                print(F"Seu saldo atual é: R$ {saldo}") 
            else:
                print("Saque cancelado.")
        else:
            print("você não tem dinheiro suficiente.")
    elif opcao == 4:
        print("Histórico de transações ")
        if historico == []:
            print("Nenhuma transação realizada.")
        else:
            for transaçao in historico:
                print(transaçao)
    elif opcao == 5:
        print("Obrigado! Volte sempre!")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        