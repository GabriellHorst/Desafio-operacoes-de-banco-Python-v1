menu = """ 
===========================================================        
   +++++++++   ++++++++   +++     +++   +++   +++                                                                      
   +++   +++   +++  +++   ++++++  +++   +++  +++
   ++++++++    +++  +++   +++ +++ +++   ++++++
   +++   +++   ++++++++   +++  ++++++   +++  +++
   +++++++++   +++  +++   +++   +++++   +++   +++

Qual operação deseja realizar? 

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

===========================================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    
    if opcao == "1":
        print()
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print()
            print(f"Depositado o valor de R$ {valor:.2f} em sua conta.")

        else:
            print()
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        print()
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print()
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print()
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print()
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print()
            print(f"Saque de R$ {valor:.2f} relizado com sucesso.")

        else:
            print()
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print()
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print()
        print("Operação inválida, por favor selecione novamente a operação desejada.")