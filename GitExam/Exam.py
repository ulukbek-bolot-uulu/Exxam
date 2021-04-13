# Task_1
# 1.1 Integer
# 1.2 Boolean
# 1.3 Dictionary
# 1.4 Sets
# 1.5 Boolean
# 1.6 Boolean
# 1.7 Integer
# 1.8 String
# 1.9 List
# 1.10 Dictionary

# Task 2

# Task 3_1

# def func_list(*args):
#     return ['Element', 'start', *args, 'finish']
#
# print(func_list(*['Hello', 5, 'go']))

# 3_2

# def func_list2(vvod, *args):
#     print()
# print(func_list2())
def myList(*args):
    print("Dict: ", args)
    return myList(list.index(x[, start[, end]]))
#
# myList('x',5,'John')
someDict = {}
word = 'foo'
definition = 'bar'
someDict.update(word=definition)
print(someDict)

# 3_3
# def func_list3():
#     return lambda x:
# print(func_list3())

# Task_4
import telebot

bot = telebot.TeleBot('1737249823:AAEFtrXPhA2eEt5AZlfvurIGevhuhte0mdk')

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать..!')

@bot.message_handler(content_types=['text'])
def read_message(message):
    vowels = 'aeouiyAEOUIY'
    i = 0
    numa = 0
    nume = 0
    numo = 0
    numu = 0
    numi = 0
    numy = 0
    while i < len(message.text):

        if message.text[i] in vowels:
            if message.text[i] == 'a' or message.text[i] == 'A':
                numa += 1
            elif message.text[i] == 'e' or message.text[i] == 'E':
                nume += 1
            elif message.text[i] == 'o' or message.text[i] == 'O':
                numo += 1
            elif message.text[i] == 'u' or message.text[i] == 'U':
                numu += 1
            elif message.text[i] == 'i' or message.text[i] == 'I':
                numi += 1
            elif message.text[i] == 'y' or message.text[i] == 'Y':
                numy += 1

        i += 1
    bot.send_message(message.chat.id, 'Letter a repeats ' + str(numa) + ' times')
    bot.send_message(message.chat.id, 'Letter e repeats ' + str(nume) + ' times')
    bot.send_message(message.chat.id, 'Letter o repeats ' + str(numo) + ' times')
    bot.send_message(message.chat.id, 'Letter u repeats ' + str(numu) + ' times')
    bot.send_message(message.chat.id, 'Letter i repeats ' + str(numi) + ' times')
    bot.send_message(message.chat.id, 'Letter y repeats ' + str(numy) + ' times')


bot.polling()
