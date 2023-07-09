name = "Rodolfo"
last_name = "Peña"
age = 31
city_live = "Lima"
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Rodolfo"
print(quote)

quote2 = 'She said: "Hello, Im Sonia"'
print(quote2)

quote3 = '''She said: "I'm Sonia"'''
print(quote3)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name,last_name)
print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)

template = f"Hola, mi nombre es {name} {last_name}, mi edad es {age} y vivo en {city_live}"
print('v4', template)