numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['lavar', 'barrer', 'cocinar']
print(tasks)

types = [1, True, "Hola"]
print(types)

print(numbers[0])
print(tasks[0])

text = 'Hola'
# text[0] = 'W' # No se puede editar un texto

tasks[0] = "Ver TV"
print(tasks)
tasks[0] = "lavar"
print(tasks)

# Aplicando slicing
print(numbers[:3])
print(True in types)
print('Hola' in types)