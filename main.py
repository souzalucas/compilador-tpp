import sys
import os

from anytree.exporter import UniqueDotExporter

import sintatico as sin
import semantico as sem
import geracao_codigo as ger

def main():
    arquivo_teste = open(sys.argv[1], 'r', encoding = 'utf-8').read()
    numero_linhas = sum(1 for linha in open(sys.argv[1], 'r', encoding = 'utf-8'))

    # Sintatico
    arvore, sintatico_sucesso = sin.analisador(arquivo_teste, numero_linhas)
    
    # Semantico
    if (sintatico_sucesso):
        UniqueDotExporter(arvore).to_picture("arvore.png")
        arvore, tabela_simbolos, sema_sucesso = sem.semantica(arvore)
        UniqueDotExporter(arvore).to_picture("arvore_podada.png")

        # Geracao de codigo
        if(sema_sucesso):
            ger.gera_codigo(arvore, tabela_simbolos, sema_sucesso)

main()
