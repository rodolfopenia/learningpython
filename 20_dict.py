person = {
  'name': 'Rodo',
  'last_name': 'Peña',
  'langs': ['NET', 'Angular', 'Python'],
  'age': 31
}

print(person)

person['city'] = 'Lima'
person['age'] = 25
person['langs'].append('Rust')
print(person)

del person['last_name']
person.pop('age')
print(person)

print('items')
print(person.items())
print('keys')
print(person.keys())
print('values')
print(person.values())