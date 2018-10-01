'''
Process:
    1. Define a genetic representation of the solution domain.
    2. Define a fitness function.
    3. Initiailize a population of size N (individuals may be seeded where an
       optimum solution is expected to be found).
    4. Measure the fitness of the population.
    5. Record the fittest M individuals.
    6. Apply the following operations to produce a new cohort of size N:
        * mutation
        * crossover
        * selection
        * inversion
    7. Repeat steps 4-6 until a satisfactory solution is found or the maximum
       number of generations have been tested.
'''
import random

from bitarray import bitarray


CHROM_LEN = 6


class Individual():
    _obj_count = 0

    def __init__(self, chromosome=None):
        if chromosome and len(chromosome) != CHROM_LEN:
            raise ValueError('chromosome length must be {}, got '
                             '{}'.format(CHROM_LEN, chromosome))

        self._id = Individual._obj_count
        Individual._obj_count += 1

        chromosome = chromosome or ''.join([str(random.randint(0, 1))
                                            for _ in range(CHROM_LEN)])
        self.chromosome = bitarray(chromosome)
        self.fitness = 0.

    def mutate(self, likelihood):
        '''Mutate (i.e. flip) each gene with constant likelihood.'''
        for i in range(CHROM_LEN):
            if random.uniform(0, 1) < likelihood:
                self.chromosome[i] = not self.chromosome[i]

        return self

    def reproduce(self, individual):
        '''Uniform crossover for each gene.'''
        chromosome = bitarray(CHROM_LEN)
        for i in range(CHROM_LEN):
            if random.randint(0, 1):
                chromosome[i] = self.chromosome[i]
            else:
                chromosome[i] = individual.chromosome[i]

        return Individual(chromosome=chromosome)

    def __lt__(self, rhs):
        return self.fitness < rhs.fitness

    def __repr__(self):
        return str({'id': self._id, 'fitness': self.fitness,
                    'chromosome': self.chromosome.to01()})
