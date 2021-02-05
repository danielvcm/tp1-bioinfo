from src.pairwise_alignment import PairWiseAlignment
import os
from dotenv import load_dotenv
import heapq as hp

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
        self.alignment_mapping = {}
        self.scores = []
        self.final_consensus = ''

    def align(self):
        self.calculate_scores_matrix()
        self.assemble_final_consensus()
        return self.get_aligned_sequences()

    def assemble_final_consensus(self):
        trash_of_sequences = set()
        consensus = ''
        while len(self.alignment_mapping) > 1:

            seq1, seq2 = self.get_viable_sequences(trash_of_sequences)

            align = PairWiseAlignment(seq1, seq2) # TODO: nao seira o caso de guardar isso? pq tô fazendo 2x
            aligned_1, aligned_2 = align.get_alligned_sequences()

            consensus = self.get_consensus_string(aligned_1, aligned_2)

            # get remaining sequences
            present_sequences = set([seq1, seq2])
            all_sequences = set(self.alignment_mapping.keys())
            remaining_sequences = all_sequences - present_sequences

            self.alignment_mapping[consensus] = {}

            self.update_scores_mapping(consensus, present_sequences, remaining_sequences)

            del self.alignment_mapping[seq1]
            del self.alignment_mapping[seq2]

        self.final_consensus = consensus


    def update_scores_mapping(self, consensus, present_sequences, remaining_sequences):
        for rem_seq in remaining_sequences:
            new_score = 0
            for pres_seq in present_sequences:
                new_score += self.alignment_mapping.get(rem_seq).get(pres_seq) or \
                             self.alignment_mapping.get(pres_seq).get(rem_seq)
            new_score /= 2
            # print(new_score)
            self.alignment_mapping[consensus][rem_seq] = new_score
            tup = (-new_score, rem_seq, consensus)  # o negativo é pra fazer maxheap
            hp.heappush(self.scores, tup)

    def get_viable_sequences(self, trash_of_sequences):

        # pop na heap
        while (True):
            score, seq1, seq2 = hp.heappop(self.scores)
            if seq1 not in trash_of_sequences and seq2 not in trash_of_sequences:
                break
        # essas sequencias não poderão ser reutilizadas
        trash_of_sequences.add(seq1)
        trash_of_sequences.add(seq2)
        return seq1, seq2

    def get_consensus_string(self, aligned_1, aligned_2):
        consensus = ''
        for pos in range(len(aligned_1)):
            if aligned_1[pos] == aligned_2[pos]:
                consensus = consensus + aligned_1[pos]
            else:
                consensus = consensus + 'X'
        return consensus

    def get_aligned_sequences(self):

        # cria um vetor de string alinhadas
        aligned_sequences = ['' for _ in range(len(self.sequences))]

        # cria um vetor de índices
        current_index = [len(seq)-1 for seq in self.sequences]

        for idx in reversed(range(0, len(self.final_consensus))):
            consensus_char = self.final_consensus[idx]
            #print("lookin at char", consensus_char)

            if consensus_char != 'X':
                for sequence_id, seq in enumerate(self.sequences):
                    aligned_sequences[sequence_id] = consensus_char + aligned_sequences[sequence_id]

            # analisar a letra na posição corresondente em todas as seq
            majority = None
            for sequence_id, seq in enumerate(self.sequences):
                # se a seq já tiver acabado, printa '-'
                # if current_index[sequence_id] < 0:
                #     aligned_sequences[sequence_id] = '-' + aligned_sequences[sequence_id]
                if seq[current_index[sequence_id]] == consensus_char:
                    aligned_sequences[sequence_id] = consensus_char + aligned_sequences[sequence_id]
                    current_index[sequence_id] -= 1
                else:
                    aligned_sequences[sequence_id] = '-' + aligned_sequences[sequence_id]

                # caso a seq[pos] tenha a mesma letra nessa posição, printa ela, e reduz o indice
                # caso não seja, printa '-' e não diminui o índice

        return aligned_sequences

    def calculate_scores_matrix(self):
        n = len(self.sequences)

        # assemble mapping
        for i in range(n):
            seq1 = self.sequences[i]
            self.alignment_mapping[seq1] = {}
            for j in range(i + 1, n):
                seq2 = self.sequences[j]
                align = PairWiseAlignment(seq1, seq2)
                self.alignment_mapping[seq1][seq2] = align.alignment_score

                tup = (-align.alignment_score, seq1, seq2)  # o negativo é pra fazer maxheap
                hp.heappush(self.scores, tup)


        # for string in self.sequences:
        #     mapping[string]= {}
        #     for string2 in self.sequences:
        #         if string2 != string:
        #             mapping[string][string2] = None


        #
        # self.alignment_matrix = [[None for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         align = PairWiseAlignment(self.sequences[i], self.sequences[j])
        #         score = align.alignment_score
        #         tup = (-score, self.sequences[i], self.sequences[j])  # o negativo é pra fazer maxheap
        #         hp.heappush(self.scores, tup)
        #         self.alignment_matrix[i][j] = score

