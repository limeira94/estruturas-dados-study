class Televisao:
    def __init__(self):
        self.marca = ""
        self.ligado = False
        self.canal = 0 
        self.volume = 0
        
    def ligar(self):
        self.ligado = True
        print(f"A TV {self.marca} está ligada")
    
    def desligar(self):
        self.ligado = False
        print(f"A TV {self.marca} está desligada")
    
    def definir_marca(self, nome_marca):
        self.marca = nome_marca
        print(f"A marca da TV é {self.marca}")
        
    def aumentar_volume(self, vol):
        if self.ligado == True:
            self.volume = vol
            print(f"Volume: {self.volume}")
        else:
            print("A TV não está ligada")
        
    def diminuir_volume(self):
        if self.ligado == True:
            self.volume -= 1
            print(f"Volume: {self.volume}")
        else:
            print("A TV não está ligada")
    
    def mudar_canal(self, ca):
        if self.ligado == True:
            self.canal = ca
            print(f"Canal: {self.canal}")
        else:
            print("A TV não está ligada")
            

def main():
    t = Televisao()
    t.definir_marca("Samsung")
    t.ligar()
    t.aumentar_volume(5)
    t.mudar_canal(3)
    t.desligar()
    

if __name__ == "__main__":
    main()