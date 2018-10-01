import copy
import math

from .utils import calculate_hitchhiker_fitness
from .utils import crossover
from .utils import initialize


POP_SIZE = 20
CULL_PCT = 0.25  # bottom percent of population culled per generation
CULL_NUM = math.ceil(POP_SIZE * CULL_PCT)
NUM_GENS = 1000
MUTATION_LIKELIHOOD = 0.25  # chance of gene mutation


def main():
    population = initialize(POP_SIZE)
    top = None

    for generation in range(NUM_GENS):
        # Evaluate fitness and re-order based on scores.
        for individual in population:
            individual.fitness = calculate_hitchhiker_fitness(42, individual)
        population = sorted(population, reverse=True)

        # Cull the bottom performers.
        del population[-CULL_NUM:]

        # Record the top performer.
        if not top:
            top = copy.deepcopy(population[0])
        elif population[0].fitness > top.fitness:
            top = copy.deepcopy(population[0])

        print('generation {}: {} {}'.format(generation, top.fitness,
                                            top))
        if top.fitness == 1.0:
            break

        # Perform genetic crossover.
        children = list(crossover(population))

        # Mutate the top performers.
        mutated_individuals = [individual.mutate(MUTATION_LIKELIHOOD)
                               for individual in population[:CULL_NUM]]

        # Re-group children and mutated
        population = children + mutated_individuals


if __name__ == '__main__':
    main()
