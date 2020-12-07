# Análise Sintática (Trabalho - 2ª parte)

A análise sintática é responsável por gerar, a partir de um conjunto de regras e dos tokens gerados pelo analisador léxico, uma árvore sintática contendo toda a estrutura do programa de entrada. Esta árvore será útil para a construção da tabela semântica, que é a próxima etapa do desenvolvimento do compilador.

## Gramática no padrão BNF

A gramática da linguagem T++ é definida por um conjunto de regras descritas no padrão BNF. A lista contendo todas as regras utilizadas para criação do analisador sintático encontra-se disponível no link a seguir: <https://docs.google.com/document/d/1oYX-5ipzL_izj_hO8s7axuo2OyA279YEhnAItgXzXAQ/edit?usp=sharing>

## Formato de análise

O formato da análise sintática nos diz a forma como a árvore gerada será percorrida. Alguns métodos possíveis são LL, LR, LALR, SLR. Para esse compilador, utilizaremos o método LALR utilizado pelo yacc. O yacc é uma ferramenta desenvolvida para Python responsável pela execução do analisador sintático.

O método LALR funciona da seguinte forma: uma tabela de regras é gerada a partir da execução do analisador sintático. Essa tabela é gerada com base no método LR, que significa left to right.

## Implementação

Para a implementação, foi criada uma função para cada regra. Cada função contém um cabeçalho com a própria regra em si, que será usada para a execução do parser pelo yacc. Nas próprias funções já temos o código necessário para a geração da árvore sintática.

O yacc, como mencionado é a ferramenta do python responsável por realizar o parser do analisador sintático. O yacc é uma ferramenta que se encontra dentro do PLY, biblioteca do python responsável por conter ferramentas léxicas e sintáticas para desenvolvimento de compiladores. O yacc, por sua vez, provê suporte eficiente e adequado para criação de gramáticas e também dá suporte para tratamento de problemas com regras vazias e gramáticas ambíguas. O analisador sintático acusa erros sintáticos da linguagem. A árvore sintática gerada será utilizada posteriormente para a análise semântica do programa de entrada. Ela contém todas as ramificações de tudo o que contém no programa de entrada. A árvore gerada será podada na análise semântica e será utilizada para criacão das regras semânticas.

A seguir temos um código que exemplifica a criação das funções do analisador sintático.

```python
def p_programa(p):
  '''
    programa : lista_declaracoes
  '''

  p[0] = Node('programa', value = 'programa', children = [p[1]])

def p_lista_declaracoes(p):
  '''
    lista_declaracoes : lista_declaracoes declaracao
                        | declaracao
  '''

  if(len(p) == 3):
    p[0] = Node('lista_declaracoes', value = 'lista_declaracoes', children = [p[1], p[2]])
  else:
    p[0] = Node('lista_declaracoes', value = 'lista_declaracoes', children = [p[1]])

def p_declaracao(p):
  '''
    declaracao : declaracao_variaveis
                | inicializacao_variaveis
                | declaracao_funcao
  '''

  p[0] = Node('declaracao', value = 'declaracao', children = [p[1]])
```

Para a geração da árvore, o seguinte código é utilizado.

```python
def main():
  arquivo_teste = open(sys.argv[1], ’r’, encoding = ’utf-8’).read()
  numero_linhas = sum(1 for linha in open(sys.argv[1], 'r', encoding = 'utf-8'))

  # Analisador sintático, execucao
  arvore, sintatico_sucesso = sin.analisador(arquivo_teste, numero_linhas)

  # Gravando árvore em uma imagem
  if (sintatico_sucesso):
    UniqueDotExporter(arvore).to_picture("programa.png")
```

Abaixo temos um exemplo de árvore gerada a partir do analisador sintático

<p align="center">
  <img src="programa.png"/>
</p>