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
print(color.BOLD, color.GREEN+"Python Remove List Items start" +color.END)

# Remove Specified Item
# example1 - Удалить указанный элемент Метод Remove() удаляет указанный элемент.
print(color.PURPLE+"example 1 - Удалить указанный элемент Метод Remove() удаляет указанный элемент" +color.END)
thislist = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thislist)
thislist.remove("banana")
print("Кінцевий масив після Метод Remove():")
print(thislist)

# example2 remove()
print(color.PURPLE + "example 2 " + color.END)
thislistfruits = ["apple", "banana", "cherry", "banana", "kiwi"]
print("Початковий масив:")
print(thislistfruits)
thislistfruits.remove("banana")
print(thislistfruits)

# Remove Specified Index
# example3 Метод pop() удаляет указанный индекс.
print(color.PURPLE + "example 3  Метод pop() удаляет указанный индекс:" + color.END)
thislist = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thislist)
thislist.pop(1)
print("thislist.pop(1) Кінцевий масив Метод pop()")
print(thislist)


# example4 Метод pop() удаляет указанный индекс.
print(color.PURPLE + "example 4  Метод pop()" + color.END)
thislist1 = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thislist1)
thislist1.pop()     # will be ['apple', 'banana'] delete last element
print("thislist.pop() Кінцевий масив Метод pop()")
print(thislist1)


# example5 del.
print(color.PURPLE + "example 5 'del':" + color.END)
thislist2 = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thislist2)
del thislist2[0]
print("'del thislist2[0]' Кінцевий масив:")
print(thislist2)

thislist = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thislist)
del thislist            # успешно удалили «этот список».
print("'del thislist' Видалив масив:")
# print(thislist)         # NameError: name 'thislist' is not defined. 


# Clear the List
# example6 clear() method
print(color.PURPLE + "example6 clear() method:" + color.END)
thislist3 = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thislist3)
thislist3.clear()
print("'clear()' Видалив елементи з масиву:")
print(thislist3)



