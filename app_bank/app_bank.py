menu = '''
--- BEM VINDO A APP BANK ---

Escolha a operação que deseja:

[d] DEPOSITO
[s] SAQUE
[e] EXTRATO
[q] SAIR

----------------------------
=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do Depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("A operação NÃO pode ser concluida! \nO valor informado é invalido.")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("A operação NÃO pode ser concluida! \nVocê não possui saldo suficiente para a operação.")
        elif excedeu_limite:
            print("A operação NÃO pode ser concluida! \nO valor do saque excede o limite.")
        elif excedeu_saques:
            print("A operação NÃO pode ser concluida! \nNúmero máximo de saque diários foi excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("A operação NÃO pode ser concluida! \nO valor informado é inválido")
    
    elif opcao == "e":
        print("\n################## EXTRATO ##################")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("#############################################")
        
    elif opcao == "q":
        print("Sessão encerrada. \nObrigado por utilizar nosso app!")
        break
    
    else:
        print("Operação Inválida. \nPor gentileza selecione novamente a operação deseja.")
