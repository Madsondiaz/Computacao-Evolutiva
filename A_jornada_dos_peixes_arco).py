
import random

populacao_peixes = 100
caminho = 8
geracoes = 100
mutacao_taxa = 0.1

direcao = [0, 1]

def gerar_peixe():
    return [random.choice(direcao) for _ in range(caminho)]

def avaliar_peixe(peixe):
    return peixe.count(1)

def torneio(populacao, k=5):
    competidores = random.sample(populacao, k)
    return max(competidores, key=avaliar_peixe)

def cruzar(pai, mae):
    ponto = random.randint(1, caminho - 2)
    return pai[:ponto] + mae[ponto:]

def mutar(peixe):
    for i in range(caminho):
        if random.random() < mutacao_taxa:
            peixe[i] = 1 - peixe[i]
    return peixe

populacao = [gerar_peixe() for _ in range(populacao_peixes)]

for geracao in range(geracoes):
    new_pop = []

    elite = sorted(populacao, key=avaliar_peixe, reverse=True)[:2]
    new_pop.extend(elite)

    while len(new_pop) < populacao_peixes:
        pai = torneio(populacao)
        mae = torneio(populacao)
        filho = cruzar(pai, mae)
        filho = mutar(filho)
        new_pop.append(filho)

    populacao = new_pop
    melhor_peixe = max(populacao, key=avaliar_peixe)
    print(f"Geração {geracao+1}: Melhor caminho {melhor_peixe}, pontos: {avaliar_peixe(melhor_peixe)}")

print("Solução Final:")
final = max(populacao, key=avaliar_peixe)
print(f"Melhor caminho: {final}, pontos: {avaliar_peixe(final)}")
