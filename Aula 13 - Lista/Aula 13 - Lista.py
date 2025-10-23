#Aula variaveis composta (lista parte 1)
#para usar listas em python e preciso usar [].

lanche = ['pizza','copo','pudin','queijo']

# As listas são mutaveis. ex:
lanche[3] = 'picole'
print(lanche)

# Para adicionar na lista vai usar o comando append('bis')
lanche.append('bis')
print(lanche)

# O comando insert(0,'tomate') passara ser o 0 e o resto ganhara novas posições.
print(lanche)

# Para excluir indice da lista.Lembrando que a lista modificara os indices da posição.
del lanche[3] # picole
lanche.pop(3) # Você retira o ultimo da lista.
lanche.remove('pizza')

#confirir para remover da lista sem dar erro, e com if e in.
if 'pizza' in lanche:
    lanche.remove('pizza')
print(lanche)



# posso usar o range tambem
valores = list(range(4,11))
print(valores)

# para ordena todos valores uas sort()
valores.sort()
print(valores)

# Para ficar ordem reversa usa reverse =true
valores.sort(reverse=True)
print(valores)

# Saber quantos elementos tem aqui.
print(len(valores))

# pratica ex1:

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v} ', end='')

#ex2:
valores1 = []
valores1.append(5)
valores1.append(9)
valores1.append(4)
for c, v in enumerate(valores1):
    print(f'\n Na posição {c} encontrei o valor {v}!', end='')
print(' Cheguei ao final da lista.')

# ex3:
valores2 = list()
for c1 in range(0,5):
    valores2.append(int(input(f'Digite o valor {c1}: ')))
for c1, v1 in enumerate(valores2):
    print(f'\n Na posição {c1} encontrei o valor {v1}!', end='')
print(' Cheguei ao final da lista.')
