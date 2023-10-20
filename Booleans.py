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
print(color.BOLD, color.GREEN+"Python Booleans start" +color.END)

# example1
print(10 > 9)           # will be True
print(10 == 9)          # will be False
print(10 < 9)           # will be False

# example2
print(color.PURPLE+"example 2" +color.END)
a = 200
b = 33

if b > a:
   print("b is greater than a")
else:
   print("b is not greater than a")

# example3
print(color.PURPLE+"example 3" +color.END)
print(bool("Hello"))
print(bool(15))         # не понятно что делает

# example4
print(color.PURPLE+"example 4" +color.END)
x = "Hello"
y = 15
print("x = " + x + "\ny = " + format(y))
print(bool(x))
print(bool(y))

# example5
"""
Почти любое значение оценивается как True, 
если оно имеет какой-либо контент. 
Любая строка имеет значение True, 
кроме пустых строк. 
Любое число истинно, кроме 0. 
Любой список, кортеж, набор и словарь имеют значение True,
 за исключением пустых.
"""
print(color.PURPLE+"example 5 - виводить значення" +color.END)     
bool("abc")                                     # will be True
bool(123)                                       # wiil be True
bool(["apple", "cherry", "banana"])             # will be True

# example6
"""
False -> (), [], {}, "", 
числа 0 и значения None. 
значение False принимает значение False.
"""
print(color.PURPLE+"example 6 - виводить значення" +color.END)
bool(False)         # will be False
bool(None)          # wiil be False
bool(0)             # will be False
bool("")            # wiil be False
bool(())            # wiil be False
bool([])            # will be False
bool({})            # will be False

# example7 - a __len__ function that returns 0 or False:
print(color.PURPLE+"example 7" +color.END)
class myClass():
   def __len__(self):
      return 0
   
myObj = myClass()
print(bool(myObj))

# example8 - You can create functions that returns a Boolean Value:
print(color.PURPLE+"example 8" +color.END)
def myFunction():
   return True
print(myFunction())

# example9 - You can create functions that returns a Boolean Value:
print(color.PURPLE+"example 9" +color.END)
def myFunc():
   return True
if myFunc():
   print("Yes!")
else:
   print("No!")

# example10 - возвращающих логическое значение, 
# функцию isinstance(), 
# можно определит, принадлежит ли объект к определенному типу данных:
print(color.PURPLE+"example 10" +color.END)
x = 200
y = 4.5
print(isinstance(x, int))
print(isinstance(y, int))


