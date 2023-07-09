import random

options = ('piedra', 'papel', 'tijera')

bot_wins = 0
user_wins = 0
rounds = 1

while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)
  print('Computadora =>', bot_wins)
  print('Usuario =>', user_wins)
  
  user_option = input('Piedra, papel o tijera => ')
  user_option = user_option.lower()
  if not user_option in options:
    print('Esa opción no es válida')
    continue
  
  computer_option = random.choice(options)
  
  print('User option =>', user_option)
  print('Bot option =>', computer_option)
  
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user ganó')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('computador ganó')
      bot_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user ganó')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computador ganó')
      bot_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user ganó')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computador ganó')
      bot_wins += 1

  if bot_wins == 2:
    print('El rotundo ganador es la computadora')
    break;
  if user_wins == 2:
    print('El rotundo ganador es el usuario')
    break;
  rounds += 1