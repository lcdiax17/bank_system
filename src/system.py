'Sistema bancário básico'

menu_de_operacao = """
    [0] Depositar
    [1] Sacar
    [2] Extrato Bancário
    [3] Sair
"""

LIMITE_DE_SAQUES_DIARIO = 3
numero_de_saques = 0
limite_por_saque = 500
saldo = 0
extrato = ""


while True:

    opcao_selecionada = input(menu_de_operacao)

    if opcao_selecionada == 0:

        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}"

        else:
            print("Erro! Valor depositado é invalído ou insuficiente")

    elif opcao_selecionada == 1:

        valor = float(input("Digite o valor que deseja sacar: "))

        limite_de_saque_excedido = valor > limite_por_saque
        valor_do_saldo_excedido = valor > saldo
        saques_excedidos = numero_de_saques > LIMITE_DE_SAQUES_DIARIO

        if limite_de_saque_excedido:
            print("Operação invalida!, limite de saque indisponivel para sua categoria")

        elif valor_do_saldo_excedido:
            print("Operação invalida! Saldo insuficiente")

        elif saques_excedidos:
            print("Operação invalida! Número de saques do dia atingiu seu limite!")

        elif valor > 0:
            saldo - + valor
            numero_de_saques += 1
            extrato += f"Saque: R$ {valor:.2f}"

    elif opcao_selecionada == 2:

        for tipo in extrato:
            if tipo == "Deposito: " in extrato:
                print(f"Extrato de depositos: \n {tipo}")
            elif tipo == "Saque: " in extrato:
                print(f"Extrato de saques: \n {tipo}")
            else:
                print(f"Extrato de saques: {extrato}")

    elif opcao_selecionada == 3:
        break

    else:
        print("Selecione uma opção valida!")
