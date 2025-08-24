menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Saldo realizado com sucesso!")

        else:
            print("Operação Inválida! O valor informado não foi aceito.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida! Saldo menor que o valor solicitado!")
        
        elif excedeu_limite:
            print("Operação inválida! Limite excedido: tente um valor menor!")

        elif excedeu_saques:
            print("Operação inválida! Você já atingiu o limite diário de saques!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        
        else:
            print("Operação falhou! O valor informado é inválido!")
    
    elif opcao == "3":
        print("\n--EXTRATO--")
        if not extrato:
            print("Não foram realizadas movimentaçãoes!")
        else:
            print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
        print("--------")

    elif opcao == "4":
        print("Obrigado por utilizar o nosso sistema. Até mais!")
        break

    else:
        print("Operação inválida! Por favor selecione uma opção válida!")