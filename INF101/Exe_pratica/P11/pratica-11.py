# p11.py
# Programador: Maycon Vinicius 
# Matrícula: 113683
# Criado em: 
# Atualizado em: 16/11/2023
# Construção de horario ultilizando classes e outros conceitos que With e try except 

import sys

####                                                                        ####
# DECLARE AQUI A CLASSE RegistroEscolar com todos os seus métodos (e atributos)#
####                                                                        ####

class RegistroEscolar:
    def __init__(self, ano, periodo):
        self.ano = ano
        self.periodo =((ano, periodo))
        self.disciplinas = []
        self.matriculas = {}
        self.horario = []
        
    def set_disciplinas(self, nomeArq):
        try:
            with open(nomeArq, 'r') as arq:
                
                listamat = []
                linha = arq.readline().rstrip('\n')  
                while linha != '':
                    dados = linha
                    mat = dados
                    listamat.append((mat))
                    linha = arq.readline().rstrip('\n')
    
            
            self.disciplinas = listamat
            
            
            
        except OSError:
            print("Erro no Arquivo de Disciplinas")
    def set_matriculas(self,nomeArq):
        try:
            with open(nomeArq,'r') as arq:
                
                dicMate = {}
                linha = arq.readline().rstrip('\n')
                while linha != '':
                    dados = linha.split(',')
                    matri = str(dados[0])
                    disci = set(dados[1:])
                    dicMate[matri] = disci
                    linha = arq.readline().rstrip('\n')
                arq.close()
            
            
            self.matriculas = dicMate
            
            
            
        except OSError:
            print("Erro no Arquivo de Matriculas")
        
    def set_horario(self):
        self.horario = []
        
        #print(self.disciplinas)
        
        emptySet = set() # conjunto vazio
    
        conflitos = [ emptySet for d in self.disciplinas ]
        for a in self.matriculas.keys():
            for d in range(len(self.disciplinas)):
                if self.disciplinas[d] in self.matriculas[a]:
                    conflitos[d] = conflitos[d].union(self.matriculas[a])
        
        restantes = set(self.disciplinas)
        
        while restantes != emptySet:
            i = 0
            d = self.disciplinas[i]
            while d not in restantes:
                i = i + 1
                d = self.disciplinas[i]
            sessao = { d }
            tentativa = restantes.difference(conflitos[i])
            for s in range(len(self.disciplinas)):
                if self.disciplinas[s] in tentativa:
                    if conflitos[s].isdisjoint(sessao):
                        sessao.add(self.disciplinas[s])
            restantes = restantes.difference(sessao)

            self.horario.append(sessao)



def main():
    # Define os nomes dos arquivos de entrada; usa os defaults, se não houver
    # argumentos com os nomes na linha de comando.
    nomeArqDiscs = 'disciplinas.txt'
    nomeArqMatrics = 'matriculas.txt'
    if len(sys.argv) > 1:
        nomeArqDiscs = sys.argv[1]
    if len(sys.argv) > 2:
        nomeArqMatrics = sys.argv[2]
    
    # Cria uma instância da classe RegistroEscolar.
    res = RegistroEscolar(2020, 2)
    
    # Estabelece as disciplinas do período instanciado.
    res.set_disciplinas(nomeArqDiscs)
    
    # Estabelece as matrículas do período instanciado.
    res.set_matriculas(nomeArqMatrics)
    
    # Estabelece as sessões para o horário do período instanciado.
    res.set_horario()
    
    # Imprime as sessões possíveis para o horário do período instanciado.
    print('\nSessões para o período {:4d}/{:d}:'.format(res.periodo[0],\
          res.periodo[1]))
    for i in range(len(res.horario)):
        print('{:3d}: '.format(i), sorted(res.horario[i]))
    print()


if __name__ == '__main__':
    main()

