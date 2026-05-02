# EX 1
import random

def rolar_dados(quantidade):
    dados = []

    for _ in range(quantidade):
        dados.append(random.randint(1, 6))

    return dados

# EX 2

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]

    dados_no_estoque.append(dado)
    dados_rolados.pop(dado_para_guardar)

    return [dados_rolados, dados_no_estoque]

#EX 3

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque[dado_para_remover]

    dados_rolados.append(dado)
    dados_no_estoque.pop(dado_para_remover)

    return [dados_rolados, dados_no_estoque]

#EX 4

def calcula_pontos_regra_simples(dados):
    pontos = {}

    for lado in range(1, 7):
        pontos[lado] = dados.count(lado) * lado

    return pontos

#EX 5

def calcula_pontos_soma(dados):
    total = 0

    for dado in dados:
        total = total + dado

    return total

#EX 6

def calcula_pontos_sequencia_baixa(dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados:
        return 15
    elif 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 15
    elif 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 15
    else:
        return 0
    
#EX 7 

def calcula_pontos_sequencia_alta(dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 30

    if 2 in dados and 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 30

    return 0

#EX 8

def calcula_pontos_full_house(lista):
    dicio={}
    x=0
    soma=0
    t2=False
    t3=False
    for i in lista:
        if i not in dicio:
            dicio[i]=1
            x+=1
        else:
            dicio[i]+=1
        soma+=i
    if x!=2:
        return 0
    else:
        for cont in lista:
            if dicio[cont]==2:
                t2=True
            elif dicio[cont]==3:
                t3=True
        if t3 and t2:
            return soma
        else:
            return 0
        
#EX 9

def calcula_pontos_quadra(lista):
    dicio = {}
    soma = 0
    for i in lista:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
        soma += i
    for num, quant in dicio.items():
        if quant >= 4:
            return soma
    
    return 0

#EX 10

def calcula_pontos_quina(dados):
    dicio = {}
    for i in dados:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
    for num, quant in dicio.items():
        if quant >= 5:
            return 50
    
    return 0

#EX 11

def calcula_pontos_regra_avancada(lista):
    dicionario={}
    dicionario['cinco_iguais'] = calcula_pontos_quina(lista)
    dicionario['full_house'] = calcula_pontos_full_house(lista)
    dicionario['quadra'] = calcula_pontos_quadra(lista)
    dicionario['sem_combinacao'] = calcula_pontos_soma(lista)
    dicionario['sequencia_alta'] = calcula_pontos_sequencia_alta(lista)
    dicionario['sequencia_baixa'] = calcula_pontos_sequencia_baixa(lista)
    return dicionario

        