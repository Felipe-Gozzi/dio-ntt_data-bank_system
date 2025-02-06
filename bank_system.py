def menu():
    menu = """\n
    ================ BANCO FGC ================
    Favor selecione o processo desejado:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu]Novo usuário
    [nc]Nova conta
    [lc]Listar contas
    [q] Sair
    ===========================================
    => """
    return input(menu)

def main():
    LIMITE_SAQUES_DIARIO = 3
    AGENCIA = "0001"

    saldo_atual = 0
    limite_saque = 500
    texto_extrato = ""
    numero_saques_realizados = 0
    usuarios = []
    contas = []

    while True:
        opcao_selecionada = menu()

        if opcao_selecionada == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                saldo_atual, texto_extrato = depositar(saldo_atual, valor, texto_extrato)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
            
        elif opcao_selecionada == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                
                saldo_atual, texto_extrato = sacar(
                saldo=saldo_atual,
                valor=valor,
                extrato=texto_extrato,
                limite=limite_saque,
                numero_saques=numero_saques_realizados,
                limite_saques=LIMITE_SAQUES_DIARIO,
            )
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

        elif opcao_selecionada == "e":
            exibir_extrato(saldo_atual, extrato=texto_extrato)

        elif opcao_selecionada == "nu":
            criar_usuario(usuarios)

        elif opcao_selecionada == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao_selecionada == "lc":
            listar_contas(contas)

        elif opcao_selecionada == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação de acordo com o menu.")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Crédito:\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação com erro! Informe um valor positivo!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação com erro! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação com erro! O valor do saque excede o limite máximo permitido.")
    elif excedeu_saques:
        print("Operação com erro! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Débito:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("Operação com erro! Informe um valor positivo!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizados operações hoje!" if not extrato else extrato)
    print(f"\nSaldo Atual:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

main()