import os
class AlignmentCell:
    """
    A cell of the alignment matrix
    args: score: int
        direction: str {'v','h','d'}
    """
    def __init__(self, score, direction):
        self.score = score
        self.direction = direction
    def __repr__(self) -> str:
        return str(self.score)+' '+self.direction

class AlignmentMatrix:

    def __init__(self,first_sequence,second_sequence):
        if type(first_sequence)!=str:
            raise TypeError(f"first_sequence must be a string not {type(first_sequence)}")
        self.first_sequence = '*'+first_sequence

        if type(second_sequence)!=str:
            raise TypeError(f"second_sequence must be a string not {type(second_sequence)}")
        self.second_sequence = '*'+second_sequence
        self.fill_score_matrix()
    
    def fill_score_matrix(self):
        indel_score = int(os.getenv("INDEL"))
        match_score = int(os.getenv("MATCH"))
        blosum = dict(os.getenv("BLOSUM62"))
        self.score_matrix = []
        for i in range(len(self.second_sequence)):
            for j in range(len(self.first_sequence)):
                #comecou uma nova linha na matriz
                if self.first_sequence[j]=='*':
                    self.score_matrix.append([AlignmentCell(0,'stop')])
                #eh a linha inicial da segunda sequencia, já existe a lista desta linha
                elif self.second_sequence[i]=='*':
                    self.score_matrix[i].append(AlignmentCell(0,'stop'))
                else:
                    vertical = self.score_matrix[i-1][j].score+indel_score
                    horizontal = self.score_matrix[i][j-1].score+indel_score
                    #por enquanto estou ignorando mismatch
                    #TODO: considerar blosum62 [2,3]
                    diagonal = self.score_matrix[i-1][j-1].score+match_score if self.first_sequence[i]==self.second_sequence[j] else 0
                    score = max(horizontal,vertical,diagonal)
                    if score == horizontal:
                        self.score_matrix[i].append(AlignmentCell(score,'h'))
                    elif score == vertical:
                        self.score_matrix[i].append(AlignmentCell(score,'v'))
                    else:
                        self.score_matrix[i].append(AlignmentCell(score,'d'))
    
    def __repr__(self) -> str:
        s = ''
        for l in range(len(self.first_sequence)):
            s+=str(self.first_sequence[l])+'\t'
        s+='\n'
        for l in range(len(self.score_matrix)):
            s+=str(self.second_sequence[l])+' '+str(self.score_matrix[l])+'\n'
        return s


