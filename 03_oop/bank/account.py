class Account:
    def __init__(self, number, owner, balance, limit):
        print("Construindo objeto Conta ... {}".format(self))
        # encapsulamento: private = __
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print('Valor solicitado maior que valor disponível na conta: {:.2f}'.format(self.__balance))
            return
        self.__balance -= amount

    def transfer(self, destiny, amount):
        self.withdraw(amount)
        destiny.deposit(amount)

    def statement(self):
        print("O saldo da conta {} é {:.2f}".format(self.__number, self.__balance))

    # getters e setters
    def get_balance(self) -> float:
        return self.__balance

    def set_limit(self, amount):
        self.__limit = amount

    # getters e setters melhorados
    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def limit(self) -> float:
        return self.__limit

    @limit.setter
    def limit(self, amount):
        self.__limit = amount

    # metodos estáticos
    @staticmethod
    def test():
        print("Esse método é estatico, ou seja, não preciso de uma instância/objeto, e por isso não temos a palavra chave 'self'")













