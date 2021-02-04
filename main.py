import sys

import src.user_helpers as user_helpers
from dotenv import load_dotenv
from src.alignment_matrix import AlignmentMatrix
from src.utils import get_params, parse_file, print_result


def main():
    """
    #### Alinhamento de sequencias
            EXECUÇAO
    $ python3 main.py SEQUENCIA1 SEQUENCIA2\n
    obtem a pontuação do alinhamento e as sequencias resultantes\n
            FLAGS\n
        -h          ajuda
        -f          especifica um arquivo FASTA de input
        -v          modo verboso, imprime matriz de alinhamento
                    alem da pontuacao e as sequencias resultantes
    """
    if len(sys.argv)>=2:
        verbose, first_sequence, second_sequence = get_params()
        if first_sequence and second_sequence:
            align = AlignmentMatrix(first_sequence,second_sequence)
            print_result(align, verbose=True)
        else:
            print(user_helpers.usage(__file__))
    else:
        print(user_helpers.usage(__file__))


if "__main__"==__name__:
    load_dotenv()
    main()