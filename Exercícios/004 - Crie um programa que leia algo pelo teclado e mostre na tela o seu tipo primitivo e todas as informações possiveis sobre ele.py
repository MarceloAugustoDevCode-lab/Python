# Desafio: 02
# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
seutipo = input('Digite seu tipo ? ')

print('Tipo original:',type(seutipo))
print('ele tem spaço: ',seutipo.isspace())
print('ele e Numerico: ',seutipo.isnumeric())
print('ele e letra: ',seutipo.isalpha())
print('ele e letra e numero: ',seutipo.isalnum())
print('ele esta Maiúsculo: ',seutipo.isupper())
print('ele esta Minúsculo: ',seutipo.islower())
print('ele esta Capitalizada: ',seutipo.istitle())