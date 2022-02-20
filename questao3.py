class Televisao:
    def __init__(self,min,max):
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

tv = Televisao()
tv.canal = 13
print("canal: ",tv.canal)
tv.muda_canal_para_cima()
print("marca da tv: ",tv.marca)
print("tamanho da tv: ",tv.tamanho)
print("canal: ",tv.canal)