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
print(color.BOLD, color.GREEN+"Python Strings start" +color.END)

# Strings 'hello' is the same as "hello"
print("Hello")
print('Hello')

a = "Hello"
print(a)

b = """
Что-то нужно написать, 
чтобы было много текста. 
Формат с переходом на строку
Двойные кавычки. 
"""
print(b)

c = '''
Что-то нужно написать, 
чтобы было много текста. 
Формат с переходом на строку
Одинарные кавычки
'''
print(c)

# Strings are Arrays
d = "Hello, World!"
print(a[1])         # print will be "e"

# Looping Through a String
for x in "banana":
   print(x)         # print will be "b" "a" "n" ... "a"

# String Length
f = "Hello, World!" # print will be 13
print(len(f))

# Check String
"""
Чтобы проверить, 
присутствует ли в строке 
определенная фраза или символ, 
мы можем использовать ключевое слово in.
"""

tet = "The best things in life are free!"
print("free" in tet)                # print will be "True"

if "free" in tet:
   print(color.BOLD, color.GREEN + "Yes, 'free' is present.", color.END)

# Check if NOT
tet = "The best things in life are free!"
print("expensive" not in tet)       # print will be "True"

if "expensive" not in tet:
   print(color.BOLD, color.RED + "No, 'expensive' is NOT present.", color.END)


# Slicing Strings
# from position 2 to position 9 (not included):
"""
В квадратных скобках указывается 
диапазон от и до ...(
последний не включается
) 
Второй элемент включен, а девятый нет.
"""
b = "Hello, World!"
print(b[2:9])           # print will be simbol "oll, Wo" 
print(b[:5])            # print will be simbol "Hello"
print(b[2:])            # print will be simbol "oll, World!"
"""
Минус обратный ход (с право на лево).
Первое значение включено, второе значение нет
"""
print(b[-5:-2])         # print will be simbol "orl"

c = "raspberry"
print(c[:2]+ " _ _ " +c[4:])     # print will be simbol "ra _ _ berry"

# Upper Case

d = "Hello, World!"
print(d.upper())  # print will be simbol "HELLO, WORLD!"

print(d.lower())  # print will be simbol "hello, world!"

"""
Метод Strip() удаляет 
все пробелы в начале и в конце:
"""
f = "  Hello, World!  "
print(f.strip())  # print will be simbol "Hello, World!"

# Example
"""
Метод заменяет символ.
Первый что нужно заменит,
Второй на что заменяется.
"""
g = "Hello, World!"
print(g.replace("H", "J"))    # print will be simbol "Jello, World!"

# String Concatenation
# Example
t = "Hello"
v = "World!"
u = t + v
print(u)

# Example
p = t + " " + v
print(p)

# Use the format()
# Example
age = 35
name = "Bonka"
# txt = "My name is " + name + ", I am " + age           - Type Error
txt = "My name is " + name + ", I am {}"
print(txt.format(age))

# Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} prices of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0}
myorder = "I want {2} prices of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))

