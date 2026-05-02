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