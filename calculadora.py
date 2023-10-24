def adicao(value1, value2):
    return value1 + value2

def subtracao(value1, value2):
    return value1 - value2

while True:
    print("Opções:")
    print("Digite '1' para adição")
    print("Digite '2' para subtração")
    print("Digite '0' para sair")
    
    escolha = input("Escolha uma opção (1/2/0): ")

    value1 = float(input("Digite o valor primario: "))
    value2 = float(input("Digite o valor secundario: "))

    if escolha == '5':
        print("Saindo da aplicação")
        break

    if escolha == '1':
        print("Resultado: ", adicao(value1, value2))
    elif escolha == '2':
        print("Resultado: ", subtracao(value1, value2))
