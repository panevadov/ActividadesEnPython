def suma(numero):
    acum = 0
    for n in numero:
        acum += n
    return acum

suma([1,2,3,4,5])

def sumar_lista():
    suma = 0
    m = 0  #aumenta los numeros, correr los numeros
    i = 0  #contador de pares/condicion de rompimiento
    while i <= 50:
        if m % 2 == 0:
            i += 1
            suma += m
        m += 1
    return suma    

sumar_lista()

s = 0
for n in range(10):
    s += n
print (s)     

n = 10
while n<=10:
    print('Prueba')

def es_primo(numero):
    resultado = True
    for divisor in range(2, numero):
        if (numero % divisor) == 0:
            print(numero, 'es igul a ', divisor, '+', numero/divisor)           
            resultado = False        
            continue
        print(numero, "es un numero primo")
    return resultado

es_primo(13)

s = 0
for n in range(1, 10):
    if n % 7 == 0:
        break
    s += n
print(s)


s = 0
for n in range(1, 10):
    if n % 2 == 0:
        continue
    s += n
print(s)

s = 0
for n in range(1, 10):
    if n % 11 == 0:
        break
    s += n
else:
    s += 10
print(s)

s = 0
for n in range(1, 10):
    if n % 2 == 0:
        pass
    s += n

print(s)

s = 0
for n in range(1, 10):
    if n % 2 != 0:
        continue
    s += n
else:
    s +=5

print(s)


class SumaDos:
    def __init__(self, datos):
        self.datos = datos
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == len(self.datos):
            raise StopIteration()
        elemento = self.datos[self.indice] + 2
        self.indice += 1
        return elemento

list(SumaDos([1,2,3,4,5]))