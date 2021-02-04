import sys

def get_params():
    verbose = False
    first_sequence = None
    second_sequence = None
    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-v':
            verbose = True
        elif sys.argv[i] == '-h':
            print(user_helpers.help(__file__))
            exit()
        elif sys.argv[i] == '-f':
            file_name = None
            if len(sys.argv)>i:
                file_name = sys.argv[i+1]
            if not file_name:
                print(user_helpers.file_input_usage())
                exit()
            else:
                [first_sequence, second_sequence] = parse_file(file_name)
        else:
            if not first_sequence:
                first_sequence = sys.argv[i]
            elif not second_sequence:
                second_sequence = sys.argv[i]
                break
    return verbose,first_sequence,second_sequence

def parse_file(file_name):
    sequences = []
    new_seq = None
    with open(file_name) as f:
        for line in f:
            if line.startswith('>'):
                new_seq = True
                continue
            elif new_seq:
                sequences.append(line.strip())
                new_seq = False
            elif new_seq == False:
                sequences[-1]+line.strip()

    if len(sequences)>2:
        print(f"AVISO: Apenas as primeiras duas sequencias do arquivo {file_name} serão alinhadas")
    elif len(sequences)<2:
        print(f"ERRO: Não foram encontradas sequencias suficientes no arquivo {file_name}")
        print(f"\tSaiba mais sobre o formato FASTA em https://en.wikipedia.org/wiki/FASTA_format")
        exit()
    return sequences[0], sequences[1]

def print_result(align,verbose=False):
    first_result, second_result = align.get_alligned_sequences()
    if verbose:
        print('\n',align)
    print('\nScore:',align.score_matrix[-1][-1].score,'\n')
    print(first_result)
    print(second_result)