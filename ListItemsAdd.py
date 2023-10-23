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
print(color.BOLD, color.GREEN+"Python Add List Items start" +color.END)

# example1 - Чтобы добавить элемент в конец списка append() method:
print(color.PURPLE+"example 1 - Чтобы добавить элемент в конец списка append() method:" +color.END)
thisList = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thisList)
thisList.append("orange")
print(color.BLUE + "Додаємо: orange" + color.END)
print("Кінцевий масив:")
print(thisList)


# example2 - Чтобы вставить элемент списка по указанному индексу insert() method:
print(color.PURPLE+"example 2 - Чтобы вставить элемент списка по указанному индексу insert() method" +color.END)
thisList = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thisList)
thisList.insert(1, "orange")
print("Кінцевий масив:")
print(thisList)

# Extend List
# example3 - Чтобы добавить элементы из другого списка в текущий список extend() method:
print(color.PURPLE+"example 3 - Чтобы добавить элементы из другого списка в текущий список extend() method:" +color.END)
thislist1 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]  # pineapple - ананас
print("Початковий масив:")
print(thislist1)
thislist1.extend(tropical)
print("Кінцевий масив:")
print(thislist1)


# Add Any Iterable
# example4
print(color.PURPLE+"example 4 - extend() method:" +color.END)
thisList = ["apple", "banana", "cherry"]
thisTuple = ("kiwi", "orange")
print("Початковий масив:")
print(thisList)
thisList.extend(thisTuple)
print("Кінцевий масив після поєднання з кортежем:")
print(thisList)

