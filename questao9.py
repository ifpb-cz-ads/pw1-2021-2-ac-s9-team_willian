class Conta:
    def __init__(self, clientes, numero, telefone, saldo=0):
        self.saldo = 0
        self.telefone = telefone
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print("CC N°%s Nome:%s Telefone: %d Saldo: %d" %
              (self.numero, self.clientes, self.saldo, self.telefone))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.sacado = True
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            print('Saldo insuficiente para um saque nesse valor')

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.numero)
        for o in self.operacoes:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n       Saldo: %10.2f\n" % self.saldo)


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True

conta = Conta('willian', 20, 1200, 99812098)
conta.resumo()
