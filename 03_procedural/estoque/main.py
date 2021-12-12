from product_repository import getAll, getById, add, update, delete

def execute():
    while True:        
        print("\n******* Escolha uma opção abaixo: *******")

        option = int(input("(1) Buscar Todos (2) Buscar Por Id (3) Adicionar (4) Editar (5) Excluir (6) Sair \n"))

        if (option == 1):
            products = getAll()
            for product in products:
                print("{0} - {1}".format(product.id, product.name))          

        elif (option == 2):
            pass

        elif (option == 3):
            pass

        elif (option == 4):            
            pass

        elif (option == 5):            
            pass
            
        elif (option == 6):
            exit()

        else:
            print("Digite uma opção válida!")


if(__name__ == "__main__"):    
    execute()