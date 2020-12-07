import sys
import ply.lex as lex

reservadas = {
  'retorna': 'RETORNA',
  'leia': 'LEIA',
  'escreva': 'ESCREVA',
  'se': 'SE',
  'então': 'ENTAO',
  'senão': 'SENAO',
  'repita': 'REPITA',
  'até': 'ATE',
  'fim': 'FIM',
  'inteiro': 'INTEIRO',
  'flutuante': 'FLUTUANTE'
}

tokens = [
  'NUM_NOTACAO_CIENTIFICA',
  'NUM_PONTO_FLUTUANTE',
  'NUM_INTEIRO',
  'ID',
  'ATRIBUICAO',
  'DOIS_PONTOS',
  'VIRGULA',
  'ABRE_PARENTESE',
  'FECHA_PARENTESE',
  'ABRE_COLCHETE',
  'FECHA_COLCHETE',
  'MAIS',
  'MENOS',
  'MULTIPLICACAO',
  'DIVISAO',
  'IGUAL',
  'DIFERENTE',
  'MENOR_IGUAL',
  'MAIOR_IGUAL',
  'MENOR',
  'MAIOR',
  'E_LOGICO',
  'OU_LOGICO',
  'NEGACAO'
] + list(reservadas.values())

t_ANY_ignore = ' \t\r\f\v'

# Expressoes Regulares
def t_ATRIBUICAO(t):
  r':='
  return t

def t_DOIS_PONTOS(t):
  r':'
  return t

def t_VIRGULA(t):
  r','
  return t

def t_ABRE_PARENTESE(t):
  r'\('
  return t
  
def t_FECHA_PARENTESE(t):
  r'\)'
  return t

def t_ABRE_COLCHETE(t):
  r'\['
  return t

def t_FECHA_COLCHETE(t):
  r'\]'
  return t

def t_MAIS(t):
  r'\+'
  return t

def t_MENOS(t):
  r'\-'
  return t

def t_MULTIPLICACAO(t):
  r'\*'
  return t

def t_DIVISAO(t):
  r'\/'
  return t

def t_IGUAL(t):
  r'\='
  return t

def t_DIFERENTE(t):
  r'\!'
  return t

def t_MENOR_IGUAL(t):
  r'<='
  return t

def t_MAIOR_IGUAL(t):
  r'>='
  return t

def t_MENOR(t):
  r'<'
  return t

def t_MAIOR(t):
  r'>'
  return t

def t_E_LOGICO(t):
  r'\&\&'
  return t

def t_OU_LOGICO(t):
  r'\|\|'
  return t

def t_NEGACAO(t):
  r'\<\>'
  return t

# Expressoes regulares mais especificas
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

def t_comment(t):
  r'(\{(.|\n)*?\})|(\{(.|\n)*?)$'
  t.lexer.lineno += len(t.value.split('\n')) - 1
  pass

def t_ANY_error(t):
	print('Caracter Inválido \'' + t.value[0] + '\' em ' + str(t.lineno) + ':' + str(f_column(t)))
	t.lexer.skip(1)

def f_column(token):
  input = token.lexer.lexdata
  line_start = input.rfind('\n', 0, token.lexpos) + 1
  return (token.lexpos - line_start) + 1

def t_ANY_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

lexer = lex.lex()

# Função para imprimir os tokens
def imprimeToken(valor, tipo):
  print(valor, ":", tipo)

def geraTokens(data):
  lexer.input(data)

  tokens = []

  while True:
    tokens_gerados = lexer.token()
    if not tokens_gerados: break

    tokens.append({
      'token_itself': tokens_gerados,
      'token': tokens_gerados.type,
      'value': tokens_gerados.value,
      'line': tokens_gerados.lineno,
      'column': f_column(tokens_gerados)
    })

    imprimeToken(tokens_gerados.value, tokens_gerados.type)

  return tokens

nome_arquivo = sys.argv[1]

# Abrindo e lendo arquivo
arquivo = open(nome_arquivo, "r")
string_arquivo = arquivo.read()

# Gerando tokens
geraTokens(string_arquivo)
