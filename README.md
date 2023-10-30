# Calculadora-PDI

Objetivo do Código:
	Este código Python tem como objetivo criar um programa que permite ao usuário realizar operações matemáticas.

Estrutura do Código:
  	O código é composto por três funções e um loop while que executa o programa principal:

  	Função adicao(value1, value2):
		Esta função recebe dois valores como argumentos e retorna a soma desses valores.
	
  	Função subtracao(value1, value2):
		Esta função também recebe dois valores como argumentos.
		Primeiro, ela verifica se value1 é menor que value2. Se for o caso, exibe uma mensagem de erro informando que o primeiro valor deve ser maior que o segundo.
		Caso contrário, ela retorna a subtração de value1 por value2.
	
  	Loop while:
		O loop while é usado para criar o menu interativo e controlar o fluxo do programa.
		A cada iteração do loop, o programa exibe as opções disponíveis:
		'1' para adição.
		'2' para subtração.
		'0' para sair.
   		O usuário é solicitado a escolher uma opção digitando '1', '2' ou '0'.
    	Se o usuário escolhe '0', o programa exibe "Saindo da aplicação" e encerra.
	  	Se o usuário escolhe '1' ou '2', o programa solicita que ele insira dois valores numéricos.
		Após obter os valores, o programa chama a função correspondente (adição ou subtração) e exibe o resultado.
    	Se o usuário escolher uma opção inválida (diferente de '1', '2' ou '0'), o programa informa que a escolha é inválida e oferece uma nova chance de escolha.
  
Manipulação de Erros:
	O código lida com alguns possíveis erros:
	Se o usuário escolher subtrair e o primeiro valor for menor que o segundo, uma mensagem de erro é exibida.
	Se o usuário escolher uma opção inválida, ele é informado e pode escolher novamente.
	Isso resume a estrutura e o funcionamento do código. Ele fornece uma maneira simples para o usuário realizar operações de adição e subtração e oferece mensagens de erro quando as entradas são inválidas. O programa continua em execução até que o usuário escolha sair.
