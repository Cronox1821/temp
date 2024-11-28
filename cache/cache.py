
# Problema 7

def fase(n, mes_inicial = 3):
    if n == 0:
        return mes_inicial
    else:
        return fase(n-1, mes_inicial) * 0.9

lista = list()

for i in range (0,10):
    lista.append(fase(i))
    print(f'Fase {i+1}: {fase(i):.0f}')

print(round(sum(lista),1))
# Problema 4

"""
lista = list()

def no():
    return 2

for i in range(1,101):
    print(i) if i % 2 == 0 else no()
    lista.append(i) if i % 2 == 0 else no() 

print(f'Valor decimo termino {lista[9]}')

print(f'Suma de los primeros 100 numeros pares {sum(lista)}')

print(f'El numero 58 se encuentra en la posicion {lista.index(58)+1}')
print(f'{lista[28]}')

"""

# Problema 5
"""
def calc_usuario(n, usuarios_iniciales = 500):
    if n == 0:
        return usuarios_iniciales
    else:
        return calc_usuario(n-1, usuarios_iniciales) * 1.15

lista = list()

for i in range(1,13):
    lista.append(calc_usuario(i))
    print(f'Mes {i}: {calc_usuario(i)}')

print(sum(lista))

"""

