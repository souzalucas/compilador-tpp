from anytree import Node

import anytree

# Constantes
OPERACOES = ['+', '-', '*', '/', ':=', ':']
NOS_SIMPLES_PODA = [
    'acao', 'expressao', 'expressao_logica', 'expressao_simples', 'expressao_aditiva', 
    'expressao_multiplicativa', 'expressao_unaria', 'operador_relacional', 
    'operador_logico', 'operador_negacao', 'fator', 'lista_variaveis'
    ]

# Variáveis globais
tabela_simbolos = []
attr_vars = []
variaveis = []
attr = []
arrays_erros = []
indice = False
escopo = "global"
no_encontrado = None
sucesso = True

erros = {
    "tem_principal": False,
    "principal_tem_retorno": False,
    "chamada_funcao_errada": []
}


# Funções de Poda
def poda_especial(arvore):
    aux = []

    if(arvore.parent.name in ["operador_soma", "operador_multiplicacao"]):
        poda_um_no(arvore.parent)

    pai = arvore.parent
    aux = [pai.children[0], pai.children[2]] 
    arvore.children = aux
    pai.children = [arvore]
    
def poda_um_no(arvore):
    aux = []
    pai = arvore.parent

    for i in range(len(pai.children)):
        if (pai.children[i].name == arvore.name):
            aux += arvore.children
        else:
            aux.append(pai.children[i])

    pai.children = aux

def poda(arvore):
    for no in arvore.children:
        poda(no)

    if(arvore.name in OPERACOES):
        poda_especial(arvore)

    if(arvore.name in NOS_SIMPLES_PODA):
        poda_um_no(arvore)
    
    if(arvore.name in ['corpo', 'lista_declaracoes', 'lista_parametros', 'lista_argumentos'] and arvore.parent.name == arvore.name):
        poda_um_no(arvore)

# Funções Auxiliares
def get_no(no, nome):
    global no_encontrado
    for n in no.children:
        if (n.name == nome):
            no_encontrado = n.children
        
        else:
            get_no(n, nome)
    
    return no_encontrado

def procura_escopo(no):
    global escopo
    if(no.parent.name != "programa"):
        if(no.parent.name == "cabecalho"):
            escopo = no.parent.children[0].name
        else:
            procura_escopo(no.parent)

def get_func(func):
    for simbolo in tabela_simbolos:
        if(simbolo["simbolo_tipo"] == "function" and simbolo["nome"] == func):
            return simbolo
    
    return None

def get_attr(no):
    global indice
    for n in no.children:
        if (n.name == "indice"):
            indice = True
        if (n.name == "var" and len(n.children) == 1):
            for s in tabela_simbolos:
                if (n.children[0].name == s["nome"] and s["simbolo_tipo"] == "variable"):
                    attr_vars.append(s["tipo_valor"])
        elif (n.name == "numero"):
            if (n.children[0].name.isdigit()):
                attr_vars.append("inteiro")
            else:
                attr_vars.append("flutuante")
        get_attr(n)

# Funcao pra gerar tabela de simbolos
def gera_tabela_simbolos(arvore):
    for no in arvore.children:
        simbolo = {
            "simbolo_tipo": None,
            "nome": None,
            "tipo_valor": None,
            "escopo": None,
            "parametros": [],
            "return": [],
            "dimensoes": [],
            "declarado": True,
            "inicializado": False,
            "usado": False
        }

        if(no.name == "declaracao_funcao"):
            simbolo["simbolo_tipo"] = "function"
            simbolo["tipo_valor"] = get_no(no, "tipo")[0].name
            simbolo["nome"] = get_no(no, "cabecalho")[0].name

            retorno = get_no(no, "retorna")[2]

            if(retorno.name == "numero"):
                ret_type = "inteiro"
                if(not retorno.children[0].name.isdigit()):
                    ret_type = "flutuante"

                simbolo["return"].append({
                    "is_variable": False,
                    "ret_type": ret_type,
                    "ret_value": retorno.children[0].name
                })

            elif(retorno.name == "var"):
                ret_type = "inteiro"
                
                for s in tabela_simbolos:
                    if(s["nome"] == retorno.children[0].name and s["simbolo_tipo"] == "variable"):
                        ret_type = s["tipo_valor"]

                simbolo["return"].append({
                    "is_variable": True,
                    "ret_type": ret_type,
                    "ret_value": retorno.children[0].name
                })

            for param in (get_no(no, "lista_parametros")):
                if(param.name == "parametro"):
                    simbolo["parametros"].append({
                        "par_type": get_no(param, "tipo")[0].name,
                        "par_name": get_no(param, ":")[1].name
                    })

                    tabela_simbolos.append({
                        "simbolo_tipo": "variable",
                        "nome": get_no(param, ":")[1].name,
                        "tipo_valor": get_no(param, "tipo")[0].name,
                        "escopo": no.children[0].children[0].name,
                        "parametros": [],
                        "declarado": True,
                        "inicializado": False,
                        "usado": False
                    })
            tabela_simbolos.append(simbolo)

        elif(no.name == "declaracao_variaveis"):
            simbolo["simbolo_tipo"] = "variable"
            simbolo["tipo_valor"] = get_no(no, "tipo")[0].name
            simbolo["nome"] = get_no(no, "var")[0].name

            if(no.parent.name == "corpo"):
                simbolo["escopo"] = no.parent.parent.children[0].name
            
            else:
                simbolo["escopo"] = "global"

            
            if(len(no.children[0].children[1].children) > 1):
                indice = no.children[0].children[1].children[1]

                if(len(indice.children) == 3):
                    simbolo["dimensoes"].append(indice.children[1].children[0].name)
                
                elif(len(indice.children) >  3):
                    simbolo["dimensoes"].append(indice.children[0].children[1].children[0].name)
                    simbolo["dimensoes"].append(indice.children[2].children[0].name)
            tabela_simbolos.append(simbolo)

        gera_tabela_simbolos(no)

# Funcoes de regras semanticas
def checa_chamada_recursiva(no):
    for n in no.children:
        if(n.name == "chamada_funcao" and n.children[0].name == "principal"):
            print("AVISO: Chamada recursiva para principal.")
        checa_chamada_recursiva(n)

def checa_funcao_principal(arvore):
    for no in arvore.children:
        if(no.name == "cabecalho" and no.children[0].name == "principal"):
            checa_chamada_recursiva(no)
            erros["tem_principal"] = True

            if(no.children[-1].children[-1].name == "retorna"):
                erros["principal_tem_retorno"] = True
             
        
        checa_funcao_principal(no)

def checa_chamada_funcao(arvore):
    global sucesso
    for no in arvore.children:
        if(no.name == "chamada_funcao"):
            func = get_func(no.children[0].name)

            if(func == None):
                sucesso = False
                print("ERRO: Chamada à função \'", func["nome"], "\' que não foi declarada.")

            else:
                func["usado"] = True

                if(no.children[0].name == "principal" and  no.parent.name == "corpo" and no.parent.parent.children[0].name != "principal"):
                    sucesso = False
                    print("ERRO: Chamada para a função principal não permitida.")

                else:
                    if(len(func["parametros"]) == 1):
                        if (len(func["parametros"]) != len(no.children[2].children)):
                            erros["chamada_funcao_errada"].append(func["nome"])
                    elif(len(func["parametros"]) > 1):
                        if (len(func["parametros"]) != len(no.children[2].children)-1):
                            erros["chamada_funcao_errada"].append(func["nome"])


        checa_chamada_funcao(no)

def checa_funcoes_nao_usadas():
    for simbolo in tabela_simbolos:
        if(simbolo["simbolo_tipo"] == "function" and not simbolo["usado"] and simbolo["nome"] != "principal"):
            print("AVISO: Função \'", simbolo["nome"], "\' declarada, mas não utilizada.")

def checa_var_erros():
    global sucesso
    for simbolo in tabela_simbolos:
        if(simbolo["simbolo_tipo"] == "variable"):
            declarado = simbolo["declarado"]
            inicializado = simbolo["inicializado"]
            usado = simbolo["usado"]

            if(declarado and not inicializado or not usado):
                print("AVISO: Variável \'", simbolo["nome"], "\' declarada e não utilizada")

def checa_inicializacao_variavel(arvore):
    global sucesso
    for no in arvore.children:
        if (no.name in [":=", "leia", "escreva", "repita", "se", "lista_argumentos"]):
            for n in no.children:
                if(n.name == "var"):
                    if (n.children[0].name not in variaveis):
                        variaveis.append(n.children[0].name)

            for simbolo in tabela_simbolos:
                if(simbolo["simbolo_tipo"] == "variable" and simbolo["nome"] in variaveis):
                    procura_escopo(no)
                    if(simbolo["escopo"] == "global" or simbolo["escopo"] == escopo):
                        simbolo["usado"] = True

                        if (no.name in [":=", "leia"]):
                            simbolo["inicializado"] = True

        checa_inicializacao_variavel(no)

def checa_atributo(arvore):
    global sucesso
    global attr_vars
    global indice
    tipo_valor = ""
    for no in arvore.children:
        if(no.name == ":="):
            indice = False
            attr_vars = []
            get_attr(no)

            if(not indice):
                for s in tabela_simbolos:
                    if(s["simbolo_tipo"] == "variable"):
                        if(s["nome"] == no.children[0].children[0].name):
                            tipo_valor = s["tipo_valor"]
                
                if(tipo_valor == "inteiro" and "flutuante" in attr_vars):
                    print("AVISO: Atribuição de tipos distintos \'", no.children[0].children[0].name, "\' inteiro e expressão flutuante.")
                
                elif(tipo_valor == "flutuante" and "inteiro" in attr_vars):
                    print("AVISO: Atribuição de tipos distintos \'", no.children[0].children[0].name, "\' flutuante e expressão inteiro.")
        
        checa_atributo(no)

def checa_array(no):
    global sucesso
    indice = None
    aux = 1
    err = False
    for n in no.children:
        if(n.name == ":" and len(n.children[1].children) > 1):
            indice = n.children[1].children[1]
        
        elif(n.name == ":=" and len(n.children[0].children) > 1):
            indice = n.children[0].children[1]
            aux = 0

        if(indice != None):
            if(n.children[aux].children[0].name not in arrays_erros):
                if(len(indice.children) == 3):
                    if(indice.children[1].name == "numero"):
                        if (not indice.children[1].children[0].name.isdigit()):
                            sucesso = False
                            print("ERRO: Índice de array \'", n.children[aux].children[0].name ,"\' não inteiro.")
                            err = True
                    else:
                        var = indice.children[1].children[0].name
                        for s in tabela_simbolos:
                            if(var == s["nome"] and s["simbolo_tipo"] == "variable" and s["tipo_valor"] == "flutuante"):
                                sucesso = False
                                print("ERRO: Índice de array \'", n.children[aux].children[0].name ,"\' não inteiro.")
                                err = True
                
                else:
                    if(indice.children[0].children[1].name == "numero"):
                        if (not indice.children[0].children[1].children[0].name.isdigit()):
                            sucesso = False
                            print("ERRO: Índice de array \'", n.children[aux].children[0].name ,"\' não inteiro.")
                            err = True
                    else:
                        var = indice.children[0].children[1].children[0].name
                        for s in tabela_simbolos:
                            if(var == s["nome"] and s["simbolo_tipo"] == "variable" and s["tipo_valor"] == "flutuante"):
                                sucesso = False
                                print("ERRO: Índice de array \'", n.children[aux].children[0].name ,"\' não inteiro.")
                                err = True

                    if(not err):
                        if(indice.children[2].name == "numero"):
                            if (not indice.children[2].children[0].name.isdigit()):
                                sucesso = False
                                print("ERRO: Índice de array \'", n.children[aux].children[0].name ,"\' não inteiro.")
                                err = True
                        else:
                            var = indice.children[2].children[0].name
                            for s in tabela_simbolos:
                                if(var == s["nome"] and s["simbolo_tipo"] == "variable" and s["tipo_valor"] == "flutuante"):
                                    sucesso = False
                                    print("ERRO: Índice de array \'", n.children[aux].children[0].name ,"\' não inteiro.")
                                    err = True

            if (err):
                arrays_erros.append(n.children[aux].children[0].name)

        checa_array(n)

def checa_indice(no):
    global sucesso
    indices = []
    for n in no.children:
        if(n.name == ":="):
            if(len(n.children[0].children) > 1):
                indice = n.children[0].children[1]

                if(len(indice.children) == 3):
                    if(indice.children[1].name == "numero"):
                        numero = indice.children[1].children[0].name

                        for s in tabela_simbolos:
                            if(n.children[0].children[0].name == s["nome"] and s["simbolo_tipo"] == "variable"):
                                if(numero >= s["dimensoes"]):
                                    sucesso = False
                                    print("ERRO: índice de array ", s["nome"] ," fora do intervalo (out of range)")
                
                else:
                    if(indice.children[0].children[1].name == "numero"):
                        indices.append(indice.children[0].children[1].children[0].name)
                    
                    if(indice.children[2].name == "numero"):
                        indices.append(indice.children[2].children[0].name)

                    for s in tabela_simbolos:
                            if(n.children[0].children[0].name == s["nome"] and s["simbolo_tipo"] == "variable"):
                                if(len(s["dimensoes"]) > 0):
                                    for i in range(len(s["dimensoes"])):

                                        if(int(indices[i]) >= int(s["dimensoes"][i])):
                                            sucesso = False
                                            print("ERRO: índice de array ", s["nome"] ," fora do intervalo (out of range)")
                                            break




        checa_indice(n)

# Funcao Principal
def semantica(arvore):
    global sucesso

    # poda arvore e gera tabela de simbolos
    poda(arvore)
    gera_tabela_simbolos(arvore)

    # Verificações de função principal
    checa_funcao_principal(arvore)

    if(not erros["tem_principal"]):
        sucesso = False
        print("ERRO: Função principal não declarada.")
    
    elif(not erros["principal_tem_retorno"]):
        sucesso = False
        print("ERRO: Função principal deveria retornar inteiro, mas retorna vazio.")
    

    # Verificações de chamadas de função
    checa_chamada_funcao(arvore)
    checa_funcoes_nao_usadas()

    if(len(erros["chamada_funcao_errada"]) > 0):
        for err in erros["chamada_funcao_errada"]:
            sucesso = False
            print("ERRO: Chamada à função \'", err , "\' com número de parâmetros diferente que o declarado.")

    checa_inicializacao_variavel(arvore)

    for simbolo in tabela_simbolos:
        if (simbolo["nome"] in variaveis):
            variaveis.remove(simbolo["nome"])

        if(simbolo["simbolo_tipo"] == "variable"):
            if (not simbolo["inicializado"] and not simbolo["usado"]):
                print("AVISO: Variável \'", simbolo["nome"] , "\' declarada e não utilizada.")
            
            elif(not simbolo["inicializado"] and simbolo["usado"]):
                print("AVISO: Variável \'", simbolo["nome"] , "\' declarada e não inicializada.")
    
    if(len(variaveis) > 0):
        for var in variaveis:
            sucesso = False
            print("ERRO: Variável \'", var ,"\'  não declarada.")

    cont = 0

    for s in tabela_simbolos:
        for t in tabela_simbolos:
            if (s["nome"] == t["nome"] and s["escopo"] == t["escopo"]):
                cont += 1
        
        if(cont > 1):
            print("AVISO: Variável \'", t["nome"] ,"\' já declarada anteriormente")

        cont = 0
    
    checa_atributo(arvore)
    checa_array(arvore)
    checa_indice(arvore)

    return arvore, tabela_simbolos, sucesso