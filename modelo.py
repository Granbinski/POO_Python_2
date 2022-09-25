class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2022, 160)
print(vingadores.nome)


atlanta = Serie('Atlanta', 2022, 100)
print(atlanta.nome)
