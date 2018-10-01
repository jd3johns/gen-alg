from ga.individual import Individual
from ga.utils import calculate_hitchhiker_fitness


def test_hitchhiker_fitness_lt():
    answer = 42
    individual = Individual(chromosome='{:06b}'.format(50))

    expected = (answer - 8) / answer

    fitness = calculate_hitchhiker_fitness(answer, individual)

    assert expected == fitness


def test_hitchhiker_fitness_gt():
    answer = 42
    individual = Individual(chromosome='{:06b}'.format(30))

    expected = 30 / answer

    fitness = calculate_hitchhiker_fitness(answer, individual)

    assert expected == fitness
