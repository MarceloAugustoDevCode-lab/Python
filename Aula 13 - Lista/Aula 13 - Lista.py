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