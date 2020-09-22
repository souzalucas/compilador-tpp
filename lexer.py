import sys
import ply.lex as lex

# Lista de palavras reservadas
reservadas = {
    'se'        : 'SE',
    'repita'    : 'REPITA',
    'fim'       : 'FIM',
    'leia'      : 'LEIA',
    'retorna'   : 'RETORNA',
    'escreva'   : 'ESCREVA',
    'inteiro'   : 'INTEIRO',
    'flutuante' : 'FLUTUANTE',
    'até'       : 'ATE',
    'senão'     : 'SENAO',
    'então'     : 'ENTAO'
}

# Lista de nomes de tokens com as palavras reservadas
tokens = ['MAIS', 'MENOS', 'MULTIPLICACAO', 'DIVISAO', 'DOIS_PONTOS', 'VIRGULA', 'MENOR', 'MAIOR', 'IGUAL', 'DIFERENTE', 'MENOR_IGUAL', 'MAIOR_IGUAL', 'E_LOGICO', 'OU_LOGICO', 'NEGACAO', 'ABRE_PARENTESE', 'FECHA_PARENTESE', 'ABRE_COLCHETE', 'FECHA_COLCHETE', 'ATRIBUICAO', 'NUM_INTEIRO', 'NUM_PONTO_FLUTUANTE', 'NUM_NOTACAO_CIENTIFICA', 'ID', 'COMENTARIO'] + list(reservadas.values())
 
# Expressões regulares para tokens simples
t_MAIS              = r'\+'
t_MENOS             = r'-'
t_MULTIPLICACAO     = r'\*'
t_DIVISAO           = r'/'
t_DOIS_PONTOS       = r':'
t_VIRGULA           = r','
t_MENOR             = r'<'
t_MAIOR             = r'>'
t_IGUAL             = r'='
t_DIFERENTE         = r'<>'
t_MENOR_IGUAL       = r'<='
t_MAIOR_IGUAL       = r'>='
t_E_LOGICO          = r'\&\&'
t_OU_LOGICO         = r'\|\|'
t_NEGACAO           = r'!'
t_ABRE_PARENTESE    = r'\('
t_FECHA_PARENTESE   = r'\)'
t_ABRE_COLCHETE     = r'\['
t_FECHA_COLCHETE    = r'\]'
t_ATRIBUICAO        = r':='
t_ignore            = ' \t'   # espacos e tabulacoes
t_ID = r'[a-zA-Z_]+[a-zA-Z_0-9]*'
t_COMENTARIO = r'\{[^\}]+?\}'
t_NUM_INTEIRO = r'[-\+]?[0-9]+'
t_NUM_PONTO_FLUTUANTE = r'[+-]?([0-9]+[.]([0-9]*)?|[.][0-9]+)'
t_NUM_NOTACAO_CIENTIFICA = r'([+-]?([0-9]+[.]([0-9]*)?|[.][0-9]+)|([0-9]+))([eE][-+]?\d+)'

# Expressão Regular para a palavra reservada 'senão'
def t_SENAO(t):
    r'senão'
    t.type = reservadas.get(t.value,'SENAO')
    return t

# Expressão Regular para a palavra reservada 'então'
def t_ENTAO(t):
    r'então'
    t.type = reservadas.get(t.value,'ENTAO')
    return t

# Expressão Regular para a palavra reservada 'até'
def t_ATE(t):
    r'até'
    t.type = reservadas.get(t.value,'ATE')
    return t
    
# Expressão regular para quebra de linha
def t_NOVA_LINHA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# Erro
def t_error(t):
    print("Caractere Ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Função para imprimir os tokens
def imprimeToken(valor, tipo):
    print(valor, ":", tipo)

# Função para gerar tokens
def geraTokens(dados):
    # Construindo o lexer
    lexer = lex.lex()

    # Atribuindo os dados ao lexer
    lexer.input(dados)
    
    # Imprimindo tokens
    while True:
        tok = lexer.token()
        if not tok: 
            break
        imprimeToken(tok.value, tok.type)

def main():
    # Arquivo do codigo a ser analisado
    nome_arquivo = sys.argv[1]

    # Abrindo e lendo arquivo
    arquivo = open(nome_arquivo, "r")
    string_arquivo = arquivo.read()
    
    # Gerando tokens
    geraTokens(string_arquivo)

main()