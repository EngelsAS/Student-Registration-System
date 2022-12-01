#O arquivo main foi criado para ser usado como um menu para o usuario
#Fazendo a tarefa de chamar as funçoes das classes
from aluno import Aluno

ListaAlunos = []


print("----------Sistema de controle acadêmico----------")

#Essas variaveis (cond/cond2) foram criadas com o objetivo de serem usadas em estruturas de condição if\else
cond = "sim"
cond2 = False

while(cond == "sim"):
    print("Escolha o numero referente a opção desejada:")
    print("1 - Cadastrar aluno\n2 - Cadastrar disciplina em aluno\n3 - Cadastrar nota em disciplina de aluno\n4 - Remover aluno")
    print("5 - Remover disciplina de aluno\n6 - Atualizar aluno\n7 - Atualizar disciplina de aluno\n8 - Atualizar nota de disciplina do aluno")
    print("9 - Visualizar a média do aluno em uma disciplina\n10 - Visualizar os nomes dos alunos que estão com média menor que 7")
    print("11 - Visualizar os nomes dos alunos que estão com média maior ou igual a 7\n12 - Visualizar as notas das disciplinas cadastradas em um aluno")
    print("0 - Encerrar")
    x = int(input())
    if(x == 1):
        print("Qual o nome do aluno que deseja cadastrar?: ")
        resp = input()
        aluno = Aluno()
        aluno.set_nome(resp)
        for pessoa in ListaAlunos:
            if(pessoa.get_nome() == resp):
                print("Esse aluno ja está cadastrado no sistema")
                cond2 = True
        if(cond2 == False):        
            ListaAlunos.append(aluno)
        cond2 = False
    
    elif(x == 2):
        print("Qual o nome do aluno que deseja atribuir disciplinas?: ")
        resp = input()
        for pessoa in ListaAlunos:
            if(pessoa.get_nome() == resp):
                pessoa.set_disciplinas()
                print("Disciplinas atribuidas para "+pessoa.get_nome())
                cond2 = True
        if(cond2 == False):
            print("Aluno não encontrado no sistema")
        cond2 = False
    
    elif(x == 3):
        print("Em qual aluno você deseja cadastrar as notas?")
        resp = input()
        for pessoa in ListaAlunos:
            if(pessoa.get_nome() == resp):
                while(cond == "sim"):
                    if(pessoa.get_disciplinas() == True):
                        print("Em qual das disciplinas desejar atribuir as notas?(Escolha o numero referente a disciplina) ")
                        resp = int(input())
                        pessoa.set_notas(resp)
                        print("Notas cadastradas, deseja atribuir nota a alguma outra disciplina?(sim/nao)")
                        cond = input()
                    else:
                        cond = "nao"
                cond = "sim"
                cond2 = True
        if(cond2 == False):
            print("Aluno não encontrado no sistema")
        cond2 = False
    
    elif(x == 4):
        print("Qual o nome do aluno que você deseja remover?")
        resp = input()
        for pessoa in ListaAlunos:
            if(pessoa.get_nome() == resp):
                ListaAlunos.remove(pessoa)
                print(pessoa.get_nome()+" foi removido")
                cond2 = True
        if(cond2 == False):
            print("Aluno não encontrado no sistema")
        cond2 = False
    
    elif(x == 5):
        print("Qual o nome do aluno que você deseja remover uma disciplina?")
        resp = input()
        for pessoa in ListaAlunos:
            if(pessoa.get_nome() == resp):
                if(pessoa.get_disciplinas() == True):
                    print("Qual disciplina deseja remover?(Escolha o numero referente a disciplina")
                    resp = int(input())
                    pessoa.remove_disc(resp)
                    cond2 = True
                else:
                    cond2 = True
        if(cond2 == False):
            print("Aluno não encontrado no sistema")
        cond2 = False
    
    elif(x == 6):
        print("Qual o nome do aluno que você deseja atualizar?")
        resp = input()
        for pessoa in ListaAlunos:
            if(pessoa.get_nome() == resp):
                print("Insira o novo nome do aluno: ")
                resp = input()
                pessoa.set_nome(resp)
                print("Nome do aluno atualizado!")
                cond2 = True
        if(cond2 == False):
            print("Aluno não encontrado no sistema")
        cond2 = False
    
    elif(x == 7):
        print("Qual o nome do aluno que você deseja atualizar a disciplina?")
        resp = input()
        for pessoa in ListaAlunos:
            if(pessoa.get_nome() == resp):
                if(pessoa.get_disciplinas() == True):
                    print("Qual dessas disciplinas você deseja atualizar?(Escolha o numero referente a disciplina)")
                    resp = int(input())
                    pessoa.atualiza_disc(resp)
                    cond2 = True
                else:
                    cond2 = True
        if(cond2 == False):
            print("Aluno não encontrado no sistema")
        cond2 = False
    
    elif(x == 8):
        print("Qual o nome do aluno que você deseja atualizar a nota?")
        resp = input()
        for pessoa in ListaAlunos:
            if(pessoa.get_nome() == resp):
                while(cond == "sim"):
                    if(pessoa.get_disciplinas() == True):
                        print("Em qual das disciplinas desejar atualizar as notas?(Escolha o numero referente a disciplina) ")
                        resp = int(input())
                        pessoa.set_notas(resp)
                        print("Notas cadastradas, deseja atualizar a nota de alguma outra disciplina?(sim/nao)")
                        cond = input()
                    else:
                        cond = "nao"
                cond = "sim"
                cond2 = True
        if(cond2 == False):
            print("Aluno não encontrado no sistema")
        cond2 = False
    
    elif(x == 9):
        print("Qual o nome do aluno que você deseja ver as medias das disciplinas?")
        resp = input()
        for pessoa in ListaAlunos:
            if(pessoa.get_nome() == resp):
                if(pessoa.get_disciplinas() == True):
                    print("Qual dessas disciplinas você deseja ver a media?(Escolha o numero referente a disciplina)")
                    resp = int(input())
                    pessoa.get_medias(resp)
                    cond2 = True
                else:
                    cond2 = True
        if(cond2 == False):
            print("Aluno não encontrado no sistema")
        cond2 = False

    #Aqui foi usado um for que chama a função passando sempre um novo aluno para ser verficado
    elif(x == 10):
        print("Deseja vizualizar os alunos com media menor que 7 em qual disciplina?\n(escolha o numero referente a disciplina)")
        print("1 - Matematica\n2 - Quimica\n3 - Fisica")
        resp = int(input())
        for pessoa in ListaAlunos:
            pessoa.get_menoresque7(resp,pessoa)

    elif(x == 11):
        print("Deseja vizualizar os alunos com media maior que 7 em qual disciplina?\n(escolha o numero referente a disciplina)")
        print("1 - Matematica\n2 - Quimica\n3 - Fisica")
        resp = int(input())
        for pessoa in ListaAlunos:
            pessoa.get_maioresque7(resp,pessoa)
    
    elif(x == 12):
        print("Qual o nome do aluno que você deseja vizualizar as notas?: ")
        resp = input()
        for pessoa in ListaAlunos:
            if(pessoa.get_nome() == resp):
                if(pessoa.get_disciplinas() == True):
                    print("As notas do aluno nessas disciplinas são: ")
                    pessoa.get_notas()
    
    elif(x == 0):
        cond = "nao"
    
    else:
        print("Opção invalida")
                