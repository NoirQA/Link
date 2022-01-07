# Ипортируем модуль random и объявляем перменную winner
import random

winner = ''
random_choice = random.randint(0,2)
#random_choice

# случайным образом определяем значенеие от 0 до 1 и сопоставляем с текстовым значение
if random_choice == 0:
    computer_choice = 'Камень'
elif random_choice == 1:
    computer_choice = 'Бумага'
else:
    computer_choice = 'Ножницы'
# print('Компьютер вырал', computer_choice)

# в этом блоке мы запрашиваем у пользователя его выбор
user_choice = ''
while (user_choice != 'Камень' and
       user_choice != 'Бумага' and
       user_choice != "Ножницы"):
    user_choice = input('введите, Камень, Ножницы или Бумага: ')
# print('Ты выбрал', user_choice, 'Компютер выбрал', computer_choice)

# в этих условиях описываеться логика игры и определение победителя
# и проверяем ввод пользователя
if computer_choice == user_choice:
    winner = 'ничья'
elif computer_choice == 'Бумага' and user_choice == 'Камень':
    winner = 'Компьютер'
elif computer_choice == 'Камень' and user_choice == 'Ножницы':
    winner = 'Компьютер'
elif computer_choice == 'Ножницы' and user_choice == 'Бумага':
    winner = winner = 'Компьютер'
else:
    winner = 'Человек'
# выводим результыт , пебедитель в игре ! или ничью
if winner == 'ничья':
    print('Мы оба вырали',computer_choice +'!','Еще играем ?')
else:
    print(winner,'выиграл! Я выбрал',computer_choice)
