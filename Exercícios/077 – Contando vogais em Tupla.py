
listapalavaras = ('aprender','programar')
contagem = len(listapalavaras)# numero de contage é 2
print(listapalavaras)
c=0
while c != contagem:
    c+=1
    if c:
        print('')
    vogais='aeiou'
    palavras = listapalavaras[c-1]
    print(f'Na palavra {palavras} temos ', end='')
    palavra = listapalavaras[c-1]
    for vogal in palavra.lower():
        if vogal.isalpha():
            if vogal.lower() in vogais:
                print(f'{vogal} ', end='')