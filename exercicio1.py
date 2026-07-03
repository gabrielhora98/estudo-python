print("===== Caixa Eletrônico =====")
saldo = 1000.0

while True:
    print("1 - Consultar saldo.")
    print("2 - Depositar.")
    print("3 - Sacar.")
    print("4 - Sair.")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(F"Seu saldo atual é: R$ {saldo}")
    elif opcao == 2:
        print("Quanto deseja depositar?")
        deposito = float(input("R$: "))
        saldo = deposito + saldo
        print(F"Seu saldo atual é: R$ {saldo}")
    elif opcao == 3:
        print("Quanto deseja sacar?")
        saque = float(input("R$: "))
        if saque <= saldo:
            saldo = saldo - saque
            print(F"Seu saldo atual é: R$ {saldo}")
        else:
            print("você não tem dinheiro suficiente.")
    elif opcao == 4:
        print("Obrigado! Volte sempre!")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        