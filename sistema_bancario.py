menu = """
     ***MENU***
     [d] - Deposito
     [s] - Saque 
     [e] - Extrato
     [q] - Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        deposito = float(input("Informe o valor do seu deposito: "))
        if deposito > 0:
          saldo += deposito
          extrato += f"Deposito de R${deposito}\n"
        else:
            print("Valor invalido")
         

    
    elif opcao == "s":
        if numero_saque == LIMITE_SAQUE:
            print("Limite diario de saques atingido")
        else:
            print("Saque")
        saque = float(input("Digite o valor do seu saque: "))
        if saque < 0:
            print("Valor invalido!")
        elif saque > 500:
            print("O limite maximo para saque é R$500")
        elif saque > saldo:
            print("Voce não possui saldo suficiente")
        else:
            saldo += saque
            numero_saque += 1
            saques_restantes = (LIMITE_SAQUE - numero_saque)
            extrato += f"Saque de : R${saque}.\n"
            print(f"Voce ainda possui : {saques_restantes} saques")
        

    
    elif opcao == "e":
        print("*****EXTRATO*****")
        if extrato == "":
            print("Não foram realizadas movimentações")
        else:
            print(extrato)
            print(f"Saldo: R${saldo} ")
    
    elif opcao == "q":
        break

    else:
        print("Operação Invalida, pr favor selecione novamente a operação desejada")