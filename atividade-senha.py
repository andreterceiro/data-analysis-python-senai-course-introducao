# Avançado:
# 1)Foi solicitado pelo Banco UNIFAFIBE que você criasse um sistema
# para os seus caixas eletrônicos. O sistema deve ser feito seguindo as instruções
# abaixo:

# O cliente deverá inserir o número da conta e uma senha que
# deve ser apenas os números do seu CPF, após isso o sistema deve exibir o saldo
# em conta e um menu com 3 opções de operações. Considere que todos os clientes têm
# um saldo inicial de R$ 1000.00.

# Opção 1: Saque:
# O cliente deverá informar a quantia que deseja sacar, o sistema
# deve pedir para que ele digite novamente a senha informada no começo do programa.
# Caso a senha esteja correta, mostre o novo saldo. O cliente não pode sacar mais
# do que o saldo na conta, caso ele tente, devolva: “VALOR INVALIDO”. Caso a
# senha esteja incorreta informe: “SENHA INCORRETA”.

# Opção 2: Deposito:
# O cliente deverá informar a quantia que deseja depositar, o
# sistema deve pedir para que ele digite novamente a senha informada no começo do
# programa. Caso a senha esteja correta, mostre o novo saldo. Caso a senha esteja
# incorreta informe: “SENHA INCORRETA”.

# Opção 3: Sair
# O programa encerra.

OPCAO_SAQUE = "1"
OPCAO_DEPOSITO = "2"
OPCAO_SAIR = "3"
saldo = 1000.0

while True:
    numero_conta = input("Por favor insira o número da conta: ")
    if not numero_conta == "":
        break

while True:
    senha = input("Por favor informe sua senha: ")
    if not senha == "":
        break

while True:
    while True:
        opcao = input("Digite sua opção, " + OPCAO_SAQUE + " para saque, " +  OPCAO_DEPOSITO + " para depósito ou " + OPCAO_SAIR + " para sair: ")
        if opcao == OPCAO_SAQUE or opcao == OPCAO_DEPOSITO or opcao == OPCAO_SAIR:
            break
        print("Opção inválida!")

    while True:
        if opcao == OPCAO_SAIR:
            quit()
        elif opcao == OPCAO_SAQUE:
            while True:
                try:
                    valor_a_ser_sacado = float(input("Por favor digite o valor a ser sacado: "))
                    if valor_a_ser_sacado > saldo:
                        print("Valor inválido! Você pode sacar no máximo", saldo)
                    elif valor_a_ser_sacado == 0:
                        print("O valor a se sacar deve ser maior que zero")
                    else:
                        saldo -= valor_a_ser_sacado
                        print("O novo saldo é:", saldo)
                    break
                except ValueError:
                    print("Valor inválido! Por favor tente novamente")
        else: # opcao == OPCAO_DEPOSITO
            while True:
                try:
                    valor_a_ser_depositado = float(input("Por favor digite o valor a ser depositado: "))
                    if valor_a_ser_depositado == 0:
                        print("O valor a se depositar deve ser maior que zero")
                    else:
                        saldo += valor_a_ser_depositado
                        print("O novo saldo é:", saldo)
                    break
                except ValueError:
                    print("Valor inválido! Por favor tente novamente")
        opcao = ""
        break