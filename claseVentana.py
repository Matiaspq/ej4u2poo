class Ventana:
    def __init__(self, titulo, x1=0, y1=0, x2=500, y2=500):
        self.titulo = titulo
        self.x1 = max(0, x1)
        self.y1 = max(0, y1)
        self.x2 = min(500, x2)
        self.y2 = min(500, y2)
        self.ancho_ventana = self.x2 - self.x1
        self.alto_ventana = self.y2 - self.y1
    
    def getTitulo(self):
        return self.titulo
    
    def alto(self):
        return self.alto_ventana
    
    def ancho(self):
        return self.ancho_ventana
    
    def mostrar(self):
        print('Ventana: {} x1: {} y1: {} x2: {} y2: {}'.format(self.titulo,self.x1,self.y1,self.x2,self.y2))
    
    def moverDerecha(self, unidades=1):
        if self.x2 + unidades <= 500:
            self.x1 += unidades
            self.x2 += unidades
    
    def moverIzquierda(self, unidades=1):
        if self.x1 - unidades >= 0:
            self.x1 -= unidades
            self.x2 -= unidades
    
    def bajar(self, unidades=1):
        if self.y2 + unidades <= 500:
            self.y1 += unidades
            self.y2 += unidades
    
    def subir(self, unidades=1):
        if self.y1 - unidades >= 0:
            self.y1 -= unidades
            self.y2 -= unidades