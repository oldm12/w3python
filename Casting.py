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
print(color.BOLD, color.GREEN+"Python Casting start" +color.END)

"""
Casting
int() 
float()
str()
"""
# Integers:
x = int(1)          # x will be 1
y = int(2.8)        # y will be 2
z = int("3")        # z will be 3
print(x)
print(y)
print(z)

# Floats:
a = float(1)          # a will be 1.0
b = float(2.8)        # b will be 2.8
c = float("3")        # c will be 3.0
d = float("4.2")      # d will be 4.2
print(a)
print(b)
print(c)
print(d)

# Strings:
e = str("s1")       # e will be "s1"
f = str(2)          # f will be "2"
g = str(3.0)        # g will be "3.0"
print(e)
print(f)
print(g)

