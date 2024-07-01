class Fila:
    def __init__(self):
        self.valores = [0] * 10
        self.inicio = 0
        self.fim = 0;
        self.total = 0;
        
    def inserir(self, elemento):
        self.valores[self.fim] = elemento;
        self.fim = (self.fim + 1) % 10
        self.total += 1
    
    def retirar(self):
        elemento = self.valores[self.inicio]
        self.inicio = (self.inicio + 1) % 10
        self.total -= 1
        return elemento
    
    def is_empty(self):
        return self.total == 0
    
    def is_fulll(self):
        return self.total == 10
    
    
def main():
    f = Fila()
    f.inserir(176)
    f.inserir(914)
    f.inserir(12)
    f.inserir(100)
    
    while not f.is_empty():
        print(f"Senha a ser retirada: {f.retirar()}")
        

if __name__ == '__main__':
    main()