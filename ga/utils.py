from .individual import Individual


def calculate_hitchhiker_fitness(answer, individual):
    '''How close is the indivudual to the answer?'''
    guess = int(individual.chromosome.to01(), 2)
    if guess < answer:
        return guess / answer
    else:
        return 2 - (guess / answer)


def initialize(num):
    return [Individual() for _ in range(num)]


def crossover(population):
    for mom, dad in zip(population[0::2], population[1::2]):
        yield mom.reproduce(dad)
        yield mom.reproduce(dad)
