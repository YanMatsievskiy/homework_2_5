'''Задача 5. Камень, Ножницы, Бумага'''

print('Выбирете один из трёх вариантов: Камень, Ножницы, Бумага')
player_one = input('Первый игрок, введите свой выбор: ').lower()
player_two = input('Второй игрок, введите свой выбор: ').lower()

if player_one == player_two:
  print('Ничья!')

elif player_one == 'камень' and player_two == 'ножницы':
  print('Победил первый игрок!')
elif player_one == 'ножницы' and player_two == 'бумага':
  print('Победил первый игрок!')
elif player_one == 'бумага' and player_two == 'камень':
  print('Победил первый игрок!!')

elif player_two == 'камень' and player_one == 'ножницы':
  print('Победил второй игрок!')
elif player_two == 'ножницы' and player_one == 'бумага':
  print('Победил второй игрок!')
elif player_two == 'бумага' and player_one == 'камень':
  print('Победил второй игрок!')

else:
  print('Ошибка! Выбирете один из трёх вариантов: Камень, Ножницы, Бумага')