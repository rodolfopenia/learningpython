my_dict = {}
print(type(my_dict))

my_dict = {
  'name': 'Rodo',
  'last_name': 'Peña',
  'age': 31
}

print(my_dict)
print(len(my_dict))
print(my_dict['name'])
print(my_dict['age'])
print(my_dict.get('last_name'))

print('name' in my_dict)
print('avion' in my_dict)