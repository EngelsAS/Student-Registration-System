#Em um arquivo separado foi criada a classe Aluno, importando as classes
#Matematica, Quimica e Fisica que serão referentes as disciplinas
#Que o aluno pode ter
from disciplinas import Matematica, Quimica, Fisica

class Aluno():
    
    def __init__(self):
        self.nome = "--"
        self.disciplinas = []
        
    def set_nome(self,nome):
        self.nome = nome

    #Essa funçao ficará responsavel por atribuir disciplinas ao aluno, as
    #Condições dentro da função foram criadas para que um aluno não se
    #Matricule mais de uma vez na mesma disciplina
    #A medida que o usuario vai escolhendo quais disciplinas o aluno está
    #Matriculado, essas disciplinas vão sendo salvar em um vetor: self.disciplinas
    def set_disciplinas(self):
        cond = "sim"
        condmat = False
        condfis = False
        condquim = False
        i = 0
        while(cond == "sim"):
            print("Qual disciplina quer atribuir a esse aluno?\n1 - Matematica\n2 - Quimica\n3 - Fisica\nEscolha o numero referente a disciplina: ")
            x = int(input())
            if(x == 1):
                if(condmat == False):
                    matematica = Matematica()
                    self.disciplinas.append(matematica)
                    condmat = True
                else:
                    print("O aluno ja está matriculado nessa disciplina")
            
            elif(x == 2):
                if(condquim == False):
                    quimica = Quimica()
                    self.disciplinas.append(quimica)
                    condquim = True
                else:
                    print("O aluno ja está matriculado nessa disciplina")

            elif(x == 3):
                if(condfis == False):
                    fisica = Fisica()
                    self.disciplinas.append(fisica)
                    condfis = True
                else:
                    print("O aluno já está matriculado nessa disciplina")
            
            else:
                print("Disciplina não encontrada")
            
            print("Deseja matricular o aluno em mais alguma disciplina?(sim/nao)")
            cond = input()
    
    def get_nome(self):
        return self.nome
    
    #Função que printa as disciplinas que o aluno está matriculado
    #Retornando True se ele estiver matriculado em qualquer uma
    #E retornando False caso ele não esteja matriculado em nenhuma
    #Esses booleanos podem e serão usados como condições para "if's"
    def get_disciplinas(self):
        if(self.disciplinas.__len__() > 0):
            print("Este aluno está matriculado nas seguintes disciplinas: ")
            i = 0
            for materias in self.disciplinas:
                i = i + 1
                print(str(i)+" - " + materias.get_nome())
            return True
        else:
            print("!!Este aluno não está matriculado em nenhuma disciplina!!")
            return False
    
    def set_notas(self,valor):
        if(self.disciplinas.__len__() >= valor):
            print("Colocar as notas do aluno em "+self.disciplinas[valor - 1].get_nome())
            print("Insira a primeira nota: ")
            resp = int(input())
            self.disciplinas[valor - 1].set_nota1(resp)
            print("Insira a segunda nota: ")
            resp = int(input())
            self.disciplinas[valor - 1].set_nota2(resp) 

    #Função para remover disciplinas
    def remove_disc(self,valor):
        if(self.disciplinas.__len__() >= valor):
            print(self.disciplinas[valor - 1].get_nome()+" foi removida das disciplinas do aluno")
            self.disciplinas.remove(self.disciplinas[valor - 1])

    #Função para atualizar disciplinas
    def atualiza_disc(self,valor):
        if(self.disciplinas.__len__() >= valor):
            print("Deseja atualizar para qual dessas disciplinas?(Escolha o numero referente a disciplina desejada)")
            print("1 - Matematica\n2 - Quimica\n3 - Fisica")
            print("(Caso substitua pela mesma disciplina, os dados serão sobrescritos)")
            resp = int(input())
            if(resp == 1):
                matematica = Matematica()
                self.disciplinas[valor - 1] = matematica
                print("Disciplina atualizada")
            elif(resp == 2):
                quimica = Quimica()
                self.disciplinas[valor - 1] = quimica
                print("Disciplina atualizada")
            elif(resp == 3):
                fisica = Fisica()
                self.disciplinas[valor - 1] = fisica
                print("Disciplina atualizada")
    
    #Essa função foi feita para printar as medias de todas as disciplinas que o usuario desejar
    #Porem nessa função não é possivel trabalhar com os valores isolados de cada media
    def get_medias(self, valor):
        if(self.disciplinas.__len__() >= valor):
            print("A media nessa disciplina é: ", self.disciplinas[valor - 1].get_media())

    #Essas funcoes abaixo foram feitas para verificar se o aluno está matriculado na disciplina
    #De forma resumida, essas funções existem apenas para serem usadas por outras funções especificas
    #Existentes na classe Aluno
    def get_matematica(self):
        for materia in self.disciplinas:
            if(materia.get_nome() == "Matematica"):
                return "Matematica"
            else:
                return None
    
    def get_quimica(self):
        for materia in self.disciplinas:
            if(materia.get_nome() == "Quimica"):
                return "Quimica"
            else:
                return None
    
    def get_fisica(self):
        for materia in self.disciplinas:
            if(materia.get_nome() == "Fisica"):
                return "Fisica"
            else:
                return None
    
    #As funções abaixo servem para retornar o valor isolado da media de cada disciplina
    def get_mediamat(self):
        for materia in self.disciplinas:
            if(materia.get_nome() == "Matematica"):
                media = materia.get_media()
                return media
            else:
                return None
    
    def get_mediaquim(self):
        for materia in self.disciplinas:
            if(materia.get_nome() == "Quimica"):
                media = materia.get_media()
                return media
            else:
                return None
    
    def get_mediafis(self):
        for materia in self.disciplinas:
            if(materia.get_nome() == "Fisica"):
                media = materia.get_media()
                return media
            else:
                return None

    #Função que retorna os alunos com medias menores do que 7
    #Aqui foram usadas as funções que retornam os valores isolados
    #De cada disciplina
    def get_menoresque7(self,valor,aluno):
        if(valor == 1):
            if(aluno.get_matematica() == "Matematica"):
                if(aluno.get_mediamat() < 7):
                    print(aluno.get_nome())
        elif(valor == 2):
            if(aluno.get_quimica() == "Quimica"):
                if(aluno.get_mediaquim() < 7):
                    print(aluno.get_nome())
        elif(valor == 3):
            if(aluno.get_fisica() == "Fisica"):
                if(aluno.get_mediafis() < 7):
                    print(aluno.get_nome())
    
    def get_maioresque7(self,valor,aluno):
        if(valor == 1):
            if(aluno.get_matematica() == "Matematica"):
                if(aluno.get_mediamat() >= 7):
                    print(aluno.get_nome())
        elif(valor == 2):
            if(aluno.get_quimica() == "Quimica"):
                if(aluno.get_mediaquim() >= 7):
                    print(aluno.get_nome())
        elif(valor == 3):
            if(aluno.get_fisica() == "Fisica"):
                if(aluno.get_mediafis() >= 7):
                    print(aluno.get_nome())
    
    def get_notas(self):
        for materia in self.disciplinas:
            print(materia.get_nome(),":\n",materia.get_nota1(),"\n",materia.get_nota2())


        


            

        

            

            


