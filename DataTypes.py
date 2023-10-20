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
Text Type:	        str
Numeric Types:	    int, float, complex
Sequence Types:	    list, tuple, range
Mapping Type:	    dict
Set Types:	        set, frozenset
Boolean Type:	    bool
Binary Types:	    bytes, bytearray, memoryview
None Type:	        NoneType
"""

x = 5
print(type(x))

a = "Hello"                                 #str
b = 20                                      #int
c = 20.5                                    #float
d = 1j                                      #complex
e = ["apple", "banana", "cherry"]           #list - список
f = ("berry", "blueberry", "raspberry")     #tuple - кортеж
g = range(6)                                #range - диапазон
i = {"name" : "Anna", "age" : 36}           #dict
j = {"berry", "banana", "blueberry"}        #set
k = frozenset({"apple", "cherry", "berry"}) #frozenset
l = True                                    #bool
m = b"Hello"                                #bytes
n = bytearray(5)                            #bytearray
o = memoryview(bytes(5))                    #memoryview
p = None                                    #NoneType

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(f))
print(type(g))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
print(type(o))
print(type(p))

print(". . . . . . . .")

aa = str("Hello")                                       #str
ba = int(20)                                            #int
ca = float(20.5)                                        #float
da = complex(1j)                                        #complex
ea = list(("apple", "banana", "cherry"))                #list - список
fa = tuple(("berry", "blueberry", "raspberry"))         #tuple - кортеж
ga = range(6)                                           #range - диапазон
ia = dict(name="Anna", age=36)                          #dict
ja = set(("berry", "banana", "blueberry"))              #set
ka = frozenset(("apple", "cherry", "berry"))            #frozenset
la = bool(5)                                               #bool
ma = bytes(5)                                           #bytes
na = bytearray(5)                                       #bytearray
oa = memoryview(bytes(5))                               #memoryview

print(type(aa))
print(type(ba))
print(type(ca))
print(type(da))
print(type(fa))
print(type(ga))
print(type(ia))
print(type(ja))
print(type(ka))
print(type(la))
print(type(ma))
print(type(na))
print(type(oa))
