

c = 0
print('Lista de produtos:')
while True:
    listaProdutos = 'CPU',900,'GABINETE',150,'MEMORIA-RAM',300,'PLACA-MAE',500
    for c in range(0, 8,2):
        lista_itens = listaProdutos[lista_itens]
    listapreco = listaProdutos[1]
    print(f' - {lista_itens}................R$ ')
    c += 1
    if c > 5:
        break
