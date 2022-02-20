class Cidade:

    def __init__(self, cidades, populacao):
        self.cidades = cidades
        self.populacao = populacao


class Estado:

    def __init__(self, cidades, populacao, nome, sigla):
        Cidade.__init__(self, cidades, populacao)
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades
        self.populacao = populacao


    def show(self):
        Sum = sum(self.populacao)
        cities = ', '.join(self.cidades)
        print('Estado: ', self.nome)
        print(self.sigla)
        print('Cidades: ',cities)
        print('Populacao total: ', Sum)


paraiba = Estado(['Cajazeiras','Joao Pessoa','Catolé'],[65000,100000,23000],'Paraiba','PB')

paraiba.show()

saopaulo = Estado(['Sao Paulo','Jundiai','São José'],[20000000,30000,20000],'Sao Paulo', 'SP')
saopaulo.show()

ceara = Estado(['Fortaleza','Sobral','Canoa Quebrada'],[1000000,100000,200000],'Ceará', 'CE')
ceara.show()