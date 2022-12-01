class Teste:
    def __init__(self):
        self.nomeclasse = self.__class__.__name__

    def printar(self):
        return self.nomeclasse
    
    def texto(self):
        print("Misera")


Teste = Teste()
print(Teste.printar())

if(Teste.printar() == "Teste"):
    print("deu certo")

x = int(input())
print(x)
