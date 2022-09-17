# **Создание викторин** - Напишите приложение, которое берёт набор вопросов из файла, выбирает из них несколько штук случайным образом, и предлагает студентам в виде викторины. Каждый набор вопросов может быть уникальным, и затем подсчитайте количество правильных ответов, которые ввел пользователь.
import random
import sys
from questions import allQuestions
from colorama import init, Fore, Back, Style # для созлания разноцветного текста в программе (pip install colorama)
import time  # для создания эффекта печатания текста с задержкой


# 1 вариант

count = 0 # счетчик для подсчета очков игрока
uniqueQuestion = []  #переменная, куда будут попадать только уникальные значения (вопросы), т.е. без повторения. Это необходимо чтоб вопросы не повторялись

print(Style.BRIGHT + Fore.BLUE)
wordTitle = '   Мы приветствуем Вас на нашей викторине!!! '
# создаем эффект печатания текста (текст выводиться с задержкой)
for i in wordTitle:
    print(i.upper(), end="")
    time.sleep(0.03)
    

def playGame():  
    global count   
        
    questionRandom = random.choice(list(allQuestions.items()))
    if  questionRandom in uniqueQuestion: #проверяем содержиться ли вопрос в списке и если содержится пропускаем и запускаем функцию заново
        playGame()
    uniqueQuestion.append(questionRandom)#если вопроса до этого не было, тогда добавляем его в наш список

    print()
    print('-----------------------------------------------')
    print(Style.BRIGHT + Fore.WHITE)
    print(questionRandom[0]) # выводим на экран полученный случайный вопорос(он всегда под индексом 1, т.к. мы преобразовали словарь в строки, а под индексом 1 храниться ключ, который и является правильным ответом. Его мы будем в дальнешем сравнивать)
    print(Style.BRIGHT + Fore.GREEN)

    def chooseVariant (): # Проверяем варианты ответов пользователя
        global count   

        x = input('Выберите ответ: ')
        answerUser = x.upper() #если пользователь вводит в нижнем регистре. Приводим в верхний, т.к. значениня в словаре (ответы) написаны с большой буквы
               
        if answerUser == questionRandom[1]:
            print(Style.BRIGHT + Fore.YELLOW)
            print('Вы заработали 1 очко!')
            count += 1

        elif answerUser != 'А' and answerUser != 'Б' and answerUser != 'В' and answerUser != 'Г':
            print(Style.BRIGHT + Fore.RED)
            print('Выберите один из вариантов (нажав соответсвующую букву)')
            chooseVariant()
        
        else:
            print(Style.BRIGHT + Fore.RED)
            print('ответ неверный')

    chooseVariant ()

    if len(uniqueQuestion) == len(allQuestions):
        print(Style.BRIGHT + Fore.YELLOW)
        print('$$$$$$$$$$$$$$$$$$$$$$$$')
        
        print(f"Всего за всю игру Вы заработали {count} очков")

        print('$$$$$$$$$$$$$$$$$$$$$$$$')
        print(Style.BRIGHT + Fore.WHITE)
        againPlay = input('Хотите сыграть еще? Нажмите "д", если хотите. Если не хотите нажмите любую клавишу   ')
        if againPlay == 'д':
            uniqueQuestion.clear() # очищаем список с вопросами
            playGame() #запускаем игру
        else: 
            sys.exit() #если пользователь отказаляся играть, то выходим из игры

    playGame()

playGame()


