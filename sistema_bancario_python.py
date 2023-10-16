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
        print("Depósito")
        valor_do_deposito = float(input("O valor a ser depositado é: R$ "))
        if valor_do_deposito > 0:
            saldo = saldo + valor_do_deposito #saldo vai receber o valor do saldo atual + o valor do depósito
            extrato = extrato + f"Depósito: R$ {valor_do_deposito:.2f}\n" #string de texto 'extrato' vai receber o valor do extrato atual + o valor do depósito
        else:
            print("O depósito precisa ser maior que zero.")

    elif opcao == "2":
        print("Saque")
        if numero_saques < LIMITE_SAQUES:
            valor_do_saque = float(input("O valor a ser sacado é: R$ "))
            if 0 < valor_do_saque <= limite and valor_do_saque <= saldo: #verifica se o valor do saque é maior que 0, se é menor ou igual ao limite definido e verifica se o valor do saque é menor ou igual ao saldo
                saldo = saldo - valor_do_saque #saldo vai receber o valor do saldo atual - o valor do saque
                extrato = extrato + f"Saque: R$ {valor_do_saque:.2f}\n" #O mesmo como visto no if else acima, vai adicionar o valor de saque + extrato dentro da string extrato, formando uma nova linha
                numero_saques = numero_saques + 1
            else:
                print("Saque acima de R$ 500.00 ou saldo insuficiente.")
        else:
            print("Limite de saques diários já foi atingido.")

    elif opcao == "3":
        print("Extrato")
        print(extrato + f"Saldo atual: R$ {saldo:.2f}") #dessa vez o saldo que será adicionado.

    elif opcao == "4":
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")
