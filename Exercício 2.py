'''Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final,
escrever a localização (linha e coluna) ou uma mensagem de "não encontrado".'''

m = []
h = []
for i in range(1, 6): # Criando a matriz
    linha = []
    for n in range(1, 6):
        linha.append(i * n)
    m.append(linha)

x = int(input())

for im, vm in enumerate(m): # Buscando o valor de x na matriz
    if x in vm:
        h.clear()
        h.append([im + 1, vm.index(x) + 1])
        print(f'Encontrado na localização {h} \n')

if h == []:
    print(f'Valor não encontrado na matriz')

for x in m:
    print(x)