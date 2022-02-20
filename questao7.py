class Conta:
    def __init__(self, clientes, número, telefone,saldo=0):
        self.saldo = 0
        self.telefone = telefone
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print("CC N°%s Nome:%s Telefone: %10.2f Saldo: %d" %
              (self.número, self.clientes, self.saldo, self.telefone))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
        else:
            print('Saldo insuficiente para um saque nesse valor')

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n       Saldo: %10.2f\n" % self.saldo)



conta = Conta('willian',20,1200,99812098)
conta.resumo()
