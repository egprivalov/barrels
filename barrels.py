import logging
import keyboard as kb
from random import shuffle

#Инициализация logging
logging.basicConfig(filename="LogFile.log", level=logging.INFO)

#Функция проверки ввода
def GvBrrl(event):
    global is_running, check
    inp = event.name
    if inp == 'space':
        print(f'Ваш бочонок: {barrels.pop(0)}')
        if len(barrels) == 0:
            check = True
            is_running = False
        logging.info(f"Good input! Input = {inp}")
    elif inp == 'esc':
        is_running = False
        logging.info(f"Good input! Input = {inp}")
    elif inp != 'shift':
        print("Нажмите пробел-для выдачи нового бочонка или esc для выхода")
        logging.exception(f"Bad input! Input = {inp}")

#Переменная отвечающая за работу цикла
is_running = True
#Переменная проверки окончания бочонков
check = False

#Ввод n
while True:
    try:
        print("Введите количество бочонков: ", end=" ")
        inp = input()
        n = int(inp)
        if n < 0:
            print("Число должно быть положительным! Попробуйте снова")
            logging.exception(f"Error! Input: {inp}. Need to be positive.")
            continue
        else:
            break
    except ValueError:
        logging.exception(f"Error! Input: {inp}. Need to be integer")
        print("Неккорректный ввод. Попробуйте снова.")

#Массив бочонков
barrels = [i for i in range(1, n+1)]
shuffle(barrels) #Перемешиваем
print("Для получения бочонка нажмите Пробел\nДля выхода нажмите esc")
kb.on_press(GvBrrl)

while is_running:
    pass

if check:
    print("Бочонки закончились!")

print("До свидания - возвращайтесь еще")