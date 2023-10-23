import os
os.system('cls')

print ("os name:", os.name, "\n") 


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

"""
Выводит 
отформатированный 
текст
"""
print(color.BOLD, color.GREEN+"Python Lists start" +color.END)

# example1
print(color.PURPLE+"example 1" +color.END)
myList = ["apple", "banana", "cherry"]
print(myList)

# example2
print(color.PURPLE+"example 2" +color.END)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Чтобы определить, сколько элементов содержит список, используйте функцию len():
# example3
print(color.PURPLE+"example 3" +color.END)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))

# example3
print(color.PURPLE+"example 3" +color.END)
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, False, 40, "male"]

print(list1)
print(list2)
print(list3)
print(list4)

# type()
print(type(list1))          # will be <class 'list'>

# конструктор list()
thislist = list(("apple", "banana", "cherry"))
print(thislist)

"""
Коллекции Python (массивы)
В языке программирования Python существует четыре типа данных коллекций:

List - Список — это упорядоченная и изменяемая коллекция. 
Позволяет дублировать участников.

Tuple - Кортеж — это упорядоченная и неизменяемая коллекция.
 Позволяет дублировать участников.

Set - Набор — это неупорядоченная, неизменяемая* 
и неиндексированная коллекция. 
Никаких повторяющихся участников.
можете удалять и/или добавлять элементы в любое время.

Dictionary - Словарь - представляет собой 
упорядоченную** и изменяемую коллекцию. 
Никаких повторяющихся участников.
**Начиная с версии Python 3.7, словари упорядочены.
"""
