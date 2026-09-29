import random
import math

# Target constants
TARGET_1 = math.pi
TARGET_2 = math.sqrt(50)

# GA Parameters
POP_SIZE = 100
GENERATIONS = 500
MUTATION_RATE = 0.1
GENE_RANGE = (0, 10)


def fitness(individual):
    """Calculates fitness: closer to targets means higher fitness."""
    v1, v2 = individual
    error = abs(v1 - TARGET_1) + abs(v2 - TARGET_2)
    return 1 / (1 + error)


def create_individual():
    """Generates a random individual [val1, val2]."""
    return [
        random.uniform(*GENE_RANGE),
        random.uniform(*GENE_RANGE)
    ]


def crossover(parent1, parent2):
    """Blends two parents to create a child."""
    return [(p1 + p2) / 2 for p1, p2 in zip(parent1, parent2)]


def mutate(individual):
    """Applies random small changes to genes."""
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] += random.uniform(-0.1, 0.1)
    return individual


# 1. Initialize Population
population = [create_individual() for _ in range(POP_SIZE)]

# 2. Evolution Loop
for gen in range(GENERATIONS):
    # Sort population by fitness
    population.sort(key=fitness, reverse=True)

    # Selection
    next_generation = population[:10]

    # Reproduction
    while len(next_generation) < POP_SIZE:
        p1, p2 = random.sample(population[:50], 2)
        child = crossover(p1, p2)
        child = mutate(child)
        next_generation.append(child)

    population = next_generation


# Results
best = population[0]

print(f"Results after {GENERATIONS} generations:")
print(f"Gene 1: {best[0]:.8f} (Target Pi: {TARGET_1:.8f})")
print(f"Gene 2: {best[1]:.8f} (Target Sqrt(50): {TARGET_2:.8f})")
print(f"Best Fitness Score: {fitness(best):.8f}")