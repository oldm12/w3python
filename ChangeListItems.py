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
print(color.BOLD, color.GREEN+"Python Access List Items start" +color.END)

# example1 - Присвоєння іншого значення елементу в масиві
print(color.PURPLE+"example 1 - Присвоєння іншого значення елементу в масиві" +color.END)
thisList = ["apple", "banana", "cherry"]
print(thisList)

print(color.BLUE+"Заміна елементу в масиві" +color.END)
thisList[1] = "blackcurrant"        # черная сородина
print(thisList)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(color.BLUE+"Заміна декількох елементів в масиві" +color.END)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thisList = ["apple", "banana", "cherry"]
print(thisList)
print(color.BLUE+"Заміна елементу та додавання елементу в масив" +color.END)
print("thisList[1:2]")
thisList[1:2] = ["blackcurrant", "watermelon"]  # 1й елемент заміна, 2й елемент додасться сдвинувши ряд 
print(thisList)

print("thisList[1:3]")
thisList[1:3] = ["watermelon"]
print(thisList)

# example2 - Метод Insert() вставляет элемент по указанному индексу без замены каких-либо существующих значений
print(color.PURPLE+"example 2 - insert() method" +color.END)
thislistIns = ["apple", "banana", "cherry"]
print(thislistIns)
thislistIns.insert(2, "watermelon")
print(color.BLUE+"thislistIns.insert(2, 'watermelon')" +color.END)
print(thislistIns)


