from product_repository import getAll, getById, add, update, delete


def execute():
    while True:
        print("\n******* Escolha uma opção abaixo: *******")

        option = int(input(
            "(1) Buscar Todos (2) Buscar Por Id (3) Adicionar (4) Editar (5) Excluir (6) Sair \n"))

        if (option == 1):
            products = getAll()
            for product in products:
                print("{0} - {1}".format(product.id, product.name))

        elif (option == 2):
            id = input("Informe o id:")
            product = getById(int(id))
            if product is None:
                print("Id não encontrado")
                continue
            print("{0} - {1}".format(product.id, product.name))

        elif (option == 3):
            name = input("Informe o nome do novo produto:")
            add(name)

        elif (option == 4):
            id = input("Informe o id:")
            product = getById(int(id))
            if product is None:
                print("Id não encontrado")
                continue
            product.name = input("Informe o novo nome do produto:")
            update(product)

        elif (option == 5):
            id = input("Informe o id:")
            product = getById(int(id))
            if product is None:
                print("Id não encontrado")
                continue
            response = delete(product)
            if response is None:
                print("Erro ao tentar e!")
                continue
            print("Produto excluído com sucesso!")

        elif (option == 6):
            exit()

        else:
            print("Digite uma opção válida!")


if(__name__ == "__main__"):
    execute()
