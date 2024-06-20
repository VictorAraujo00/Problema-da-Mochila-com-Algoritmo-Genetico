from random import getrandbits, randint, random, choice

#Gerar indiviudo aleatoriamente(Cromossomo)
def individuo(num_itens):
    return [getrandbits(1) for x in range(num_itens)]

#Criar população
def populacao(num_individuos, num_itens):
    return[individuo(num_itens) for x in range(num_individuos)]


#Calcular o fitness do indiviuo(cromossomo) = calcular o valor total daquele cromossomo
def fitness(individuo, peso_maximo, pesos_valores):
    peso_total = 0
    valor_total = 0

    for indice, valor in enumerate(individuo):
        peso_total += (individuo[indice] * pesos_valores[indice][0])
        valor_total += (individuo[indice] * pesos_valores[indice][1])

    
    
    if (peso_maximo - peso_total) < 0:
        return -1

    return valor_total

#Calcula a média fitness da população
def media_fitness(populacao, peso_maximo, pesos_valores):
    soma_fitness = sum(fitness(x, peso_maximo, pesos_valores) for x in populacao if fitness(x, peso_maximo, pesos_valores) >= 0)
    return soma_fitness/(len(populacao) * 1.0)

#Seleção dos individuos para reprodução a partir de uma roleta
def selecao_roleta(pais):
    def sortear(fitness_total, indice_ignorar = -1):
        roleta = []
        acumulado = 0
        valor_sorteado = random()

        if indice_ignorar!= -1:
            fitness_total -= valores[0][indice_ignorar]
        
        for indice, i in enumerate(valores[0]):

            if indice_ignorar==indice:
                continue
            acumulado += i
            roleta.append(acumulado/fitness_total)

            if roleta[-1] >= valor_sorteado:
                return indice
    
    valores = list(zip(*pais))
    fitness_total = sum(valores[0])

    indice_pai = sortear(fitness_total)
    indice_mae = sortear(fitness_total, indice_pai)

    pai = valores[1][indice_pai]
    mae = valores[1][indice_mae]

    return pai, mae



#Evoluir os indiviuos da população
def evoluir(populacao, peso_maximo, pesos_valores, num_cromossomos, mutacao=0.05):
    #Pega os cromossomos pais a partir do fitness
    pais = [[fitness(x, peso_maximo, pesos_valores), x] for x in populacao if fitness(x, peso_maximo, pesos_valores) >= 0] 
    pais.sort(reverse=True)

    #Reproducao entre dois indiviuos escolhidos pela roleta
    filhos = []
    
    #Reprodução
    while len(filhos) < num_cromossomos:
        pai, mae = selecao_roleta(pais)
        meio = len(pai)//2
        filho = pai[:meio] + mae[meio:]
        filhos.append(filho)

    #Mutacao de um indiviuo
    for individuo in filhos:
        if mutacao > random():
            pos_mutacao = randint(0, len(individuo)-1)
            if individuo[pos_mutacao] == 1:
                individuo[pos_mutacao] = 0
            else:
                individuo[pos_mutacao] = 1
    
    return filhos