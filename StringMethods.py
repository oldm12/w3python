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
print(color.BOLD, color.GREEN+"Python String Methods start" +color.END)

# capitalize() - Преобразует первый символ в верхний регистр
upperCase = "hello, world!"
print("Original: " + upperCase)
print(upperCase.capitalize())
x = upperCase.capitalize()
print(x)

# casefold() - Преобразует строку в нижний регистр
lowerCase = "Hello, World!"
print("Original: " + lowerCase)
print(lowerCase.casefold())
y = lowerCase.casefold()
print(y)

# center() - Возвращает центрированную строку
centeredString = "Hello, World!"
print("Original: " + centeredString)
print(centeredString.center(30))        # Значення у дужках обои'язкове
z = centeredString.center(20)
print(z)


# count() - Возвращает количество раз, сколько свтретилось значение в строке
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# string.count(value, start, end)
text = "I love raspberrys, berry, blueberry, berry are my favorite fruit"
y = text.count("berry", 10, 25)
print(y)
x = text.count("berry")
print(x)


# encode() - Возвращает закодированную версию строки
# If no encoding is specified, UTF-8 will be used
txt = "My name is Ståle"
x = txt.encode()
print(x)

# string.encode(encoding=encoding, errors=errors)
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# endswith() - Возвращает true, если строка заканчивается указанным значением
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(txt.endswith("d"))
print(x)

# string.endswith(value, start, end)
txt = "Hello, welcome to my world."
a = txt.endswith("my world.")
b = txt.endswith("my world.", 5, 11)
print(a)
print(b)

# expandtabs() - Устанавливает размер табуляции строки
# string.expandtabs(tabsize)  - Размер табуляции по умолчанию – 8.
tubText = "H\te\tl\tl\to"
tubPr = tubText.expandtabs(3)
print(tubPr)
print(tubText)
print(tubText.expandtabs())
print(tubText.expandtabs(2))
print(tubText.expandtabs(4))
print(tubText.expandtabs(10))

# find() - Ищет в строке указанное значение и возвращает позицию, где оно было найдено.
# string.find(value, start, end)
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
y = txt.find("e")       # первое встречание в тексте
print(y)
z = txt.find("e", 5, 10)
print(z)

print(txt.find("q"))    # Если значение не найдено, метод find() возвращает -1
# print(txt.index("q"))   # Mетод index() вызовет ValueError: substring not found

# format() - Форматирует указанные значения в строку
# string.format(value1, value2...)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}"
txt2 = "My name is {0}, I'm {1}"
txt3 = "My name is {}, I'm {}"
print(txt1.format(fname = "John", age = 36))
print(txt2.format("John",36))
print(txt3.format("John",36))

# print(g.replace("H", "J"))    # print will be simbol "Jello, World!"


