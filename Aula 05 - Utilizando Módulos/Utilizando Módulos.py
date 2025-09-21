# Trabalhando com Modulos.

# Bibliotecas podemos fazer importação no Python.
# Dentro da linguagem python incluir alguma coisa tenho que usar o comando  Import.

# exemplo, math em português e matematica.

#import math

# mais se eu quiser so uma funcionalidade de math em vez de usar toda biblioteca. eu uso o from.

#from math import pow # e potencia.

# algumas funções do math

# ceil - ele redonda pra cima.
# floor - ele redonda pra baixo.
# trunc - truncar o numero ele vai eliminar da , pra frente.
# pow - e a potencia.
# sqrt - e para calcular a raiz quadrada.
# factorial - e usada para calculo fatorial.

# e se eu quiser import duas ficara dessa forma.

#from math import sqrt,floor

# pratica
'''
import math
numero = int(input('digite um numero: '))
raiz = math.sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero,raiz))

# usando ceil
numero2 = int(input('digite um numero: '))
raiz2 = math.sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero2,math.ceil(raiz2)))

# usando floor
numero3 = int(input('digite um numero: '))
raiz3 = math.sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero3,math.floor(raiz3)))
'''

# agora com from fara mesma coisa

from math import sqrt,floor,ceil
numero = int(input('digite um numero: '))
raiz = sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero,raiz))

# para ter acesso a mais bibliotecas voce pode acessar pypi.python.org.



