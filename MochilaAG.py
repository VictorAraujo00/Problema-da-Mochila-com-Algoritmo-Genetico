from Genetic import *

#Pesos e valores de cada item que pode ser colocado na mochila
pesos_valores = [[4, 30], [8, 10], [8, 30], [25, 75], [2, 10], [50, 100], [6, 300], [12, 50], [100, 400], [8, 300]]

#Peso maximo da mochila
peso_maximo = 100

#número de crmossomos(Número de soluções possiveis)
num_cromossomos = 120

#Quantas vezes o algoritmo vai evoluir os individuos da população
geracoes = 80

#Número de itens é igual ao tamanho vetor pesos_vales(itens)
num_itens = len(pesos_valores)

#Chamar o procedimento para gerar a população
populacao = populacao(num_cromossomos, num_itens)

#Armazena todo histórico de fitness para ser plotado o gráfico
historico_fitness = [media_fitness(populacao, peso_maximo, pesos_valores)]

for i in range(geracoes):
    #Evolui a população a cada geração
    populacao = evoluir(populacao, peso_maximo, pesos_valores, num_cromossomos)

    #A cada evolução calcula a media fitness da população para ser plotado no gráfico
    historico_fitness.append(media_fitness(populacao, peso_maximo, pesos_valores))

#Printar a média de valor na mochila a cada geração
for indice, dados in enumerate(historico_fitness):
    print("Geração", indice, "| Média de valor na mochila: ", dados)

#Printar o peso disponivel na mochila
print("\nPeso máximo:",peso_maximo,"g\n\nItens disponíveis:")

#Printar o valor e o peso de cada item
for indice,i in enumerate(pesos_valores):
    print("Item ",indice+1,": ",i[0],"g | R$",i[1])

#Printar algumas boas soluções
print("\nExemplos de boas solucoes: ")
for i in range(5):
    print(populacao[i])

#Gerar o gráfico 
from matplotlib import pyplot as plt
plt.plot(range(len(historico_fitness)), historico_fitness)
plt.grid(True, zorder=0)
plt.title("Problema da mochila")
plt.xlabel("Geracao")
plt.ylabel("Valor medio da mochila")
plt.show()
