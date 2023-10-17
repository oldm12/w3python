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

"""
int
float
complex
"""

x = 1   # int
y = 2.8 # float
z = 1j  # complex
print(type(x))
print(type(y))
print(type(z))

# int
a = 1                   # int
b = 1234567890987654    # int
c = -4567890            # int
print(type(a))
print(type(b))
print(type(c))

# float
d = 1.12        # float
e = 1.0         # float
f = -34.84      # float
print(type(d))
print(type(e))
print(type(f))

k = 35e3        # float
l = 12E4        # float
m = -94.4E100   # float
print(type(k))
print(type(l))
print(type(m))

# complex
o = 3 + 5j      # complex
p = 5j          # complex
q = -5j         # complex
print(type(o))
print(type(p))
print(type(q))

#convert from int to ...
t = 1       # int
v = 2.8     # float
u = 1j      # complex

#convert from int to float:
a = float(t)

#convert from int to int:
b = int(v)

#convert from int to complex:
c = complex(t)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number
import random
print(random.randrange(1, 10))

import random2
print(random2.randrange(1, 10))

