import random
import matplotlib.pyplot as plt


N = 3
POPULATION_SIZE = 10
MAX_GENERATIONS = 1000
MUTATION_RATE = 0.05
VISUALIZE_EVERY = 50
MAX_FITNESS = (N * (N - 1)) // 2  


def create_individual():
    genes = [random.randint(0, N - 1) for _ in range(N)]
    fitness = evaluate_fitness(genes)
    return {'genes': genes, 'fitness': fitness}


def evaluate_fitness(genes):
    non_attacking = 0
    for i in range(N):
        for j in range(i + 1, N):
            if genes[i] != genes[j] and abs(genes[i] - genes[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking


def create_population():
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    return sorted(population, key=lambda x: x['fitness'], reverse=True)


def select_parent(population):
    candidates = random.sample(population, 5)
    return max(candidates, key=lambda x: x['fitness'])


def crossover(parent1, parent2):
    point = random.randint(0, N - 1)
    child_genes = parent1['genes'][:point] + parent2['genes'][point:]
    return {'genes': child_genes, 'fitness': evaluate_fitness(child_genes)}

def mutate(individual):
    if random.random() < MUTATION_RATE:
        i = random.randint(0, N - 1)
        individual['genes'][i] = random.randint(0, N - 1)
        individual['fitness'] = evaluate_fitness(individual['genes'])


def evolve_population(population):
    new_generation = population[:10]  # elitismo
    while len(new_generation) < POPULATION_SIZE:
        parent1 = select_parent(population)
        parent2 = select_parent(population)
        child = crossover(parent1, parent2)
        mutate(child)
        new_generation.append(child)
    return sorted(new_generation, key=lambda x: x['fitness'], reverse=True)

def plot_board(genes, generation, fitness):
    plt.figure(figsize=(6, 6))
    plt.title(f"Geração: {generation} | Fitness: {fitness}")
    plt.xticks(range(N))
    plt.yticks(range(N))
    plt.grid(True)
    plt.gca().invert_yaxis()

    for col, row in enumerate(genes):
        plt.plot(col, row, 'ko', markersize=20)  
    plt.show()

def run_genetic_algorithm():
    population = create_population()
    for generation in range(1, MAX_GENERATIONS + 1):
        best = population[0]
        if best['fitness'] == MAX_FITNESS:
            print(f"Solução encontrada na geração {generation}")
            plot_board(best['genes'], generation, best['fitness'])
            return
        if generation % VISUALIZE_EVERY == 0:
            print(f"Geração {generation} | Melhor fitness: {best['fitness']}")
            plot_board(best['genes'], generation, best['fitness'])
        population = evolve_population(population)
    print("Nenhuma solução perfeita encontrada.")
    plot_board(population[0]['genes'], MAX_GENERATIONS, population[0]['fitness'])


run_genetic_algorithm()


#Quando melhora/piora o desempenho do algoritmo na mudança dos parâmetros indicados? 
#R: O desempenho será melhor ou pior irá depender da modificação dos parâmetros. Se tiver aumento na população resultara em um aumento nas chances de encontrar uma solução mais viável. Se a população for grande a demora de processo do algoritmo sera maior e menor se a população for reduzida
