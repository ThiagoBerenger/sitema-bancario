#Sistema bancário

menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q]


=>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Valor do deposito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R${valor:.2f}\n'
        
        else:
            print('Erro na operação. Tente novamente com um valor válido!')

    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))

        exedeu_saldo = valor > saldo
        exedeu_limite = valor > limite
        exedeu_saques = numero_saques >= LIMITE_SAQUES

        if exedeu_saldo:
            print('Operação falhou! você não tem saldo suficiente.')
        elif exedeu_limite:
            print('Limite excedido.')
        elif exedeu_saques:
            print('Número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Valor inválido')

    elif opcao == 'e':
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')

    elif opcao == 'q':
        break

    else:
        print('Opção inválida, tente novamente.')