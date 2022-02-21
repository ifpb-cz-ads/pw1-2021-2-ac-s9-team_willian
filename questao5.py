class Televisao:
    def __init__(self,min=2,max=14):
        self.ligada = False
        self.canal = 2
        self.tamanho = 32
        self.marca = 'semp'
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        self.canal -= 1
        if(self.canal-1 <= self.cmin):
               self.canal = self.cmax
    def muda_canal_para_cima(self):
        self.canal += 1
        if (self.canal + 1 >= self.cmax):
            self.canal = self.cmin

tv1 = Televisao()
tv1.min = 3
tv1.max = 14
tv1.canal = 14;
tv1.muda_canal_para_cima()
print(tv1.canal)
tv2 = Televisao()
tv2.min = 2
tv2.max = 10

