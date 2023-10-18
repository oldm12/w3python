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
print(color.BOLD, color.GREEN+"Python Introduction start" +color.END)

# Creating Variables

x = 5
y = "John"
print(x)
print(y)

a = 3       # a is of type int
a = "sad"   # a is of type str
# напечатает последнее присвоенное значение переменной а
print(a)

# Casting - вывод значения в переменной в нужном типе (классе)
b = str(7)      # b will be '7' - text
c = int(7)      # c will be 7 - number
d = float(7)    # d will be 7.0 - number

print(b, c, d)

# Get the Type - вывод типа (класса) присвоенного переменной
e = 9
f = "Word"
g = 8.0

print(type(e)) # print type "e" -> class 'int'
print(type(f)) # print type "f" -> class 'str'
print(type(g)) # print type "g" -> class 'float'

# is the same as - одинаковый синтаксис
h = "ball"
h = 'ball'

# A will not overwrite a - не перезапишет, разные переменные
a = 4
A = "hat"

print(A, a)

myvar = "one"
my_var = "two"
_my_var = "three"
myVar = "four"
MYVAR = "five"
myvar2 = "six"

print(myvar, my_var, _my_var, myVar, MYVAR, myvar2)

"""
Camel Case
Верблюжий чехол -> 
Каждое слово, кроме первого, 
начинается с заглавной буквы.
"""
myNameVar = "rat"

"""
Pascal Case
Паскаль Кейс
Каждое слово начинается 
с заглавной буквы.
"""
MyNameVar = "bat"

"""
Snake Case
Змеиный случай
Каждое слово отделяется 
символом подчеркивания.
"""
my_name_var = "cat"

pr = ","

print(myNameVar, pr, MyNameVar, pr, my_name_var, "\n")


# Many Values to Multiple Variables
o, p, q = "orange", "banana", "cherry"
print(o)
print(p)
print(q)

l = m = n = "raspberry"
print(l)
print(m)
print(n)


#Unpack a Collection 
"""
 Если у вас есть набор 
 значений в списке, кортеже и т. д. 
 Python позволяет извлекать 
 значения в переменные. 
 Это называется распаковка.
"""

fruits = ["apple", "banana", "cherry"]
#Кол-во переменных должно совпасть с кол-вом елементов в массиве
r, t, u = fruits 
print(r)
print(t)
print(u)


#Output Variables
xp = "Python is awesome"
print(xp)

xe = "Python"
ye = "is"
ze = "awesome 2"
print(xe, ye, ze)

xk = "Python "
yk = "is "
zk = "awesome 3"
print(xk + yk + zk)

xa = 5
ya = 10
print(xa + ya)


#Global Variables
kr = "awesome 4"

def myfunc():
   print("Python is " + kr)

myfunc()

sd = "awesome 5"

def my_func():
   sd = "fantastic"
   print("Python is " + sd)

my_func()

print("Python is " + sd)


#The global Keyword
def MyFunc():
   global s
   s = "wery well"

MyFunc()
print("Python is " + s)

ab = "apple"
print(ab)

def my_Func():
   global ab
   ab = "rasoberry"

my_Func()

print("My favorite fruit is " + ab)
