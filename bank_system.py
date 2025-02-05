menu = """
================ BANCO FGC ================
Favor selecione o processo desejado:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
===========================================
=> """

saldo_atual = 0
limite_saque = 500
texto_extrato = ""
numero_saques_realizados = 0
LIMITE_SAQUES_DIARIO = 3

while True:

    opcao_selecionada = input(menu)

    if opcao_selecionada == "1":

        try:
            valor = float(input("Digite o valor para depósito: "))
            if valor > 0:
                saldo_atual += valor
                texto_extrato += f"Crédito: R$ {valor:.2f}\n"
            else:
                print("Operação com erro! Informe um valor positivo!")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    elif opcao_selecionada == "2":
        try:
            valor = float(input("Digite o valor para saque: "))

            excedeu_saldo = valor > saldo_atual
            excedeu_limite = valor > limite_saque
            excedeu_saques = numero_saques_realizados >= LIMITE_SAQUES_DIARIO

            if excedeu_saldo:
                print("Operação com erro! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação com erro! O valor do saque excede o limite máximo permitido.")
            elif excedeu_saques:
                print("Operação com erro! Número máximo de saques diários excedido.")
            elif valor > 0:
                saldo_atual -= valor
                texto_extrato += f"Débito: R$ {valor:.2f}\n"
                numero_saques_realizados += 1
            else:
                print("Operação com erro! Informe um valor positivo!")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    elif opcao_selecionada == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizados operações hoje!" if not texto_extrato else texto_extrato)
        print(f"\nSaldo Atual: R$ {saldo_atual:.2f}")
        print("==========================================")

    elif opcao_selecionada == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação de acordo com o menu.")