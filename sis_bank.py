menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("❌ Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("❌ Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("❌ Operação falhou! O valor do saque excede o limite de R$ 500.00.")
        elif excedeu_saques:
            print("❌ Operação falhou! Limite de 3 saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("❌ Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n=========== EXTRATO BANCÁRIO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("========================================")

    elif opcao == "q":
        print("✅ Obrigado por usar nosso sistema bancário. Até logo!")
        break

    else:
        print("❌ Operação inválida! Tente novamente.")
