# Lista de disciplinas
disciplinas = ['INF100', 'INF101', 'INF103', 'MAT140',
               'MAT141', 'MAT144', 'LET100', 'FIS203']

# Dicionário de alunos
matriculas = {
    "Ana Lobo": {'INF101', 'MAT140', 'LET100'},
    "João Marques": {'INF100', 'INF103', 'MAT141'},
    "Jasão Silva": {'INF100', 'MAT144', 'INF103', 'LET100'},
    "Paulo Gomes": {'INF101', 'LET100'},
    "Aline Souza": {'INF100', 'MAT141', 'LET100', 'INF103'},
    "Antônio Soares": {'INF103', 'MAT144', 'LET100'},
    "Teresa Oliveira": {'INF101', 'MAT141', 'LET100'},
    "José Farias": {'MAT144', 'LET100', 'FIS203'},
    "Ivo Lopes": {'INF101', 'FIS203', 'MAT144', 'LET100'},
    "Luíza Xisto": {'INF101', 'MAT141'}
    }

emptySet = set()

conflito = [emptySet for d in disciplinas]

def print_conflito(conflito, disciplinas) :
  for i in range(len(disciplinas)) :
    print(disciplinas[i],': conflito', conflito[i])
  print()

for a in matriculas.keys():
  for d in range(len(disciplinas)): # len(disciplinas=8 | range [0 ... 7]
    if disciplinas[d] in matriculas[a]: # INF100 pertence a {'INF100', 'INF103', 'MAT141'}
      conflito[d] = conflito[d].union(matriculas[a])

print_conflito(conflito, disciplinas)

# Constrói o horário que é uma lista de sessões em que cada
# sessão é uma seleção de disciplinas que não conflitam.

restante = set(disciplinas)
horario = []

while restante != emptySet:
  i = 0
  d = disciplinas[i]
  while d not in restante:
    i = i + 1
    d = disciplinas[i]

  sessao = {d}
  tentativa = restante.difference(conflito[i])
  for s in range(len(disciplinas)):
    if disciplinas[s] in tentativa:
      if conflito[s].isdisjoint(sessao):
        sessao.add(disciplinas[s])

  restante = restante.difference(sessao)
  horario.append(sessao)

  
  # Imprime as sessões não conflitantes do horário.
  for i in range(len(horario)):
      print(horario[i])
