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
print("capitalize() - Преобразует первый символ в верхний регистр")
upperCase = "hello, world!"
print(color.BLUE + "Original: " + upperCase + color.END)
print(upperCase.capitalize())
x = upperCase.capitalize()
print(x)

# casefold() - Преобразует строку в нижний регистр
lowerCase = "Hello, World!"
print(color.BLUE + "Original: " + lowerCase + color.END)
print(lowerCase.casefold())
y = lowerCase.casefold()
print(y)

# center() - Возвращает центрированную строку
centeredString = "Hello, World!"
print(color.BLUE + "Original: " + centeredString + color.END)
print(centeredString.center(30))        # Значення у дужках обои'язкове
z = centeredString.center(20)
print(z)


# count() - Возвращает количество раз, сколько свтретилось значение в строке
txt = "I love apples, apple are my favorite fruit."
x = txt.count("apple")
print(color.BLUE + "Original: " + txt + color.END)
print(color.RED + "Find: apple" + color.END)
print(x)

# string.count(value, start, end)
text = "I love raspberrys, berry, blueberry, berry are my favorite fruit."
y = text.count("berry", 10, 25)
print(color.BLUE + "Original: " + text + color.END)
print(color.RED + "Find: 'berry' пошук з 10 до 25 символа" + color.END)
print(y)
x = text.count("berry")
print(color.RED + "Find: 'berry' весь текст" + color.END)
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
# string.endswith(value, start, end)
print(color.GREEN + "endswith() - Возвращает true, если строка заканчивается указанным значением" + color.END)
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(color.BLUE + "Original: " + txt + color.END)
print(color.RED + "Find: '.'" + color.END)
print(x)
print(color.RED + "Find: 'd'" + color.END)
print(txt.endswith("d"))
print(color.GREEN + "string.endswith(value, start, end)" + color.END)
a = txt.endswith("my world.")
b = txt.endswith("my world.", 5, 11)
print(color.RED + "Find: 'my world.' весь текст" + color.END)
print(a)
print(color.RED + "Find: 'my world.' пошук з 5 до 11 символа" + color.END)
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

# ?format_map() - Форматирует указанные значения в строке

# String index() Method
# string.index(value, start, end)
txt = "Hello, welcome to my world."
x = txt.index("welcome")   # will be welcome "w" -> 7
print(x)
y = txt.index("e")         # will be "e" -> 1
print(y)                   
z = txt.index("e", 5, 10)  # will be "e" -> 8
print(z)       
# print(txt.index("q"))      # will be "q" -> # Mетод index() вызовет ValueError: substring not found

# String isalnum() Method - Возвращает True, если все символы в строке являются буквенно-цифровыми.
ab = "Company12"
x = ab.isalnum()
print(x)

# String isalpha() Method - Возвращает значение True, если все символы строки алфавит.
abc = "CompanyX"
x = abc.isalpha()
print(x)

# String isascii() Method 
# Возвращает значение True, если все символы 
# в строке являются символами ascii.
# ASCII был первым набором символов (стандартом кодирования), который использовался между компьютерами в Интернете.
print("String isascii() Method Возвращает значение True, если все символы в строке являются символами ascii")
abab = "Company12"
StIs = abab.isascii()
print(abab)
print(StIs)

# String isdecimal() Method - Возвращает True, если все символы в строке являются циврами десятичными int.
print("String isdecimal() Method - Возвращает True, если все символы в строке являются циврами int")
example = "1234"
x = example.isdecimal()
print(color.BLUE + "Original: " + example.format() + color.END)
print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a)
print(a.isdecimal())
print(b)
print(b.isdecimal())

# String isdigit() Method - Возвращает True, если все символы в строке — цифры.
print(color.GREEN + "String isdigit() Method - Возвращает True, если все символы в строке — цифры." + color.END)
exampleG = "50800"
x = exampleG.isdigit()
print(color.BLUE + "Original: " + exampleG.format() + color.END)
print(x)
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "3.14"
print(color.BLUE + "Original: " + a.format() + color.END)
print(a.isdigit())
print(color.BLUE + "Original: " + b.format() + color.END)
print(b.isdigit())
print(color.BLUE + "Original: " + c.format() + color.END)
print(c.isdigit())

# String isidentifier() Method - озвращает True, если строка является идентификатором
print(color.GREEN + "String isidentifier() Method - озвращает True, если строка является идентификатором" + color.END)
txt = "Demo"
x = txt.isidentifier()
print(color.BLUE + "Original: " + txt + color.END)
print(x)

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
e = "1234"

print(color.BLUE + "Original: " + a + color.END)
print(a.isidentifier())
print(color.BLUE + "Original: " + b + color.END)
print(b.isidentifier())
print(color.BLUE + "Original: " + c + color.END)
print(c.isidentifier())
print(color.BLUE + "Original: " + d + color.END)
print(d.isidentifier())
print(color.BLUE + "Original: " + e + color.END)
print(e.isidentifier())

# String islower() Method - Возвращает значение True, если все символы в строке написаны строчными буквами.
print(color.GREEN + "String islower() Method - Возвращает значение True, если все символы в строке написаны строчными буквами." + color.END)
txt = "hello world!"
print(color.BLUE + "Original: " + txt + color.END)
x = txt.islower()
print(x)

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(color.BLUE + "Original: " + a + color.END)
print(a.islower())
print(color.BLUE + "Original: " + b + color.END)
print(b.islower())
print(color.BLUE + "Original: " + c + color.END)
print(c.islower())

# String isnumeric() Method - Возвращает True, если все символы в строке числовые.
print(color.GREEN + "String isnumeric() Method - Возвращает True, если все символы в строке числовые." + color.END)
txt = "565543"
print(color.BLUE + "Original: " + txt + color.END)
x = txt.isnumeric()
print(x)

a = "\u0030" #unicode for 0 - will be True
b = "\u00B2" #unicode for &sup2; - will be True
c = "10km2"       # will be False
d = "-1"          # will be False
e = "1.5"         # will be False

print(color.BLUE + "Original: " + a + color.END)
print(a.isnumeric())
print(color.BLUE + "Original: " + b + color.END)
print(b.isnumeric())
print(color.BLUE + "Original: " + c + color.END)
print(c.isnumeric())
print(color.BLUE + "Original: " + d + color.END)
print(d.isnumeric())
print(color.BLUE + "Original: " + e + color.END)
print(e.isnumeric())

# String isprintable() Method - Возвращает значение True, если все символы строки можно распечатать.
print(color.GREEN + "String isprintable() Method - Возвращает значение True, если все символы строки можно распечатать." + color.END)
txt = "Hello! Are you #1?"
print(color.BLUE + "Original: " + txt + color.END)
x = txt.isprintable()
print(x)

a = "Hello!\nAre you #1?"
b = "Hello!\tAre you #1?"
print(color.BLUE + "Original: " + a + color.END)
y = a.isprintable()
print(a.isprintable())
print(color.BLUE + "Original: " + b + color.END)
print(b.isprintable())

# String isspace() Method - Возвращает True, если все символы в строке являются пробелами.
print(color.GREEN + "String isspace() Method - Возвращает True, если все символы в строке являются пробелами." + color.END)
txt = "   "
print(color.BLUE + "Original: " + txt + color.END)
x = txt.isspace()
print(x)

a = "   s   "
print(color.BLUE + "Original: " + a + color.END)
print(a.isspace())

# String istitle() Method - Возвращает True, если строка соответствует правилам заголовка.
print(color.GREEN + "String istitle() Method - Возвращает True, если строка соответствует правилам заголовка." + color.END)
txt = "Hello, And Welcome To My World!"
print(color.BLUE + "Original: " + txt + color.END)
x = txt.istitle()
print(x)

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(color.BLUE + "Original: " + a + color.END)
print(a.istitle())
print(color.BLUE + "Original: " + b + color.END)
print(b.istitle())
print(color.BLUE + "Original: " + c + color.END)
print(c.istitle())
print(color.BLUE + "Original: " + d + color.END)
print(d.istitle())

# String isupper() Method - Возвращает значение True, если все символы в строке имеют верхний регистр.
print(color.GREEN + "String isupper() Method - Возвращает значение True, если все символы в строке имеют верхний регистр." + color.END)
txt = "THIS IS NOW!"
print(color.BLUE + "Original: " + txt + color.END)
x = txt.isupper()
print(x)

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(color.BLUE + "Original: " + a + color.END)
print(a.isupper())
print(color.BLUE + "Original: " + b + color.END)
print(b.isupper())
print(color.BLUE + "Original: " + c + color.END)
print(c.isupper())



# print(g.replace("H", "J"))    # print will be simbol "Jello, World!"


