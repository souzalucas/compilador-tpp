import sys
import ply.lex as lex

sucesso = True

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

t_ANY_ignore = ' \t\r\f\v'

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

def t_NUM_NOTACAO_CIENTIFICA(t):
  r'(-|\+)?[\d+]+\.?[\d+]*(e|E)(-|\+)?[\d+]+'
  t.value = float(t.value)
  return t

def t_NUM_PONTO_FLUTUANTE(t):
  r'(-|\+)?[\d+]+\.[\d+]*'
  t.value = float(t.value)
  return t

def t_NUM_INTEIRO(t):
  r'(-|\+)?\d+'
  t.value = int(t.value)
  return t

def t_ID(t):
  r'[a-zA-Z_áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ][a-zA-Z_0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]*'
  t.type = reservadas.get(t.value, 'ID')
  return t

def t_COMENTARIO(t):
  r'(\{(.|\n)*?\})|(\{(.|\n)*?)$'
  t.lexer.lineno += len(t.value.split('\n')) - 1
  pass

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
  global sucesso
  sucesso = False

  print("Caractere Ilegal '%s'" % t.value[0])
  t.lexer.skip(1)

def f_column(token):
  input = token.lexer.lexdata
  line_start = input.rfind('\n', 0, token.lexpos) + 1
  return (token.lexpos - line_start) + 1

def t_ANY_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# Função para imprimir os tokens
def imprimeToken(valor, tipo):
  print(valor, ":", tipo)

# Construindo o lexer
lexer = lex.lex()

# Função para gerar tokens
def geraTokens(dados):

  # Atribuindo os dados ao lexer
  lexer.input(dados)
  
  tokens =  []

  # Imprimindo tokens
  while True:
    tok = lexer.token()
    if not tok: break
  
    tokens.append({
      'token_itself': tok,
      'token': tok.type,
      'value': tok.value,
      'line': tok.lineno,
      'column': f_column(tok)
    })
  
  return tokens, sucesso

# def main():
#   # Arquivo do codigo a ser analisado
#   nome_arquivo = sys.argv[1]

#   # Abrindo e lendo arquivo
#   arquivo = open(nome_arquivo, "r")
#   string_arquivo = arquivo.read()

#   # Gerando tokens
#   geraTokens(string_arquivo)

# main()