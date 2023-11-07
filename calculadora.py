def value():
    while True:
        entrada = input("Digite um número(ou '0' para sair): ")
        if entrada == '0':
            return None
        entrada = entrada.replace(",", ".")
        try:
            numero = float(entrada)
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")


while True:
    print("Opcões:")
    print("Digite '1' para adição")
    print("Digite '2' para subtração")
    print("Digite '0' para sair")

    escolha = input("Escolha uma opção (1/2/0): ")

    if escolha == '0':
        print("Saindo da aplicação")
        break
    elif escolha == '1':
        value1 = value()
        value2 = value()
        if value1 is not None and value2 is not None:
            resultado = value1 + value2
            print("Resultado: ", resultado)
    elif escolha == '2':
        value1 = value()
        value2 = value()
        if value1 is not None and value2 is not None:
            if value1 >= value2:
                resultado = value1 - value2
                print("Resultado: ", resultado)
            else:
                print("O primeiro valor deve ser maior que o segundo")
        else:
            print("Valores inválidos para subtração.")
    else:
        print("Opção inváçida. Escolha 1, 2 ou 0 para sair.")
        