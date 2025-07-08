# Deposito
    #deve ser possível depositar valores positivo para minha conta bancária
    #não precisamos identificar usuário, nem número de agencia.
    #todo deposito deve ser armazenado em uma variavel e exibido na operação de extrato.
# Saque
    #o sistema deve permitir realizar 3 saques diarios com limite máximo de 500 por saque.
    #caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
    #todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato.
# Extrato
    #deve listar todos os depositos e saques na conta.
    #no fim da listagem deve ser exibido o saldo atual da conta.
    #os valores devem ser exibidos utilizando o formato R$ xxx.xx
menu = """
    |========= MENU ========|
    |    Escolha a opção:   |
    |      [1] Sacar        |
    |      [2] Depositar    | 
    |      [3] Extrato      |
    |      [4] Sair         |
    |_______________________|      
"""

saldoBancario = 0.00
extrato = []
limite = 200.00
qtdSaque = 3
limiteSaque = 500.00

while True:

    print(menu)
    retorno = input('Digite a opção desejada: ')
    if retorno.isnumeric() == True:
        
        opcao = int(retorno)
        if opcao == 1:
            if(qtdSaque != 0):
                print('Saldo atual: ', saldoBancario)  
                saque = float(input('Digite o valor que deseja sacar: '))
                
                if(saldoBancario+limite < saque):
                    print(f'Você não pode realizaar esse saque de R$ {saque:.2f}, pois não possui saldo!')
                elif (saque <= limiteSaque):
                    qtdSaque-=1
                    saldoBancario -= saque
                    nota = 'Saque'
                    extrato.append(f"{nota}: R$ {saque:.2f}")
                    print('Saldo atual: ', saldoBancario)
                else:
                    print(f'Saque maior que limite por saque, valor máximo permitido de {limiteSaque}')
            else:
                print('Você não pode mais realizar saques nesta data! ')
            
        elif opcao == 2:
            deposito = float(input('Digite o valor a ser depositado: '))
            if (deposito > 0):
                nota = 'Depósito'
                extrato.append(f"{nota}: R$ {deposito:.2f}")
                saldoBancario += deposito
                print(saldoBancario)
                print(extrato)
            else: 
                print('Deposite um valor válido!')
        elif opcao == 3:
            print(extrato)
            print('Saldo: ', saldoBancario)

        elif opcao == 4:
            break;
    else:
        print('Opção Inválida, digite o valor de uma das opções!')


print('Obrigado, volte sempre!')