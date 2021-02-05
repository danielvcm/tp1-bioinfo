
def usage(file_name):
    return f"""
 ---------------------------
|    Trabalho Pratico 1     |
| Alinhamento de sequencias |
 ---------------------------

$ python3 {file_name} SEQUENCIA1 SEQUENCIA
obtem a pontuação do alinhamento e as sequencias resultantes

$ python3 {file_name} -h
traz mais informacoes sobre argumentos e parametros opcionais
            """

def help(file_name):
    return f"""
 ---------------------------
|    Trabalho Pratico 1     |
| Alinhamento de sequencias |
|           AJUDA           |
 ---------------------------
           EXECUÇÃO
$ python3 {file_name} SEQUENCIA1 SEQUENCIA
obtem a pontuação do alinhamento e as sequencias resultantes

           FLAGS
    -h          ajuda
    -f          especifica um arquivo FASTA de input
    -v          modo verboso, imprime matriz de alinhamento
                alem da pontuacao e as sequencias resultantes
    """

def file_input_usage():
    return "ERRO: Um arquivo no formato FASTA deve ser especificado depois da flag -f"