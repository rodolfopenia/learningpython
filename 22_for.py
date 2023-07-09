'''
for element in range(1, 21):
  print(element)

'''

my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)

product = {
  'name': 'camisa',
  'price': 100,
  'stock': 89
}

for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'Rodo',
    'age': 31
  },
  {
    'name': 'Vivi',
    'age': 34
  },
  {
    'name': 'Santi',
    'age': 25
  }
]

for person in people:
  print('name =>', person['name'])