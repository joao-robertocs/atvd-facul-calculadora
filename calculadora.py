while True:
    print('Selecione a operação:')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Sair')

    escolha = input('Escolha uma opção: (1/2/3/4/5) ')

    if escolha == '5':
        print('Fechando!')
        break

    num1 = float(input('Digite seu primeiro número: '))
    num2 = float(input('Digite seu segundo número: '))

    if escolha == '1':
        print(f'Resultado: {num1} + {num2} = {num1 + num2}')
    elif escolha == '2':
        print(f'Resultado: {num1} - {num2} = {num1 - num2}')
    elif escolha == '3':
        print(f'Resultado: {num1} * {num2} = {num1 * num2}')
    elif escolha == '4':
        if num2 == 0:
            print('Erro: divisão por zero!')
        else:
            print(f'Resultado: {num1} / {num2} = {num1 / num2}')
    else:
        print('Opção inválida! Tente novamente.')

input('Pressione enter para continuar...')
print('\n' * 2)
