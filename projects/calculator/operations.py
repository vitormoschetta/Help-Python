class  Operations:    
    def PrintResult(self, result):
        print('Resultado: ' + str(self.result))

    def Soma(self, x, y):
        self.result = float(x) + float(y)
        self.PrintResult(self.result)

    def Subtracao(self, x, y):
        self.result  = float(x) - float(y)
        self.PrintResult(self.result)

    def Multiplicacao(self, x, y):
        self.result  = float(x) * float(y)
        self.PrintResult(self.result)

    def Divisao(self, x, y):
        self.result  = float(x) / float(y)
        self.PrintResult(self.result)