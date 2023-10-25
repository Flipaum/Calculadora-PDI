def adicao(value1, value2):
    return value1 + value2

def subtracao(value1, value2):
    if value1 < value2:
        print("Digite um valor maior que o segundo numero")
    else: 
        return value1 - value2

while True:
    print("Opções:")
    print("Digite '1' para adição")
    print("Digite '2' para subtração")
    print("Digite '0' para sair")
    
    escolha = input("Escolha uma opção (1/2/0): ")

    if escolha == '0':
        print("Saindo da aplicação")
        break

    value1 = float(input("Digite o valor primario: "))
    value2 = float(input("Digite o valor secundario: "))

    if escolha == '1':
        print("Resultado: ", adicao(value1, value2))
    elif escolha == '2':
        resultado = subtracao(value1, value2)
        if resultado is not None:
            print("Resultado da subtração:", resultado)
    else:
        print("Opção inválida. Escolha 1, 2 ou 0 para sair.")