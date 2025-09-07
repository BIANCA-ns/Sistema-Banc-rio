def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Saldo realizado com sucesso!")
        return saldo, extrato
    
    else:
        print("Operação Inválida! O valor informado não foi aceito.")
        return saldo, extrato




def sacar(*, valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação inválida! Saldo menor que o valor solicitado!")
        return saldo, extrato, numero_saques
            
    elif excedeu_limite:
        print("Operação inválida! Limite excedido: tente um valor menor!")
        return saldo, extrato, numero_saques
            
    elif excedeu_saques:
        print("Operação inválida! Você já atingiu o limite diário de saques!")
        return saldo, extrato, numero_saques
            
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        return saldo, extrato, numero_saques
            
    else:
        print("Operação falhou! O valor informado é inválido!")
        return saldo, extrato, numero_saques




def extrato(saldo, /, *, extrato):
    print("\n--EXTRATO--")
    if not extrato:
        print("Não foram realizadas movimentaçãoes!")

    else:
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    
        print("--------")




def criar_usuario(usuarios):
    cpf = input("Informe o seu cpf: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro! Este cpf já está cadastrado.")
            return
    
    nome = input("Informe o seu nome: ")
    data_nascimento = input("Informe a sua das de nascimento: ")
    logradouro = input("Informa o seu logradouro: ")
    numero = input("Informe o número do endereço: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe o estado: ")

    usuario = {
        "cpf": cpf, "nome": nome, "data_nascimeto": data_nascimento, 
        "endereco":{"logradouro": logradouro, "numero": numero, "cidade": cidade, "estado": estado,
        }
    }
    return usuario




def criar_conta(agencia, usuario):
    numero_conta = len(contas) + 1

    conta = {
        "agencia": agencia, "numero": numero_conta, "usuario": usuario
    }
    return conta

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return 




menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastro de usuário
[5] Cadastro de conta
[6] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = 0001


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)



    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(valor=valor, saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)



    elif opcao == "3":
        extrato(saldo, extrato=extrato)



    elif opcao == "4":
        novo_usuario = criar_usuario(usuarios)
        if novo_usuario:
            usuarios.append(novo_usuario)



    elif opcao == "5":
        cpf_input = input("Informe o seu CPF para criar a conta: ")
        usuario = filtrar_usuario(cpf_input, usuarios)
        if usuario:
            nova_conta = criar_conta(AGENCIA, usuario)
            if nova_conta:
                contas.append(nova_conta)
                print("Conta criada com sucesso!")
        else:
            print("Erro! Usuário não encontrado.")



    elif opcao == "6":
        print("Obrigado por utilizar o nosso sistema. Até mais!")
        break

    else:
        print("Operação inválida! Por favor selecione uma opção válida!")