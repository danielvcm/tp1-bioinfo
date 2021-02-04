from src.pairwise_alignment import PairWiseAlignment
import os
from dotenv import load_dotenv
import heapq as hp
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO

class MultipleAlignment:
    """
    2 - fazer o upgma

    > ({abc, bcd}, 10) -> nova sequencia xabcx. Atualiza
    ({abc, acd}, 20) ->
    ({bcd, acd}, 30)

    3 - construir consensos
    (stringA, stringB, valor de alinhamento, consenso)
    (stringC, stringD, valor de alinhamento, consenso)
    """
    def __init__(self, sequences):
        self.sequences = sequences
        self.alignment_matrix = None
        self.scores = []

    def align(self):
        self.calculate_scores_matrix()
        return self.generate_dendogram()

    def generate_dendogram(self):
        # constructor = DistanceTreeConstructor(distance_calculator=self.alignment_matrix, method='upgma')
        constructor = DistanceTreeConstructor()
        return constructor.upgma(self.alignment_matrix)


    def calculate_scores_matrix(self):
        # mapping = {}
        # # assemble mapping
        # for string in strings:
        #     mapping[string]= {}
        #     for string2 in strings:
        #         if string2 != string:
        #             mapping[string][string2] = None
        # for thing in mapping:
        #     print(thing, ":", mapping[thing])

        n = len(self.sequences)
        self.alignment_matrix = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                align = PairWiseAlignment(self.sequences[i], self.sequences[j])
                score = align.alignment_score
                tup = (-score, self.sequences[i], self.sequences[j])  # o negativo é pra fazer maxheap
                hp.heappush(self.scores, tup)
                self.alignment_matrix[i][j] = score

