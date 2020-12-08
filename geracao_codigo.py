# Iportando llvm
from llvmlite import ir
from llvmlite import binding as llvm

# Importando itertools para criar iteradores
import itertools

llvm.initialize()
llvm.initialize_all_targets()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

modulo = ir.Module('module.bc')
modulo.triple = llvm.get_default_triple()

target = llvm.Target.from_triple(modulo.triple)
target_machine = target.create_target_machine()

modulo.data_layout = target_machine.target_data

escrevaInteiro = ir.Function(modulo,ir.FunctionType(ir.VoidType(), [ir.IntType(32)]),name="escrevaInteiro")
escrevaFlutuante = ir.Function(modulo,ir.FunctionType(ir.VoidType(),[ir.FloatType()]),name="escrevaFlutuante")
leiaInteiro = ir.Function(modulo,ir.FunctionType(ir.IntType(32),[]),name="leiaInteiro")
leiaFlutuante = ir.Function(modulo,ir.FunctionType(ir.FloatType(),[]),name="leiaFlutuante")

# Dicionario de variaveis globais
info = {
    "variaveis_globais": []
}

# Vetor de variaveis locais
variaveis_locais = []

# Vetor de variaveis auxuliares
aux = []

# Vetor de funcoes
funcoes = []

# Econtra uma variavel e retorna se ela é uma variável ou argumento
def encontra_variavel(nome, variaveis_locais, funcao):
    for var in info["variaveis_globais"] + variaveis_locais:
        if(var.name == nome):
            return var, "var"
    
    for arg in funcao["function"].args:
        if(arg.name == nome):
            return arg, "arg"


# Função de quesolve uma expressão
def resolve_expressao(n, variaveis_locais, funcao):
    param_1 = 0
    param_2 = 0

    if(n.children[0].name == "numero"):
        param_1 = ir.Constant(ir.IntType(32), int(n.children[0].children[0].name))
    elif(n.children[0].name == "var"):
        ret, oque = encontra_variavel(n.children[0].children[0].name, variaveis_locais, funcao)

        if(oque == "var"):
            param_1 = funcao["builder"].load(ret)
        
        else:
            param_1 = ret
    
    if(n.children[1].name == "numero"):
        param_2 = ir.Constant(ir.IntType(32), int(n.children[1].children[0].name))
    elif(n.children[1].name == "var"):
        ret, oque = encontra_variavel(n.children[1].children[0].name, variaveis_locais, funcao)
        
        if(oque == "var"):
            param_2 = funcao["builder"].load(ret)
        
        else:
            param_2 = ret
        
    if(n.name == "+"): return funcao["builder"].add(param_1, param_2, name='summ')
    elif(n.name == "-"): return funcao["builder"].sub(param_1, param_2, name='sub')
    elif(n.name == "*"): return funcao["builder"].mul(param_1, param_2, name='mult')
    elif(n.name == "/"): return funcao["builder"].sdiv(param_1, param_2, name='div')


# Função de quesolve uma chamada de função
def resolve_chamada_funcao(n, builder, variaveis_locais, funcao):
    global funcoes
    params = []

    for f in funcoes:
        if(f["function"].name == n.children[0].name):
            if(len(n.children[2].children) > 0):
                for arg in n.children[2].children:
                    if(arg.name == "var"):
                        ret, oque = encontra_variavel(arg.children[0].name, variaveis_locais, f)
                        params.append(
                            funcao["builder"].load(ret)
                        )
                    elif(arg.name == "numero"):
                        params.append(
                            ir.Constant(ir.IntType(32), int(arg.children[0].name))
                        )
                return builder.call(f["function"], params)

            else:
                return builder.call(f["function"], [])

# Função que preenche o corpo da função
def preenche_funcao(corpo, funcao):
    global variaveis_locais
    global aux

    for no in corpo.children:
        if(no not in aux):
            aux.append(no)
            if(no.name == "declaracao_variaveis"):
                if(no.children[0].children[0].children[0].name == "inteiro"):
                    var = funcao["builder"].alloca(ir.IntType(32), name=no.children[0].children[1].children[0].name)

                elif(no.children[0].children[0].children[0].name == "flutuante"):
                    var = funcao["builder"].alloca(ir.FloatType(), name=no.children[0].children[1].children[0].name)

                var.align = 4
                variaveis_locais.append(var)
            
            elif(no.name == "atribuicao"):
                # Atribuição de um único número ou uma única variável.

                if(no.children[0].children[1].name == "numero" or no.children[0].children[1].name == "var"):
                    var = 0
                    
                    for local in variaveis_locais + info["variaveis_globais"]:
                        if(local.name == no.children[0].children[0].children[0].name):
                            var = local

                    if(no.children[0].children[1].name == "var"):
                        aux = variaveis_locais + info["variaveis_globais"]

                        for a in aux:
                            if(no.children[0].children[1].children[0].name == a.name):
                                temp = funcao["builder"].load(a,"")
                                funcao["builder"].store(temp, var)
                    
                    else:
                        if(str(var.type) == "i32*"):
                            funcao["builder"].store(ir.Constant(ir.IntType(32),  int(no.children[0].children[1].children[0].name)) , var)
                        
                        elif(str(var.type) == "float*"):
                            funcao["builder"].store(ir.Constant(ir.FloatType(),  float(no.children[0].children[1].children[0].name)) , var)

                elif(no.children[0].children[1].name in ["+", "-", "*", "/"]):
                    op = resolve_expressao(no.children[0].children[1] ,variaveis_locais, funcao)
                    ret, oque = encontra_variavel(no.children[0].children[0].children[0].name,variaveis_locais, funcao)
                    funcao["builder"].store(op, ret)

                elif(no.children[0].children[1].name == "chamada_funcao"):
                    f = resolve_chamada_funcao(no.children[0].children[1], funcao["builder"], variaveis_locais, funcao)
                    ret, oque = encontra_variavel(no.children[0].children[0].children[0].name ,variaveis_locais, funcao)
                    funcao["builder"].store(f, ret)

            elif(no.name == "repita" and len(no.children) > 0):
                repita = funcao["builder"].append_basic_block('repita')
                ate = funcao["builder"].append_basic_block('ate')
                repita_fim = funcao["builder"].append_basic_block('repita_fim')

                funcao["builder"].branch(repita)
                funcao["builder"].position_at_end(repita)
                preenche_funcao(no.children[1], funcao)
                funcao["builder"].branch(ate)

                funcao["builder"].position_at_end(ate)

                if (no.children[3].name == "var"):
                    for var in variaveis_locais + info["variaveis_globais"]:
                        if (var.name == no.children[3].children[0].name):
                            a_cmp = funcao["builder"].load(var, 'a_cmp', align=4)
                
                elif (no.children[3].name == "numero"):
                    a_cmp = ir.Constant(ir.IntType(32), int(no.children[3].children[0].name))
                
                if (no.children[5].name == "var"):
                    for var in variaveis_locais + info["variaveis_globais"]:
                        if (var.name == no.children[5].children[0].name):
                            b_cmp = funcao["builder"].load(var, 'a_cmp', align=4)
                
                elif (no.children[5].name == "numero"):
                    b_cmp = ir.Constant(ir.IntType(32), int(no.children[5].children[0].name))

                comp = funcao["builder"].icmp_signed("==", a_cmp, b_cmp, name='comp')
                funcao["builder"].cbranch(comp, repita_fim, repita)

                funcao["builder"].position_at_end(repita_fim)

            elif(no.name == "condicional"):
                tem_else = False

                for n in no.children:
                    if (n.name == "senão"):
                        tem_else = True

                iftrue_1 = funcao["builder"].append_basic_block('iftrue_1')
                iffalse_1 = funcao["builder"].append_basic_block('iffalse_1')
                ifend_1 = funcao["builder"].append_basic_block('ifend_1')

                if (no.children[1].name == "var"):
                    for var in variaveis_locais + info["variaveis_globais"]:
                        if (var.name == no.children[1].children[0].name):
                            a_cmp = funcao["builder"].load(var, 'a_cmp', align=4)
                
                elif (no.children[1].name == "numero"):
                    a_cmp = ir.Constant(ir.IntType(32), int(no.children[1].children[0].name))
                
                if (no.children[3].name == "var"):
                    for var in variaveis_locais + info["variaveis_globais"]:
                        if (var.name == no.children[3].children[0].name):
                            b_cmp = funcao["builder"].load(var, 'a_cmp', align=4)
                
                elif (no.children[3].name == "numero"):
                    b_cmp = ir.Constant(ir.IntType(32), int(no.children[3].children[0].name))
                
                If_1 = funcao["builder"].icmp_signed(no.children[2].name, a_cmp, b_cmp, name='if_test_1')
                funcao["builder"].cbranch(If_1, iftrue_1, iffalse_1)

                then_body = no.children[5]

                funcao["builder"].position_at_end(iftrue_1)
                preenche_funcao(then_body, funcao)
                funcao["builder"].branch(ifend_1)

                if(tem_else):
                    else_body = no.children[7]
                    funcao["builder"].position_at_end(iffalse_1)
                    preenche_funcao(else_body, funcao)
                    funcao["builder"].branch(ifend_1)
                else:
                    funcao["builder"].position_at_end(iffalse_1)
                    funcao["builder"].branch(ifend_1)

                funcao["builder"].position_at_end(ifend_1)

            elif(no.name == "leia" and len(no.children) > 0):
                if(no.children[2].name == "var"):
                    for v in variaveis_locais + info["variaveis_globais"]:
                        if (v.name == no.children[2].children[0].name):
                            if(str(v.type) == "i32*"):
                                ret = funcao["builder"].call(leiaInteiro, [])
                                funcao["builder"].store(ret, v)

                            elif(str(v.type) == "float*"):
                                ret = funcao["builder"].call(leiaFlutuante, [])
                                funcao["builder"].store(ret, v)
            
            elif(no.name == "escreva" and len(no.children) > 0):
                if(no.children[2].name == "var"):
                    for v in variaveis_locais + info["variaveis_globais"]:
                        if (v.name == no.children[2].children[0].name):
                            if(str(v.type) == "i32*"):
                                var = funcao["builder"].load(v, name='write_var', align=4)
                                funcao["builder"].call(escrevaInteiro, [var])
                            elif(str(v.type) == "float*"):
                                var = funcao["builder"].load(v, name='write_var', align=4)
                                funcao["builder"].call(escrevaFlutuante, [var])
                elif(no.children[2].name == "numero"):
                    if(no.children[2].children[0].name.isdigit()):
                        var = ir.Constant(ir.IntType(32), int(no.children[2].children[0].name))
                        
                        funcao["builder"].call(escrevaInteiro, [var])

                    elif(not no.children[2].children[0].name.isdigit()):
                        var = ir.Constant(ir.FloatType(), float(no.children[2].children[0].name))
                        funcao["builder"].call(escrevaFlutuante, [var]) 

            elif(no.name == "retorna" and len(no.children) > 0):
                r = 0
                if(no.children[2].name == "numero"):
                    r = ir.Constant(ir.IntType(32), int(no.children[2].children[0].name))
                
                elif(no.children[2].name == "var"):
                    for var in variaveis_locais+info["variaveis_globais"]:
                        if(var.name == no.children[2].children[0].name):
                            r = funcao["builder"].load(var, name='ret_temp', align=4)
                
                elif(no.children[2].name in ["+", "-", "*", "/"]):
                    r = funcao["builder"].alloca(ir.IntType(32), name='ret_temp')
                    op = resolve_expressao(no.children[2], variaveis_locais, funcao)
                    funcao["builder"].store(op, r)

                funcao["builder"].ret(r)

        preenche_funcao(no, funcao)


# Função recursiva que passa pelos nós da árvore
def passar_por_arvore(arvore, funcoes):
    global variaveis_locais
    for no in arvore.children:

        # Passa pelas funções
        for f in funcoes:
            if((f["function"].name == no.name or (f["function"].name == "main" and no.name == "principal")) and no.parent.name == "cabecalho"):
                variaveis_locais = []
                preenche_funcao(no.parent.children[-1], f)

        passar_por_arvore(no, funcoes)

# Função que gera o código intermediário
def gera_codigo(arvore, tabela_simbolos, sema_success):

    global modulo
    global info

    # Define as variáveis globais e funções
    for simbolo in tabela_simbolos:
        # Se o simbolo for uma variavel
        if (simbolo["simbolo_tipo"] == "variable" and simbolo["escopo"] == "global"):
            var_type = simbolo["tipo_valor"]

            # Verifica se o tipo é inteiro
            if(var_type == "inteiro"):
                if(len(simbolo["dimensoes"]) == 0):
                    g = ir.GlobalVariable(modulo, ir.IntType(32), simbolo["nome"])

                if(len(simbolo["dimensoes"]) == 1):
                    g_type = ir.ArrayType(ir.IntType(32), int(simbolo["dimensoes"][0]))
                    g = ir.GlobalVariable(modulo, g_type, simbolo["nome"])
                    info["variaveis_globais"].append(g)
            
            # Verifica se o tipo é flutuante
            elif(var_type == "flutuante"):

                if(len(simbolo["dimensoes"]) == 0):
                    g = ir.GlobalVariable(modulo, ir.FloatType(), simbolo["nome"])

                if(len(simbolo["dimensoes"]) == 1):
                    g_type = ir.ArrayType(ir.FloatType(), int(simbolo["dimensoes"][0]))
                    g = ir.GlobalVariable(modulo, g_type, simbolo["nome"])
            
            g.linkage = "common"
            g.align = 4
            info["variaveis_globais"].append(g)

        # Se o simbolo for uma funcao
        elif (simbolo["simbolo_tipo"] == "function"):
            if(simbolo["nome"] == "principal"):
                simbolo["nome"] = "main"
            
            # Lista de argumentos
            arguments_list = []

            if (len(simbolo["parametros"]) > 0):
                for a in simbolo["parametros"]:
                    if(a["par_type"] == "inteiro"):
                        arguments_list.append(ir.IntType(32))
                    else:
                        arguments_list.append(ir.FloatType())

            if(len(simbolo["return"]) > 0):
                if(simbolo["return"][0]["ret_type"] == "inteiro"):
                    f_ret = ir.IntType(32)
                else:
                    f_ret = ir.FloatType()
            
                f_func = ir.FunctionType(f_ret, arguments_list)
                f = ir.Function(modulo, f_func, name=simbolo["nome"])
                entryBlock = f.append_basic_block('entry')
                builder = ir.IRBuilder(entryBlock)
                
            else:
                f_func = ir.FunctionType(ir.VoidType(), arguments_list)
                f = ir.Function(modulo, f_func, name=simbolo["nome"])
                entryBlock = f.append_basic_block('entry')
                builder = ir.IRBuilder(entryBlock)
            
            for i in range(len(f.args)):
                f.args[i].name = simbolo["parametros"][i]["par_name"]


            funcoes.append({"function": f, "builder": builder, "arguments": f.args})

    # Chama a funcao recursiva que passa pela arvore
    passar_por_arvore(arvore, funcoes)

    file = open('modulo.ll', 'w')
    file.write(str(modulo))
    file.close()
    print(modulo)