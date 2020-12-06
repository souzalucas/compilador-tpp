import sys
import os

from anytree.exporter import UniqueDotExporter

import sintatico as sin
# import semantico as sem
# import generate_code as gen

def main():
    arquivo_teste = open(sys.argv[1], 'r', encoding = 'utf-8').read()
    numero_linhas = sum(1 for linha in open(sys.argv[1], 'r', encoding = 'utf-8'))

    # Syntax
    arvore, sintatico_sucesso = sin.parser(arquivo_teste, numero_linhas)
    
    # Semantics
    if (sintatico_sucesso):
        # arvore, symbol_table, sema_sucesso = sem.semantics(arvore)
        UniqueDotExporter(arvore).to_picture("program.png")

        # if(sema_success):
        #     gen.gen_code(arvore, symbol_table, sema_success)

main()
