class Cachorro:
    def __init__(self, nome, idade, raca, comida, energia):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.energia = energia
        self.acordado = False
        self.feliz = False

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado(a)")

    def comer(self):
        if self.acordado is True:
            self.comida -= 1
            self.feliz = True
            print(f"{self.nome} se alimentou")
            print(f"{self.comida} alimentos restantes")
        else:
            print(f"{self.nome} está dormindo e não pode comer.")

    def dormir(self):
        self.energia = 100
        self.acordado = False
        print(f"{self.nome} está dormindo")

    def brincar(self):
        if self.acordado is True: 
            if self.energia >= 20:
                self.energia -= 20
                self.feliz = True
                print(f"{self.nome} está brincando e está feliz!")
            else:
                print(f"{self.nome} está cansado e não pode brincar")            
        else:
            print(f"{self.nome} está dormindo e não pode brincar.")

    def latir(self):
        if self.acordado is True:
            print(f"{self.nome} brincou tanto que está latindo")
            print("AU AU AU AU")
        else:
            print(f"{self.nome} está dormindo")

meu_animal1 = Cachorro ("Lila", 2, "Pincher", 8, 100)
meu_animal2 = Cachorro ("Pipo", 1, "Alemao", 7, 100)

meu_animal1.acordar()
meu_animal1.comer()
meu_animal1.brincar()
meu_animal1.latir()

meu_animal2.acordar()
meu_animal2.comer()
meu_animal2.brincar()
meu_animal2.brincar()
meu_animal2.brincar()
meu_animal2.brincar()
meu_animal2.brincar()
meu_animal2.brincar()
meu_animal2.latir()
meu_animal2.dormir()
meu_animal2.acordar()
meu_animal2.brincar()