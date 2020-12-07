# Compilador TPP

[Analise Sintática] (doc_lexico.md)

[Analise Léxica] (doc_lexico.md)

# Análise Léxica (Trabalho - 1ª parte)

O analisador léxico realiza uma varredura em todo o código-fonte em T++ e gera uma lista de tokens. Um token é uma marca que representa uma unidade. A lista de tokens será fundamental para as próximas etapas do compilador. Para desenvolvimento do analisador léxico foi utilizado a biblioteca PLY.
## Linguagem de programação T++

O T++ utilizado neste trabalho é uma linguagem de programação simples, desenvolvida para fins didáticos a ser utilizada para a fixação dos conteúdos da disciplina de compiladores.

Esta linguagem possui suas palavras-chave em português. Os tipos de variáveis suportados são inteiro, flutuante e notação científica. Há suporte para estrutura condicional "se-entao-senão", bem como a estrutura de repetição "repita-até". Além disso, a linguagem suporta operadores lógicos e aritméticos. Também é possível ler e escrever
dados no terminal, criar vetores e funcões.

Mais detalhes do analisador léxico serão apresentados a seguir.

## Palavras reservadas
Abaixo temos as palavras reservadas da linguagem e seus respectivos tokens.

|PALAVRA RESERVADA|TOKEN|
|:-|:-|
|se|SE|
|repita|REPITA|
|fim|FIM|
|leia|LEIA|
|retorna|RETORNA|
|escreva|ESCREVA|
|inteiro|INTEIRO|
|flutuante|FLUTUANTE|
|até|ATE|
|senão|SENAO|
|então|ENTAO|

## Expressões regulares
Foram utilizadas expressões regulares para reconhecimento dos tokens em T++. No total foram 36 expressões regulares para das palavras-chave, operadores lógicos e aritméticos, numerais e símbolos, como igual, dois pontos, colchetes e parenteses.

|EXPRESSÃO REGULAR|TOKEN|
|:-|:-|
|r'\+'|MAIS|
|r'-'|MENOS|
|r'\*'|MULTIPLICACAO|
|r'/' |DIVISAO|
|r':'|DOIS_PONTOS|
|r','|VIRGULA|
|r'<'|MENOR|
|r'>'|MAIOR|
|r'='|IGUAL|
|r'<>'|DIFERENTE|
|r'<='|MENOR_IGUAL|
|r'>='|MAIOR_IGUAL|
|r'\\&\\&'|E_LOGICO|
|r'\\\|\\\|'|OU_LOGICO|
|r'!'|NEGACAO|
|r':='|ATRIBUICAO|
|r'\\('|ABRE_PARENTESE|
|r'\\)'|FECHA_PARENTESE|
|r'\\['|ABRE_COLCHETE|
|r'\\]'|FECHA_COLCHETE| 
|r'[a-zA-Z_áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ][a-zA-Z_0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]*'|ID|
|r'(-\|\\+)?\d+'|NUM_INTEIRO|
|r'(-\|\\+)?[\d+]+\\.[\d+]*'|NUM_PONTO_FLUTUANTE|
|r'(-\|\\+)?[\d+]+\\.?[\d+]*(e\|E)(-\|\\+)?[\d+]+'|NUM_NOTACAO_CIENTIFICA|
|r'se'|SE|
|r'então'|ENTAO|
|r'senão'|SENAO|
|r'fim'|FIM|
|r'repita'|REPITA|
|r'até'|ATE|
|r'leia'|LEIA|
|r'escreva'|ESCREVA|
|r'retorna'|RETORNA|
|r'inteiro'|INTEIRO|
|r'flutuante'|FLUTUANTE|

## Autômatos para geração de tokens
Os autômatos finitos que representam as expressões regulares utilizadas estão no seguinte link: <https://docs.google.com/document/d/1MsXd_C5zmrnNvaq3RI7FepmpKVP5LPnUKePc4ihThZc/edit?usp=sharing>.

## Implementação

### PLY (Python Lex-Yacc)
Para a varredura e busca dos tokens foi utilizada a biblioteca PLY do Python. PLY é uma implementação de ferramentas de análise lex e yacc para Python.

### Detalhes do código
Primeiramente, foi criado um dicionário contendo todas as palavras reservadas como chave, e seus respectivos tokens como valor.

```python
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
```
Logo após, foi criada uma lista com todos os tokens da linguagem.

```python
tokens = ['MAIS', 'MENOS', 'MULTIPLICACAO', 'DIVISAO', 
          'DOIS_PONTOS', 'VIRGULA', 'MENOR', 'MAIOR', 
          'IGUAL', 'DIFERENTE', 'MENOR_IGUAL', 'MAIOR_IGUAL', 
          'E_LOGICO', 'OU_LOGICO', 'NEGACAO', 'ABRE_PARENTESE', 
          'FECHA_PARENTESE', 'ABRE_COLCHETE', 'FECHA_COLCHETE', 
          'ATRIBUICAO', 'NUM_INTEIRO', 'NUM_PONTO_FLUTUANTE', 
          'NUM_NOTACAO_CIENTIFICA', 'ID'] + list(reservadas.values())
```

A partir daí, é necessário definirmos as expressões regulares de cada token, por exemplo:
```python
#Expressão regular para o operador '+'
def t_MAIS(t):
  r'\+'
  return t

# Expressão Regular para a palavra reservada 'senão'
def t_SENAO(t):
  r'senão'
  t.type = reservadas.get(t.value,'SENAO')
  return t
```

Para construir o lexer, usamos a função `lex()` da biblioteca ply, assim:
```python
lexer = lex.lex()
```

Logo após, podemos passar o código a ser feito a varredura (recebido por parâmetro) usando a função `input()`.
```
lexer.input(dados)
```

Em seguida, os tokens já podem ser gerados com a função `token()`, para assim serem impressos na tela.

```python
tok = lexer.token()
```

## Exemplo de uso

Como exemplo, usaremos o arquivo de teste `fat.tpp`, veja seu código abaixo:

```python
inteiro: n
flutuante: a[10]

inteiro fatorial(inteiro: n)
    inteiro: fat
    se n > 0 então {não calcula se n > 0}
        fat := 1
        repita
            fat := fat * n
            n := n - 1
        até n = 0
        retorna(fat) {retorna o valor do fatorial de n}
    senão
        retorna(0)
    fim
fim

inteiro principal()
    leia(n)
    escreva(fatorial(n))
    retorna(0)
fim
```

Para executar o programa, é necessário passar como parâmetro o arquivo `.tpp` a ser feito a varredura.

```shell
python3 lexico.py lexica-testes/fat.tpp
```

O resultado sairá como:

```
inteiro : ID
: : DOIS_PONTOS
n : ID
flutuante : ID
: : DOIS_PONTOS
a : ID
[ : ABRE_COLCHETE
10 : NUM_INTEIRO
] : FECHA_COLCHETE
inteiro : ID
fatorial : ID
( : ABRE_PARENTESE
inteiro : ID
: : DOIS_PONTOS
n : ID
) : FECHA_PARENTESE
inteiro : ID
: : DOIS_PONTOS
fat : ID
se : ID
n : ID
> : MAIOR
0 : NUM_INTEIRO
então : ENTAO
fat : ID
:= : ATRIBUICAO
1 : NUM_INTEIRO
repita : ID
fat : ID
:= : ATRIBUICAO
fat : ID
* : MULTIPLICACAO
n : ID
n : ID
:= : ATRIBUICAO
n : ID
- : MENOS
1 : NUM_INTEIRO
até : ATE
n : ID
= : IGUAL
0 : NUM_INTEIRO
retorna : ID
( : ABRE_PARENTESE
fat : ID
) : FECHA_PARENTESE
senão : SENAO
retorna : ID
( : ABRE_PARENTESE
0 : NUM_INTEIRO
) : FECHA_PARENTESE
fim : ID
fim : ID
inteiro : ID
principal : ID
( : ABRE_PARENTESE
) : FECHA_PARENTESE
leia : ID
( : ABRE_PARENTESE
n : ID
) : FECHA_PARENTESE
escreva : ID
( : ABRE_PARENTESE
fatorial : ID
( : ABRE_PARENTESE
n : ID
) : FECHA_PARENTESE
) : FECHA_PARENTESE
retorna : ID
( : ABRE_PARENTESE
0 : NUM_INTEIRO
) : FECHA_PARENTESE
fim : ID
```

Mais outro exemplo de varredura, com o arquivo `bubble_sort.tpp`.

Entrada:

```python
inteiro: vet[10]
inteiro: tam

tam := 10

{ preenche o vetor no pior caso }
preencheVetor()
  inteiro: i
  inteiro: j
  i := 0
  j := tam
  repita
    vet[i] = j
    i := i + 1
    j := j - 1
  até i < tam
fim

{ implementação do bubble sort }
bubble_sort()
  inteiro: i
  i := 0
  repita
    inteiro: j
    j := 0
    repita
      se vet[i] > v[j] então
        inteiro: temp
        temp := vet[i]
        vet[i] := vet[j]
        vet[j] := temp
      fim
      j := j + 1
    até j < i
    i := i + 1
  até i < tam
fim

{ programa principal }
inteiro principal()
  preencheVetor()
  bubble_sort()
  retorna(0)
fim
```

Saída:

```
inteiro : ID
: : DOIS_PONTOS
vet : ID
[ : ABRE_COLCHETE
10 : NUM_INTEIRO
] : FECHA_COLCHETE
inteiro : ID
: : DOIS_PONTOS
tam : ID
tam : ID
:= : ATRIBUICAO
10 : NUM_INTEIRO
preencheVetor : ID
( : ABRE_PARENTESE
) : FECHA_PARENTESE
inteiro : ID
: : DOIS_PONTOS
i : ID
inteiro : ID
: : DOIS_PONTOS
j : ID
i : ID
:= : ATRIBUICAO
0 : NUM_INTEIRO
j : ID
:= : ATRIBUICAO
tam : ID
repita : ID
vet : ID
[ : ABRE_COLCHETE
i : ID
] : FECHA_COLCHETE
= : IGUAL
j : ID
i : ID
:= : ATRIBUICAO
i : ID
+ : MAIS
1 : NUM_INTEIRO
j : ID
:= : ATRIBUICAO
j : ID
- : MENOS
1 : NUM_INTEIRO
até : ATE
i : ID
< : MENOR
tam : ID
fim : ID
bubble_sort : ID
( : ABRE_PARENTESE
) : FECHA_PARENTESE
inteiro : ID
: : DOIS_PONTOS
i : ID
i : ID
:= : ATRIBUICAO
0 : NUM_INTEIRO
repita : ID
inteiro : ID
: : DOIS_PONTOS
j : ID
j : ID
:= : ATRIBUICAO
0 : NUM_INTEIRO
repita : ID
se : ID
vet : ID
[ : ABRE_COLCHETE
i : ID
] : FECHA_COLCHETE
> : MAIOR
v : ID
[ : ABRE_COLCHETE
j : ID
] : FECHA_COLCHETE
então : ENTAO
inteiro : ID
: : DOIS_PONTOS
temp : ID
temp : ID
:= : ATRIBUICAO
vet : ID
[ : ABRE_COLCHETE
i : ID
] : FECHA_COLCHETE
vet : ID
[ : ABRE_COLCHETE
i : ID
] : FECHA_COLCHETE
:= : ATRIBUICAO
vet : ID
[ : ABRE_COLCHETE
j : ID
] : FECHA_COLCHETE
vet : ID
[ : ABRE_COLCHETE
j : ID
] : FECHA_COLCHETE
:= : ATRIBUICAO
temp : ID
fim : ID
j : ID
:= : ATRIBUICAO
j : ID
+ : MAIS
1 : NUM_INTEIRO
até : ATE
j : ID
< : MENOR
i : ID
i : ID
:= : ATRIBUICAO
i : ID
+ : MAIS
1 : NUM_INTEIRO
até : ATE
i : ID
< : MENOR
tam : ID
fim : ID
inteiro : ID
principal : ID
( : ABRE_PARENTESE
) : FECHA_PARENTESE
preencheVetor : ID
( : ABRE_PARENTESE
) : FECHA_PARENTESE
bubble_sort : ID
( : ABRE_PARENTESE
) : FECHA_PARENTESE
retorna : ID
( : ABRE_PARENTESE
0 : NUM_INTEIRO
) : FECHA_PARENTESE
fim : ID
```
