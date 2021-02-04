import os
from src.blosum import blosum

class AlignmentCell:
    """
    A cell of the alignment matrix
    args: score: int
        direction: str {'_','|','\\','.'}
    """
    def __init__(self, score, direction):
        self.score = score
        self.direction = direction

    def __repr__(self) -> str:
        return str(self.score)+' '+self.direction


# noinspection SpellCheckingInspection
class PairWiseAlignment:
    def __init__(self, first_sequence, second_sequence):
        self.first_sequence = first_sequence
        self.second_sequence = second_sequence
        self.indel_score = int(os.getenv("INDEL"))
        self.validate_input()
        self.score_matrix = [[] for _ in range(len(self.second_sequence))]
        self.alignment_score = 0
        self.calculate_alignment()

    def calculate_alignment(self):
        self.fill_first_row_and_column()
        self.fill_score_matrix()


    def validate_input(self):
        if type(self.first_sequence)!=str:
            raise TypeError(f"first_sequence must be a string not {type(self.first_sequence)}")
        if type(self.second_sequence)!=str:
            raise TypeError(f"second_sequence must be a string not {type(self.second_sequence)}")
        self.first_sequence = '*' + self.first_sequence.upper()
        self.second_sequence = '*' + self.second_sequence.upper()


    def fill_first_row_and_column(self):

        # fill line
        self.score_matrix[0].append(AlignmentCell(0, '.'))
        for i in range(1, len(self.first_sequence)):
            score = self.score_matrix[0][i-1].score + self.indel_score
            self.score_matrix[0].append(AlignmentCell(score, '.'))

        # fill column
        for i in range(1, len(self.second_sequence)):
            score = self.score_matrix[i-1][0].score + self.indel_score
            self.score_matrix[i].append(AlignmentCell(score, '.'))

    def fill_score_matrix(self):
        print("Filling score matrix")
        for i in range(1, len(self.second_sequence)):
            for j in range(1, len(self.first_sequence)):

                try:
                    blosum_score = blosum[self.second_sequence[i]][self.first_sequence[j]]
                except:
                    raise Exception("Entrada com alguma proteina não existente na BLOSUM62")

                vertical = self.score_matrix[i-1][j].score + self.indel_score
                horizontal = self.score_matrix[i][j-1].score + self.indel_score
                diagonal = self.score_matrix[i - 1][j - 1].score + blosum_score

                if self.second_sequence[i] == self.first_sequence[j]:
                    self.score_matrix[i].append(AlignmentCell(diagonal, '\\'))
                else:
                    score = max(horizontal, vertical, diagonal)
                    if score == diagonal:
                        self.score_matrix[i].append(AlignmentCell(score,'\\'))
                    elif score == horizontal:
                        self.score_matrix[i].append(AlignmentCell(score,'_'))
                    elif score == vertical:
                        self.score_matrix[i].append(AlignmentCell(score,'|'))

        self.alignment_score = self.score_matrix[-1][-1].score

    def get_alligned_sequences(self):
        print("Getting aligned sequences")
        row = len(self.second_sequence) - 1
        col = len(self.first_sequence) - 1
        first_seq = ''
        second_seq = ''

        while row > 0 and col > 0 and self.score_matrix[row][col].direction != '.':
            if self.score_matrix[row][col].direction == '\\':
                first_seq = self.first_sequence[col] + first_seq
                second_seq = self.second_sequence[row] + second_seq
                row -= 1
                col -= 1
            elif self.score_matrix[row][col].direction == '_':
                print("B")
                first_seq = self.first_sequence[col] + first_seq
                second_seq = '-' + second_seq
                col -= 1
            elif self.score_matrix[row][col].direction == '|':
                first_seq = '-' + first_seq
                second_seq = self.second_sequence[row] + second_seq
                row -=1

        return first_seq, second_seq

    def __repr__(self) -> str:
        s = '   '
        for l in range(len(self.first_sequence)):
            s+=str(self.first_sequence[l])+',   '
        s+='\n'
        for l in range(len(self.score_matrix)):
            s+=str(self.second_sequence[l])+' '+ str(self.score_matrix[l])+'\n'
        return s




