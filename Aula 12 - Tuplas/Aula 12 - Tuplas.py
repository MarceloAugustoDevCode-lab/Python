# Variavés composta: TUPLAS as TUPLAS são imutáveis.
#variavel simples:
lanche1 = 'Hamburgue'

#variavel composta a tuplas, lista e dicionario : vamos usar tupla

lanche = ('hamburgue', 'suco','pizza','pudin')

print(lanche)
print(lanche[1])# e o suco
print(lanche[-2])# pizza
print(lanche[1:3])# suco e pizza
print(lanche[:2])# hamburgue e suco
print(lanche[-2:])# pizza e pudin
print(lanche[-3])# pudin
print(lanche[2]) #ele vai mostra pizza
print(lanche[0:2]) # ele vai mostra hamburgue, suco no python vai ate 0 1 o 2 nao mostra.
print(lanche[1:])# vai do suco ate o pudin
print(len(lanche)) # quantos elementos tem no lanche que e 4



# com estrutura for.
for c in lanche: #
    print(c)

for cont in range(0, len(lanche)):
    print(cont)

for cont1 in range(0, len(lanche)):
    print(lanche[cont1])

# contando a posição:
for cont2 in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont2]} na posição {cont2}')

#ou desse jeito.
for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# o sorted coloca em ordem alfabetica.
print(sorted(lanche))


