listaProdutos = 'CPU',900,'GABINETE',150,'MEMORIA-RAM',300,'PLACA-MAE',500
print('Lista de produtos:')
for lista_itens in range(0, len(listaProdutos),2):
    lista_itens = listaProdutos[lista_itens]
    print(f' - {lista_itens}................R$',end=' ')
for listapreço in range(1, len(listaProdutos),2):
    listapreço = listaProdutos[listapreço]
    print(listapreço ,end=' ')