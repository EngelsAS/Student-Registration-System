#Nesse arquivo foram criadas as Classes referentes as disciplinas que o usuario
#pode escolher, as classes foram criadas atraves do conceito de Herança
#sendo a classe Disciplina, a classe "pai"
#e as classes Matematica, Quimica e Fisica sendo as classes filhas

class Disciplina:

    def __init__(self):
        self.nota1 = "--"
        self.nota2 = "--"
        self.media = 0
        self.nomeclasse = self.__class__.__name__
    
    def set_nota1(self,valor):
        self.nota1 = valor
    
    def set_nota2(self,valor):
        self.nota2 = valor

    def get_nota1(self):
        return self.nota1
    
    def get_nota2(self):
        return self.nota2
    
    def get_media(self):
        self.media = (self.nota1 + self.nota2)/2
        return self.media
    
    def get_nome(self):
        return self.nomeclasse

class Matematica(Disciplina):
    pass

class Quimica(Disciplina):
    pass

class Fisica(Disciplina):
    pass


