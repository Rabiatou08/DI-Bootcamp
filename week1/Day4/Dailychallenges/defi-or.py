import random

class Gene:
    def __init__(self):
        self.value = random.randint(0, 1)

    def mutate(self):
        if random.random() < 0.5:
            self.value = 1  # mutation toujours vers 1


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            gene.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self, mutation_rate):
        for chromosome in self.chromosomes:
            if random.random() < mutation_rate:
                chromosome.mutate()

    def is_all_ones(self):
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)


class Organism:
    def __init__(self, dna, mutation_rate):
        self.dna = dna
        self.mutation_rate = mutation_rate

    def mutate(self):
        self.dna.mutate(self.mutation_rate)

    def is_perfect(self):
        return self.dna.is_all_ones()


# Simulation
organisms = [Organism(DNA(), mutation_rate=0.9) for _ in range(100)]

generations = 0
winner = None

while not winner:
    generations += 1
    for organism in organisms:
        organism.mutate()
        if organism.is_perfect():
            winner = organism
            break

    if generations % 100 == 0:
        print(f"Génération {generations}...")

print(f"\n ADN parfait trouvé en {generations} générations !")
print("\n Carnet de recherche :")
print(f"- Nombre d'organismes : {len(organisms)}")
print(f"- Taux de mutation : 0.9")
print(f"- Générations nécessaires : {generations}")
print(f"- Conclusion : en mutant toujours vers 1 avec un taux élevé,")
print(f"  le résultat est atteint en quelques dizaines de générations.")