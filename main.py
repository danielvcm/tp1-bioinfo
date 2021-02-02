import sys

from dotenv import load_dotenv
from src.alignment_matrix import AlignmentMatrix


def main():
    """
    Recebe duas strings pela linha de comando e printa a matriz de comparação
    """
    #TODO: ler do arquivo e tratar entrada
    if len(sys.argv)>2:
        align = AlignmentMatrix(sys.argv[1],sys.argv[2])
        score_matrix, first_seq, second_seq = align.calculate_alignment()
        print(align)
        print(first_seq)
        print(second_seq)


if "__main__"==__name__:
    load_dotenv()
    main()