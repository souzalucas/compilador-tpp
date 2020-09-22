# Análise Léxica (Trabalho - 1ª parte)

Implementação da fase de análise léxica do compilador para a linguagem de programação T++, utilizando a ferramenta PLY, do Python 3.

## Linguagem de programação T++

### Sintaxe da linguagem usando a gramática BNF

|||
|-:|-|
|programa ::=|lista_declaracoes|
|lista_declaracoes ::= |lista_declaracoes declaracao \| declaracao
|declaracao ::= |declaracao_variaveis \| inicializacao_variaveis \| declaracao_funcao|
|declaracao_variaveis ::= |tipo DOIS_PONTOS lista_variaveis|
|inicializacao_variaveis ::= |atribuicao|
|lista_variaveis ::= |lista_variaveis VIRGULA var \| var|
|var ::= |ID \| ID indice|
|indice ::=| indice ABRE_COLCHETE expressao FECHA_COLCHETE \| ABRE_COLCHETE expressao FECHA_COLCHETE|
|tipo ::= |INTEIRO \| FLUTUANTE|
|declaracao_funcao ::= |tipo cabecalho \| cabecalho|
|cabecalho ::= |ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM|
|lista_parametros ::= |lista_parametros VIRGULA parametro \| parametro \| vazio|
|parametro ::= |tipo DOIS_PONTOS ID \| parametro ABRE_COLCHETE FECHA_COLCHETE|
|corpo ::= |corpo acao \| vazio|
|acao ::= |expressao \| declaracao_variaveis \| se \| repita \| leia \| escreva \| retorna \| erro|
|se ::= |SE \| expressao ENTAO corpo FIM \| SE expressao ENTAO corpo SENAO corpo FIM|
|repita ::= |REPITA corpo ATE expressao|
|atribuicao ::= |var ATRIBUICAO expressao|
|leia ::= |LEIA ABRE_PARENTESE var FECHA_PARENTESE|
|escreva ::= |ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE|
|retorna ::= |RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE|
|expressao ::= |expressao_logica \| atribuicao|
|expressao_logica ::= |expressao_simples \| expressao_logica operador_logico expressao_simples|
|expressao_simples ::= |expressao_aditiva \| expressao_simples operador_relacional expressao_aditiva|
|expressao_aditiva ::= |expressao_multiplicativa \| expressao_aditiva operador_soma expressao_multiplicativa|
|expressao_multiplicativa ::= |expressao_unaria \| expressao_multiplicativa operador_multiplicacao expressao_unaria|
|expressao_unaria ::= |fator \| operador_soma fator \| operador_negacao fator|
|operador_relacional ::= |MENOR \| MAIOR \| IGUAL \| DIFERENTE \| MENORIGUAL \| MAIORIGUAL|
|operador_soma ::= |MAIS \| MENOS|
|operador_logico ::= |ELOGICO \| OULOGICO|
|operador_negacao ::= |NEGACAO|
|operador_multiplicacao ::= |MULTIPLICACAO \| DIVISAO|
|fator ::= |ABRE_PARENTESE expressao FECHA_PARENTESE \| var \| chamada_funcao \| numero|
|numero ::= |NUM_INTEIRO \| NUM_PONTO_FLUTUANTE \| NUM_NOTACAO_CIENTIFICA|
|chamada_funcao ::= |ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE|
|lista_argumentos ::= |lista_argumentos VIRGULA expressao \| expressao \| vazio|


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
Abaixo temos as expressões regulares de cada token da linguagem.

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
|r'\\{[^\\}]+?\\}'|COMENTARIO|
|r'[a-zA-Z_]+[a-zA-Z_0-9]*'|ID|
|r'[-\+]?[0-9]+'|NUM_INTEIRO|
|r'[+-]?([0-9]+[.]([0-9]*)?\|[.][0-9]+)'|NUM_PONTO_FLUTUANTE|
|r'([+-]?([0-9]+[.]([0-9]*)?\|[.][0-9]+)\|([0-9]+))([eE][-+]?\d+)'|NUM_NOTACAO_CIENTIFICA|
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

## Implementação

### PLY (Python Lex-Yacc)
Para a varredura e busca dos tokens foi utilizada a biblioteca PLY do Python. PLY é uma implementação de ferramentas de análise lex e yacc para Python.

### Detalhes do código
Primeiramente, foi criado um dicionário contendo todas as palavras reservadas como chave, e seus respectivos tokens como valor.

```python
reservadas = {
'se' 		: 'SE',
'repita' 	: 'REPITA',
'fim' 		: 'FIM',
'leia' 		: 'LEIA',
'retorna' 	: 'RETORNA',
'escreva' 	: 'ESCREVA',
'inteiro' 	: 'INTEIRO',
'flutuante'	: 'FLUTUANTE',
'até' 		: 'ATE',
'senão' 	: 'SENAO',
'então' 	: 'ENTAO'
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
          'NUM_NOTACAO_CIENTIFICA', 'ID', 'COMENTARIO'] + list(reservadas.values())
```

A partir daí, é necessário definirmos as expressões regulares de cada token, por exemplo:
```python
#Expressão regular para o operador '+'
t_MAIS = r'\+'

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
python3 lexer.py lexica-testes/fat.tpp
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
{não calcula se n > 0} : COMENTARIO
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
{retorna o valor do fatorial de n} : COMENTARIO
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
{ preenche o vetor no pior caso } : COMENTARIO
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
{ implementação do bubble sort } : COMENTARIO
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
{ programa principal } : COMENTARIO
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
