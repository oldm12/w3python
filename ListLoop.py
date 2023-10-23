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
print(color.BOLD, color.GREEN+"Python Loop Lists start" +color.END)

# Loop Lists
# example1 - Loop Through a List. Using a for loop:
print(color.PURPLE+"example 1 - Loop Through a List. Using a for loop:" +color.END)
thislist = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thislist)
print(color.BLUE + "Перебір циклом та вивід поелементно:" + color.END)
for x in thislist:
   print(x)

# example2 - Loop Through the Index Numbers. Use the range() and len() functions:
print(color.PURPLE+"example 2 - Loop Through the Index Numbers. Use the range() and len() functions:" +color.END)
thislist2 = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thislist2)
print(color.BLUE + "Перебір for i in range(len(thislist2)) та вивід поелементно:" + color.END)
for i in range(len(thislist2)):
   print(thislist2[i])


# example3 - using a while:
print(color.PURPLE+"example 3 - using a while:" +color.END)
thislist3 = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thislist3)
print(color.BLUE + "Перебір циклом while та вивід поелементно:" + color.END)
i = 0
while i < len(thislist3):
   print(thislist3[i])
   i = i + 1


# Looping Using List Comprehension предлагает самый короткий синтаксис для циклического перемещения по спискам:
# example4 - using 'for'
print(color.PURPLE+"example 4 - using FOR:" +color.END)
thislist4 = ["apple", "banana", "cherry"]
print("Початковий масив:")
print(thislist4)
[print(x) for x in thislist4]


