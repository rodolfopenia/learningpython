numbers = (1, 2, 3, 5)
strings = ('rodo', 'nelva', 'vivi', 'vivi')
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# Una tupla no se puede editar
print(strings)
print(strings.index('nelva'))
print(strings.count('vivi'))

# Si podemos convertir una tupla a lista
my_list = list(strings)
print(my_list)
print(type(my_list))

my_typle = tuple(my_list)
print(my_typle)
print(type(my_typle))