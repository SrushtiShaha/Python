import random

# Configuration
POP_SIZE = 6          # Number of individuals in the population
GENOME_LEN = 5        # 5 bits for range 0-31
ITERATIONS = 5        # Run for 5 generations
MUTATION_RATE = 0.05  # Probability of a bit flipping


def decode(chromosome):
    """Converts a binary list to a decimal integer."""
    return int("".join(map(str, chromosome)), 2)


def fitness_func(chromosome):
    """Calculates fitness: f(x) = x^2."""
    x = decode(chromosome)
    return x ** 2


def create_initial_population(size, length):
    """Generates a random initial population of bit strings."""
    return [[random.randint(0, 1) for _ in range(length)] for _ in range(size)]


def selection(population, fitnesses):
    """Roulette wheel selection: favors individuals with higher fitness."""
    selected = random.choices(population, weights=fitnesses, k=len(population))
    return selected


def crossover(parent1, parent2):
    """Single-point crossover at a random index."""
    cp = random.randint(1, GENOME_LEN - 1)
    child1 = parent1[:cp] + parent2[cp:]
    child2 = parent2[:cp] + parent1[cp:]
    return child1, child2


def mutate(chromosome):
    """Randomly flips bits based on the mutation rate."""
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome


# --- Execution Loop ---
population = create_initial_population(POP_SIZE, GENOME_LEN)

print(f"{'Gen':<5} | {'Best x':<8} | {'Best f(x)':<10} | {'Avg Fitness'}")
print("-" * 45)

for i in range(1, ITERATIONS + 1):
    fitnesses = [fitness_func(ind) for ind in population]

    # Track results
    best_idx = fitnesses.index(max(fitnesses))
    avg_fit = sum(fitnesses) / POP_SIZE

    print(f"{i:<5} | {decode(population[best_idx]):<8} | {max(fitnesses):<10} | {avg_fit:.2f}")

    # 1. Selection
    mating_pool = selection(population, fitnesses)

    # 2. Crossover
    next_gen = []
    for j in range(0, POP_SIZE, 2):
        p1, p2 = mating_pool[j], mating_pool[j + 1]
        c1, c2 = crossover(p1, p2)
        next_gen.extend([c1, c2])

    # 3. Mutation
    population = [mutate(ind) for ind in next_gen]


best_final = max(population, key=fitness_func)
print(f"\nFinal Result: x = {decode(best_final)}, f(x) = {fitness_func(best_final)}")