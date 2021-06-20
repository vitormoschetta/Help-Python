from os import truncate
from account import account_create, deposit_amount, withdraw_amount, statement

def process():
    while True:        
        print("\n******* Escolha uma opção abaixo: *******")

        option = int(input("(1) Criar conta (2) Depositar (3) Sacar (4) Extrato (5) Sair \n"))

        if (option == 1):
            number = input("Informe o número da conta:")
            owner = input("Informe o nome do titular da conta:")
            balance = float(input("Informe o saldo inicial da conta:"))
            limit = input("Informe o limite de crédito da:")
            account = account_create(number, owner, balance, limit)
            print(account)
            print("Conta criada com suceso!")

        elif (option == 2):
            amount = float(input("Informe o valor a ser depositado:"))
            deposit_amount(account, amount)  
            print("Valor depositado com sucesso!")
            print("Saldo atualizado: {}".format(account["balance"]))    

        elif (option == 3):
            amount = float(input("Informe o valor do saque:"))
            withdraw_amount(account, amount)  
            print("Saque realizado com sucesso!")
            print("Saldo atualizado: {}".format(account["balance"])) 

        elif (option == 4):            
            print("Saldo atualizado: {}".format(account["balance"])) 

        elif (option == 5):
            exit()

        else:
            print("Digite uma opção válida!")


if(__name__ == "__main__"):    
    process()