import random
import string

# Target password
TARGET = "University"
POP_SIZE = 100
MUTATION_RATE = 0.1
GENES = string.ascii_letters + " "

# Generate random string
def create_individual():
    return ''.join(random.choice(GENES) for _ in range(len(TARGET)))


# Fitness function (count matching characters)
def fitness(individual):
    return sum(1 for i in range(len(TARGET)) if individual[i] == TARGET[i])


# Selection (top individuals)
def selection(population):
    population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return population[:POP_SIZE // 2]


# Crossover (combine two parents)
def crossover(parent1, parent2):
    point = random.randint(0, len(TARGET) - 1)
    child = parent1[:point] + parent2[point:]
    return child


# Mutation (change one random letter)
def mutate(individual):
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, len(TARGET) - 1)
        new_char = random.choice(GENES)
        individual = individual[:idx] + new_char + individual[idx + 1:]
    return individual


# Genetic Algorithm
def genetic_algorithm():
    population = [create_individual() for _ in range(POP_SIZE)]
    generation = 0

    while True:
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        best = population[0]

        print(f"Generation {generation}: {best} (Fitness: {fitness(best)})")

        if best == TARGET:
            print("\nPassword found!")
            break

        selected = selection(population)
        new_population = []

        while len(new_population) < POP_SIZE:
            parent1 = random.choice(selected)
            parent2 = random.choice(selected)

            child = crossover(parent1, parent2)
            child = mutate(child)

            new_population.append(child)

        population = new_population
        generation += 1


# Run
genetic_algorithm()