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

# example1
print(color.PURPLE+"example 1" +color.END)
thisList = ["apple", "banana", "cherry"]
print(thisList[1])          # wiil be "banana"

# Negative Indexing
# Отрицательная индексация означает 
# начало с конца -1 относится к последнему элементу, 
# -2 относится к предпоследнему элементу

# example2
print(color.PURPLE+"example 2" +color.END)
thisList = ["apple", "banana", "cherry"]
print(thisList[-1])          # wiil be "cherry"

# example3
print(color.PURPLE+"example 3" +color.END)
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])          # wiil be ['cherry', 'orange', 'kiwi'] 
# Поиск начнется с индекса 2 (включен) и 
# закончится индексом 5 (не включен).

print(thisList[:4])         # wiil be ['apple', 'banana', 'cherry', 'orange'] 
print(thisList[2:])         # will be ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thisList[-4:-1])      # will be ['orange', 'kiwi', 'melon']
print(thisList[-1:-4])      # will be [] - записть ошибка выводит строго с лева на право элементы

# example4
print(color.PURPLE+"example 4" +color.END)
thisList = ["apple", "banana", "cherry"]
if "apple" in thisList:
   print("Yes, 'apple' is in the fruits list")
   

# example5
print(color.PURPLE+"example 5" +color.END)
thisList = ["apple", "banana", "cherry"]
if "kiwi" in thisList:
   print("Yes, 'apple' is in the fruits list")
else:
   print("No, 'kiwi' is not in the fruits list")










