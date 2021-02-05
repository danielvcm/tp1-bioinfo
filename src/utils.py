import sys
from . import user_helpers

def get_params():
    verbose = False
    from_file = False
    sequences = []
    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-v':
            verbose = True
        elif sys.argv[i] == '-h':
            print(user_helpers.help(__file__))
            exit()
        elif sys.argv[i] == '-f':
            from_file = True
            file_name = None
            if len(sys.argv)>i:
                file_name = sys.argv[i+1]
            if not file_name:
                print(user_helpers.file_input_usage())
                exit()
            else:
                sequences = parse_file(file_name)
        else:
            if not from_file:
                sequences.append(sys.argv[i])
    return verbose, sequences

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
                sequences[-1]+=line.strip()
    
    if len(sequences)<2:
        print(f"ERRO: Não foram encontradas sequencias suficientes no arquivo {file_name}")
        print(f"\tSaiba mais sobre o formato FASTA em https://en.wikipedia.org/wiki/FASTA_format")
        exit()
    return sequences

def print_result(align,verbose=False):
    first_result, second_result = align.get_alligned_sequences()
    if verbose:
        print('\n',align)
    print('\nScore:',align.alignment_score,'\n')
    print(first_result)
    print(second_result)