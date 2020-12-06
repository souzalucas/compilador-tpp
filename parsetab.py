
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_COLCHETE ABRE_PARENTESE ATE ATRIBUICAO COMENTARIO DIFERENTE DIVISAO DOIS_PONTOS ENTAO ESCREVA E_LOGICO FECHA_COLCHETE FECHA_PARENTESE FIM FLUTUANTE ID IGUAL INTEIRO LEIA MAIOR MAIOR_IGUAL MAIS MENOR MENOR_IGUAL MENOS MULTIPLICACAO NEGACAO NUM_INTEIRO NUM_NOTACAO_CIENTIFICA NUM_PONTO_FLUTUANTE OU_LOGICO REPITA RETORNA SE SENAO VIRGULA\n    programa : lista_declaracoes\n  \n    lista_declaracoes : lista_declaracoes declaracao\n                        | declaracao\n  \n    declaracao : declaracao_variaveis\n                | inicializacao_variaveis\n                | declaracao_funcao\n  \n    declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n  \n    inicializacao_variaveis : atribuicao\n  \n    lista_variaveis : lista_variaveis VIRGULA var \n                    | var\n  \n    var : ID\n        | ID indice\n  \n    indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE\n            | ABRE_COLCHETE expressao FECHA_COLCHETE\n  \n    tipo : INTEIRO\n          | FLUTUANTE\n  \n    declaracao_funcao : tipo cabecalho \n                        | cabecalho\n  \n    cabecalho : ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM\n  \n    lista_parametros : lista_parametros VIRGULA parametro\n                      | parametro\n                      | vazio\n  \n    parametro : tipo DOIS_PONTOS ID\n              |  parametro ABRE_COLCHETE FECHA_COLCHETE\n  \n    corpo : corpo acao\n          | vazio\n  \n    acao : expressao\n          | declaracao_variaveis\n          | se\n          | repita\n          | leia\n          | escreva\n          | retorna\n  \n    se : SE expressao ENTAO corpo FIM\n        | SE expressao ENTAO corpo SENAO corpo FIM\n  \n    repita : REPITA corpo ATE expressao\n  \n    atribuicao : var ATRIBUICAO expressao\n  \n    leia : LEIA ABRE_PARENTESE var FECHA_PARENTESE\n  \n    escreva : ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE\n  \n    retorna : RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE\n  \n    expressao : expressao_logica\n              | atribuicao\n  \n    expressao_logica : expressao_simples\n                      | expressao_logica operador_logico expressao_simples\n  \n    expressao_simples : expressao_aditiva\n                      | expressao_simples operador_relacional expressao_aditiva\n  \n    expressao_aditiva : expressao_multiplicativa\n                      | expressao_aditiva operador_soma expressao_multiplicativa\n  \n    expressao_multiplicativa : expressao_unaria\n                              | expressao_multiplicativa operador_multiplicacao expressao_unaria\n  \n    expressao_unaria : fator\n                      | operador_soma fator\n                      | operador_negacao fator\n  \n    operador_relacional : MENOR\n                        | MAIOR\n                        | IGUAL\n                        | DIFERENTE\n                        | MENOR_IGUAL\n                        | MAIOR_IGUAL\n  \n    operador_soma : MAIS\n                  | MENOS\n  \n    operador_logico : E_LOGICO\n                    | OU_LOGICO\n  \n    operador_negacao : NEGACAO\n  \n    operador_multiplicacao : MULTIPLICACAO\n                            | DIVISAO\n  \n    fator : ABRE_PARENTESE expressao FECHA_PARENTESE\n          | var\n          | chamada_funcao\n          | numero\n  \n    numero : NUM_INTEIRO\n            | NUM_PONTO_FLUTUANTE\n            | NUM_NOTACAO_CIENTIFICA\n  \n    chamada_funcao : ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE\n  \n    lista_argumentos : lista_argumentos VIRGULA expressao\n                      | expressao\n                      | vazio\n  \n    vazio : \n  '
    
_lr_action_items = {'INTEIRO':([0,2,3,4,5,6,8,9,14,16,19,20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,72,73,77,78,79,80,81,85,86,87,88,92,93,95,96,97,98,99,100,101,102,103,106,112,116,121,122,123,124,125,126,127,128,129,],[10,10,-3,-4,-5,-6,-8,-18,-2,-17,10,-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-78,10,-14,-9,-44,-46,-48,-50,-67,10,-26,-13,-74,-19,-25,-27,-28,-29,-30,-31,-32,-33,-78,10,-78,10,-36,-38,-39,-40,-34,-78,10,-35,]),'FLUTUANTE':([0,2,3,4,5,6,8,9,14,16,19,20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,72,73,77,78,79,80,81,85,86,87,88,92,93,95,96,97,98,99,100,101,102,103,106,112,116,121,122,123,124,125,126,127,128,129,],[11,11,-3,-4,-5,-6,-8,-18,-2,-17,11,-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-78,11,-14,-9,-44,-46,-48,-50,-67,11,-26,-13,-74,-19,-25,-27,-28,-29,-30,-31,-32,-33,-78,11,-78,11,-36,-38,-39,-40,-34,-78,11,-35,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,14,15,16,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,75,77,78,79,80,81,85,86,87,88,92,93,94,95,96,97,98,99,100,101,102,103,105,106,112,113,114,115,116,117,121,122,123,124,125,126,127,128,129,],[13,13,-3,-4,-5,-6,17,-8,-18,-15,-16,-2,24,-17,31,-12,31,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,31,-49,-51,31,31,-69,-70,-60,-61,-64,-71,-72,-73,31,24,31,-62,-63,31,-54,-55,-56,-57,-58,-59,31,31,31,-65,-66,-52,-68,-53,-78,91,-14,-9,-44,-46,-48,-50,-67,31,-26,-13,-74,31,-19,-25,-27,-28,-29,-30,-31,-32,-33,31,-78,31,24,31,31,-78,31,31,-36,-38,-39,-40,-34,-78,31,-35,]),'$end':([1,2,3,4,5,6,8,9,14,16,20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,78,79,80,81,85,86,92,93,95,],[0,-1,-3,-4,-5,-6,-8,-18,-2,-17,-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,-9,-44,-46,-48,-50,-67,-13,-74,-19,]),'DOIS_PONTOS':([7,10,11,49,104,],[15,-15,-16,75,15,]),'ATRIBUICAO':([12,13,20,25,31,77,92,],[18,-11,-12,18,-11,-14,-13,]),'ABRE_PARENTESE':([13,17,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,94,96,97,98,99,100,101,102,103,105,106,107,108,109,112,114,115,116,117,121,122,123,124,125,126,127,128,129,],[19,19,37,-12,37,-7,-10,-11,-68,-37,-41,-42,-43,-45,64,-47,37,-49,-51,37,37,-69,-70,-60,-61,-64,-71,-72,-73,37,37,-62,-63,37,-54,-55,-56,-57,-58,-59,37,37,37,-65,-66,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,37,-26,-13,-74,37,-25,-27,-28,-29,-30,-31,-32,-33,37,-78,113,114,115,37,37,37,-78,37,37,-36,-38,-39,-40,-34,-78,37,-35,]),'ABRE_COLCHETE':([13,20,24,31,47,77,89,90,91,92,],[21,50,21,21,74,-14,74,-24,-23,-13,]),'MAIS':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,37,38,39,40,41,43,44,45,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,94,96,97,98,99,100,101,102,103,105,106,112,114,115,116,117,121,122,123,124,125,126,127,128,129,],[40,-12,40,-7,-10,-11,-68,-37,-41,-42,-43,40,-11,-47,-49,-51,40,-69,-70,-60,-61,-71,-72,-73,40,40,-62,-63,40,-54,-55,-56,-57,-58,-59,40,40,40,-65,-66,-52,-68,-53,-78,-14,-9,-44,40,-48,-50,-67,40,-26,-13,-74,40,-25,-27,-28,-29,-30,-31,-32,-33,40,-78,40,40,40,-78,40,40,-36,-38,-39,-40,-34,-78,40,-35,]),'MENOS':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,37,38,39,40,41,43,44,45,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,94,96,97,98,99,100,101,102,103,105,106,112,114,115,116,117,121,122,123,124,125,126,127,128,129,],[41,-12,41,-7,-10,-11,-68,-37,-41,-42,-43,41,-11,-47,-49,-51,41,-69,-70,-60,-61,-71,-72,-73,41,41,-62,-63,41,-54,-55,-56,-57,-58,-59,41,41,41,-65,-66,-52,-68,-53,-78,-14,-9,-44,41,-48,-50,-67,41,-26,-13,-74,41,-25,-27,-28,-29,-30,-31,-32,-33,41,-78,41,41,41,-78,41,41,-36,-38,-39,-40,-34,-78,41,-35,]),'NEGACAO':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,37,38,39,40,41,43,44,45,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,94,96,97,98,99,100,101,102,103,105,106,112,114,115,116,117,121,122,123,124,125,126,127,128,129,],[42,-12,42,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,42,-69,-70,-60,-61,-71,-72,-73,42,42,-62,-63,42,-54,-55,-56,-57,-58,-59,42,42,42,-65,-66,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,42,-26,-13,-74,42,-25,-27,-28,-29,-30,-31,-32,-33,42,-78,42,42,42,-78,42,42,-36,-38,-39,-40,-34,-78,42,-35,]),'NUM_INTEIRO':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,94,96,97,98,99,100,101,102,103,105,106,112,114,115,116,117,121,122,123,124,125,126,127,128,129,],[43,-12,43,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,43,-49,-51,43,43,-69,-70,-60,-61,-64,-71,-72,-73,43,43,-62,-63,43,-54,-55,-56,-57,-58,-59,43,43,43,-65,-66,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,43,-26,-13,-74,43,-25,-27,-28,-29,-30,-31,-32,-33,43,-78,43,43,43,-78,43,43,-36,-38,-39,-40,-34,-78,43,-35,]),'NUM_PONTO_FLUTUANTE':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,94,96,97,98,99,100,101,102,103,105,106,112,114,115,116,117,121,122,123,124,125,126,127,128,129,],[44,-12,44,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,44,-49,-51,44,44,-69,-70,-60,-61,-64,-71,-72,-73,44,44,-62,-63,44,-54,-55,-56,-57,-58,-59,44,44,44,-65,-66,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,44,-26,-13,-74,44,-25,-27,-28,-29,-30,-31,-32,-33,44,-78,44,44,44,-78,44,44,-36,-38,-39,-40,-34,-78,44,-35,]),'NUM_NOTACAO_CIENTIFICA':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,94,96,97,98,99,100,101,102,103,105,106,112,114,115,116,117,121,122,123,124,125,126,127,128,129,],[45,-12,45,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,45,-49,-51,45,45,-69,-70,-60,-61,-64,-71,-72,-73,45,45,-62,-63,45,-54,-55,-56,-57,-58,-59,45,45,45,-65,-66,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,45,-26,-13,-74,45,-25,-27,-28,-29,-30,-31,-32,-33,45,-78,45,45,45,-78,45,45,-36,-38,-39,-40,-34,-78,45,-35,]),'FECHA_PARENTESE':([19,20,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,46,47,48,64,68,69,70,71,77,79,80,81,82,83,84,85,86,89,90,91,92,93,110,118,119,120,],[-78,-12,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,72,-21,-22,-78,-52,-68,-53,86,-14,-44,-46,-48,93,-76,-77,-50,-67,-20,-24,-23,-13,-74,-75,123,124,125,]),'VIRGULA':([19,20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,46,47,48,64,68,69,70,77,78,79,80,81,82,83,84,85,86,89,90,91,92,93,110,],[-78,-12,52,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,73,-21,-22,-78,-52,-68,-53,-14,-9,-44,-46,-48,94,-76,-77,-50,-67,-20,-24,-23,-13,-74,-75,]),'FIM':([20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,96,97,98,99,100,101,102,103,116,121,122,123,124,125,126,127,128,129,],[-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,95,-26,-13,-74,-25,-27,-28,-29,-30,-31,-32,-33,-78,126,-36,-38,-39,-40,-34,-78,129,-35,]),'SE':([20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,96,97,98,99,100,101,102,103,106,112,116,121,122,123,124,125,126,127,128,129,],[-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,105,-26,-13,-74,-25,-27,-28,-29,-30,-31,-32,-33,-78,105,-78,105,-36,-38,-39,-40,-34,-78,105,-35,]),'REPITA':([20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,96,97,98,99,100,101,102,103,106,112,116,121,122,123,124,125,126,127,128,129,],[-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,106,-26,-13,-74,-25,-27,-28,-29,-30,-31,-32,-33,-78,106,-78,106,-36,-38,-39,-40,-34,-78,106,-35,]),'LEIA':([20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,96,97,98,99,100,101,102,103,106,112,116,121,122,123,124,125,126,127,128,129,],[-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,107,-26,-13,-74,-25,-27,-28,-29,-30,-31,-32,-33,-78,107,-78,107,-36,-38,-39,-40,-34,-78,107,-35,]),'ESCREVA':([20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,96,97,98,99,100,101,102,103,106,112,116,121,122,123,124,125,126,127,128,129,],[-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,108,-26,-13,-74,-25,-27,-28,-29,-30,-31,-32,-33,-78,108,-78,108,-36,-38,-39,-40,-34,-78,108,-35,]),'RETORNA':([20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,72,77,78,79,80,81,85,86,87,88,92,93,96,97,98,99,100,101,102,103,106,112,116,121,122,123,124,125,126,127,128,129,],[-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-78,-14,-9,-44,-46,-48,-50,-67,109,-26,-13,-74,-25,-27,-28,-29,-30,-31,-32,-33,-78,109,-78,109,-36,-38,-39,-40,-34,-78,109,-35,]),'ATE':([20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,78,79,80,81,85,86,88,92,93,96,97,98,99,100,101,102,103,106,112,122,123,124,125,126,129,],[-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,-9,-44,-46,-48,-50,-67,-26,-13,-74,-25,-27,-28,-29,-30,-31,-32,-33,-78,117,-36,-38,-39,-40,-34,-35,]),'SENAO':([20,22,23,24,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,78,79,80,81,85,86,88,92,93,96,97,98,99,100,101,102,103,116,121,122,123,124,125,126,129,],[-12,-7,-10,-11,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,-9,-44,-46,-48,-50,-67,-26,-13,-74,-25,-27,-28,-29,-30,-31,-32,-33,-78,127,-36,-38,-39,-40,-34,-35,]),'MULTIPLICACAO':([20,25,31,32,34,35,38,39,43,44,45,68,69,70,77,81,85,86,92,93,],[-12,-68,-11,66,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,66,-50,-67,-13,-74,]),'DIVISAO':([20,25,31,32,34,35,38,39,43,44,45,68,69,70,77,81,85,86,92,93,],[-12,-68,-11,67,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,67,-50,-67,-13,-74,]),'MENOR':([20,25,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,79,80,81,85,86,92,93,],[-12,-68,57,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,57,-46,-48,-50,-67,-13,-74,]),'MAIOR':([20,25,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,79,80,81,85,86,92,93,],[-12,-68,58,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,58,-46,-48,-50,-67,-13,-74,]),'IGUAL':([20,25,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,79,80,81,85,86,92,93,],[-12,-68,59,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,59,-46,-48,-50,-67,-13,-74,]),'DIFERENTE':([20,25,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,79,80,81,85,86,92,93,],[-12,-68,60,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,60,-46,-48,-50,-67,-13,-74,]),'MENOR_IGUAL':([20,25,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,79,80,81,85,86,92,93,],[-12,-68,61,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,61,-46,-48,-50,-67,-13,-74,]),'MAIOR_IGUAL':([20,25,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,79,80,81,85,86,92,93,],[-12,-68,62,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,62,-46,-48,-50,-67,-13,-74,]),'E_LOGICO':([20,25,27,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,79,80,81,85,86,92,93,],[-12,-68,54,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,-44,-46,-48,-50,-67,-13,-74,]),'OU_LOGICO':([20,25,27,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,79,80,81,85,86,92,93,],[-12,-68,55,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,-44,-46,-48,-50,-67,-13,-74,]),'FECHA_COLCHETE':([20,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,51,68,69,70,74,76,77,79,80,81,85,86,92,93,],[-12,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,77,-52,-68,-53,90,92,-14,-44,-46,-48,-50,-67,-13,-74,]),'ENTAO':([20,25,26,27,28,29,30,31,32,34,35,38,39,43,44,45,68,69,70,77,79,80,81,85,86,92,93,111,],[-12,-68,-37,-41,-42,-43,-45,-11,-47,-49,-51,-69,-70,-71,-72,-73,-52,-68,-53,-14,-44,-46,-48,-50,-67,-13,-74,116,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'lista_declaracoes':([0,],[2,]),'declaracao':([0,2,],[3,14,]),'declaracao_variaveis':([0,2,87,112,121,128,],[4,4,98,98,98,98,]),'inicializacao_variaveis':([0,2,],[5,5,]),'declaracao_funcao':([0,2,],[6,6,]),'tipo':([0,2,19,73,87,112,121,128,],[7,7,49,49,104,104,104,104,]),'atribuicao':([0,2,18,21,37,50,64,87,94,105,112,114,115,117,121,128,],[8,8,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'cabecalho':([0,2,7,],[9,9,16,]),'var':([0,2,15,18,21,33,36,37,50,52,53,56,63,64,65,87,94,105,112,113,114,115,117,121,128,],[12,12,23,25,25,69,69,25,25,78,69,69,69,25,69,25,25,25,25,118,25,25,25,25,25,]),'indice':([13,24,31,],[20,20,20,]),'lista_variaveis':([15,],[22,]),'expressao':([18,21,37,50,64,87,94,105,112,114,115,117,121,128,],[26,51,71,76,83,97,110,111,97,119,120,122,97,97,]),'expressao_logica':([18,21,37,50,64,87,94,105,112,114,115,117,121,128,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'expressao_simples':([18,21,37,50,53,64,87,94,105,112,114,115,117,121,128,],[29,29,29,29,79,29,29,29,29,29,29,29,29,29,29,]),'expressao_aditiva':([18,21,37,50,53,56,64,87,94,105,112,114,115,117,121,128,],[30,30,30,30,30,80,30,30,30,30,30,30,30,30,30,30,]),'expressao_multiplicativa':([18,21,37,50,53,56,63,64,87,94,105,112,114,115,117,121,128,],[32,32,32,32,32,32,81,32,32,32,32,32,32,32,32,32,32,]),'operador_soma':([18,21,30,37,50,53,56,63,64,65,80,87,94,105,112,114,115,117,121,128,],[33,33,63,33,33,33,33,33,33,33,63,33,33,33,33,33,33,33,33,33,]),'expressao_unaria':([18,21,37,50,53,56,63,64,65,87,94,105,112,114,115,117,121,128,],[34,34,34,34,34,34,34,34,85,34,34,34,34,34,34,34,34,34,]),'fator':([18,21,33,36,37,50,53,56,63,64,65,87,94,105,112,114,115,117,121,128,],[35,35,68,70,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'operador_negacao':([18,21,37,50,53,56,63,64,65,87,94,105,112,114,115,117,121,128,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'chamada_funcao':([18,21,33,36,37,50,53,56,63,64,65,87,94,105,112,114,115,117,121,128,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'numero':([18,21,33,36,37,50,53,56,63,64,65,87,94,105,112,114,115,117,121,128,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'lista_parametros':([19,],[46,]),'parametro':([19,73,],[47,89,]),'vazio':([19,64,72,106,116,127,],[48,84,88,88,88,88,]),'operador_logico':([27,],[53,]),'operador_relacional':([29,79,],[56,56,]),'operador_multiplicacao':([32,81,],[65,65,]),'lista_argumentos':([64,],[82,]),'corpo':([72,106,116,127,],[87,112,121,128,]),'acao':([87,112,121,128,],[96,96,96,96,]),'se':([87,112,121,128,],[99,99,99,99,]),'repita':([87,112,121,128,],[100,100,100,100,]),'leia':([87,112,121,128,],[101,101,101,101,]),'escreva':([87,112,121,128,],[102,102,102,102,]),'retorna':([87,112,121,128,],[103,103,103,103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','sintatico.py',19),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','sintatico.py',26),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','sintatico.py',27),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','sintatico.py',37),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','sintatico.py',38),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','sintatico.py',39),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','sintatico.py',46),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','sintatico.py',57),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_lista_variaveis','sintatico.py',64),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','sintatico.py',65),
  ('var -> ID','var',1,'p_var','sintatico.py',79),
  ('var -> ID indice','var',2,'p_var','sintatico.py',80),
  ('indice -> indice ABRE_COLCHETE expressao FECHA_COLCHETE','indice',4,'p_indice','sintatico.py',95),
  ('indice -> ABRE_COLCHETE expressao FECHA_COLCHETE','indice',3,'p_indice','sintatico.py',96),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','sintatico.py',115),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo','sintatico.py',116),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','sintatico.py',125),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','sintatico.py',126),
  ('cabecalho -> ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM','cabecalho',6,'p_cabecalho','sintatico.py',136),
  ('lista_parametros -> lista_parametros VIRGULA parametro','lista_parametros',3,'p_lista_parametros','sintatico.py',149),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','sintatico.py',150),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','sintatico.py',151),
  ('parametro -> tipo DOIS_PONTOS ID','parametro',3,'p_parametro','sintatico.py',168),
  ('parametro -> parametro ABRE_COLCHETE FECHA_COLCHETE','parametro',3,'p_parametro','sintatico.py',169),
  ('corpo -> corpo acao','corpo',2,'p_corpo','sintatico.py',180),
  ('corpo -> vazio','corpo',1,'p_corpo','sintatico.py',181),
  ('acao -> expressao','acao',1,'p_acao','sintatico.py',191),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','sintatico.py',192),
  ('acao -> se','acao',1,'p_acao','sintatico.py',193),
  ('acao -> repita','acao',1,'p_acao','sintatico.py',194),
  ('acao -> leia','acao',1,'p_acao','sintatico.py',195),
  ('acao -> escreva','acao',1,'p_acao','sintatico.py',196),
  ('acao -> retorna','acao',1,'p_acao','sintatico.py',197),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','sintatico.py',204),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','sintatico.py',205),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','sintatico.py',229),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','sintatico.py',241),
  ('leia -> LEIA ABRE_PARENTESE var FECHA_PARENTESE','leia',4,'p_leia','sintatico.py',252),
  ('escreva -> ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE','escreva',4,'p_escreva','sintatico.py',264),
  ('retorna -> RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE','retorna',4,'p_retorna','sintatico.py',276),
  ('expressao -> expressao_logica','expressao',1,'p_expressao','sintatico.py',288),
  ('expressao -> atribuicao','expressao',1,'p_expressao','sintatico.py',289),
  ('expressao_logica -> expressao_simples','expressao_logica',1,'p_expressao_logica','sintatico.py',296),
  ('expressao_logica -> expressao_logica operador_logico expressao_simples','expressao_logica',3,'p_expressao_logica','sintatico.py',297),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','sintatico.py',307),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','sintatico.py',308),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','sintatico.py',318),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','sintatico.py',319),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','sintatico.py',329),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','sintatico.py',330),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','sintatico.py',340),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','sintatico.py',341),
  ('expressao_unaria -> operador_negacao fator','expressao_unaria',2,'p_expressao_unaria','sintatico.py',342),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','sintatico.py',352),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','sintatico.py',353),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','sintatico.py',354),
  ('operador_relacional -> DIFERENTE','operador_relacional',1,'p_operador_relacional','sintatico.py',355),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operador_relacional','sintatico.py',356),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operador_relacional','sintatico.py',357),
  ('operador_soma -> MAIS','operador_soma',1,'p_operador_soma','sintatico.py',366),
  ('operador_soma -> MENOS','operador_soma',1,'p_operador_soma','sintatico.py',367),
  ('operador_logico -> E_LOGICO','operador_logico',1,'p_operador_logico','sintatico.py',376),
  ('operador_logico -> OU_LOGICO','operador_logico',1,'p_operador_logico','sintatico.py',377),
  ('operador_negacao -> NEGACAO','operador_negacao',1,'p_operador_negacao','sintatico.py',386),
  ('operador_multiplicacao -> MULTIPLICACAO','operador_multiplicacao',1,'p_operador_multiplicacao','sintatico.py',395),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','sintatico.py',396),
  ('fator -> ABRE_PARENTESE expressao FECHA_PARENTESE','fator',3,'p_fator','sintatico.py',405),
  ('fator -> var','fator',1,'p_fator','sintatico.py',406),
  ('fator -> chamada_funcao','fator',1,'p_fator','sintatico.py',407),
  ('fator -> numero','fator',1,'p_fator','sintatico.py',408),
  ('numero -> NUM_INTEIRO','numero',1,'p_numero','sintatico.py',422),
  ('numero -> NUM_PONTO_FLUTUANTE','numero',1,'p_numero','sintatico.py',423),
  ('numero -> NUM_NOTACAO_CIENTIFICA','numero',1,'p_numero','sintatico.py',424),
  ('chamada_funcao -> ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE','chamada_funcao',4,'p_chamada_funcao','sintatico.py',433),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','sintatico.py',446),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','sintatico.py',447),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','sintatico.py',448),
  ('vazio -> <empty>','vazio',0,'p_vazio','sintatico.py',465),
]