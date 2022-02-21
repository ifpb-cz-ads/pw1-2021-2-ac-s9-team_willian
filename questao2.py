class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.tamanho = 32
        self.marca = 'semp'

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1


tv = Televisao()

print(tv.marca)
print(tv.tamanho)
print(tv.canal)