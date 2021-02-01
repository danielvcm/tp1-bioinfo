import sys
from .src.alignment_matrix import AlignmentMatrix


def main():
    """
    Recebe duas strings pela linha de comando e printa a matriz de comparação
    """
    #TODO: ler do arquivo e tratar entrada
    if len(sys.argv)>2:
        matrix = AlignmentMatrix(sys.argv[1],sys.argv[2])
        print(matrix)

