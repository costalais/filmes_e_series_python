#Classe principal
class Programa:
    def __init__(self,nome,ano,likes = 0):
        self.nome = nome
        self.ano=ano
        self.likes = likes

    def dar_like(self):
        self.likes += 1
    
    def __str__(self,):
         return f"{self.nome} - {self.ano} - {self.likes} Likes"

#classes Filme e Série

class Filme:
    def __init__(self, nome,ano,duracao,likes = 0):
        super().__init__()
        self.nome = nome
        self.ano = ano
        self.likes= likes
        self.duracao = duracao
    
    def dar_like(self):
        self.likes += 1
    
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'
    
class Serie:
        def __init__(self,nome,ano,temporada, likes=0):
            super().__init__()
            self.nome = nome
            self.ano = ano
            self.likes=likes
            self.temporada= temporada

        def __str__(self):
            return f"{self.nome}- {self.ano} - {self.temporada} temporadas- {self.likes} Likes"
        
        def dar_like(self):
         self.likes += 1

#Inserção de filmes e séries pelo usuário
filmes = []
series = []

while True:
    opcao = input("Deseja adicionar um programa? (f - Filme / s - Série / n - Sair): ")
    
    if opcao.lower() == "n":
        break

    elif opcao.lower() == "f":
        nome = input("Insira um Filme: ")
        ano = int(input("Insira o Ano de lançamento: "))
        duracao = int(input("Insira a duração do filme em minutos: "))
        filme = Filme(nome, ano, duracao )
        filmes.append(filme)
    
    elif opcao.lower() == "s":
        nome = input("Insira o nome da série: ")
        ano = int(input("Insira o ano de lançamento da série: "))
        temporada = int(input("Insira o número de temporadas: "))
        serie = Serie(nome, ano, temporada)
        series.append(serie)

# Exibindo os filmes e séries adicionados
print("Filmes adicionados:")
for filme in filmes:
    print(filme)

print("Séries adicionadas:")
for serie in series:
    print(serie)

# Dar Like
for i, filme in enumerate(filmes):
    print(f"{i}. {filme.nome} - Likes: {filme.likes}")

for i, serie in enumerate(series):
    print(f"{i}. {serie.nome} - Likes: {serie.likes}")

filme_escolhido = int(input("Digite o número do filme que deseja dar like: "))
filmes[filme_escolhido].dar_like()

serie_escolhida = int(input("Digite o número da série que deseja dar like: "))
series[serie_escolhida].dar_like()

print(f"Likes atualizados para o filme {filme_escolhido}.")
print(f"Likes atualizados para a série {serie_escolhida}.")
