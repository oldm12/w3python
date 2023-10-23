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
print(color.PURPLE+"example 1" +color.END)
print(10 + 5)

"""
Arithmetic Operators:
+	Addition	        x + y	
-	Subtraction	        x - y	
*	Multiplication	    x * y	    Умножение
/	Division	        x / y	    деление
%	Modulus	            x % y	    Модуль
**	Exponentiation	    x ** y	    Возведение в степень
//	Floor division	    x // y      Этажное разделение
"""

# example2
print(color.PURPLE+"example 2 - Arithmetic Operators" +color.END)
x = 6
y = 3
a = x + y
b = x - y
c = x * y
d = x / y
e = x % y
f = x ** y
g = x // y

print("x = " + format(x) +", " + "y = " + format(y))
print("x + y = " + format(a))
print("x - y = " + format(b))
print("x * y = " + format(c))
print("x / y = " + format(d))
print("x % y = " + format(e))
print("x ** y = " + format(f))
print("x // y = " + format(g))


"""
Assignment Operators
"""
# example3 - Операторы присваивания для присвоения значений переменным:
print(color.PURPLE+"example 3 - Assignment Operators" +color.END)
print(color.BLUE + "x += 3, x = x + 3" + color.END)
x = 3
x += 3
print("x = 3, x += 3        => x = " + format(x))
y = 3
y = y + 3
print("y = 3, y = y + 3     => y = " + format(y))

print(color.BLUE + "x -= 3, x = x - 3" + color.END)
a = 5
a -= 3
print("a = 5, a -= 3        => a = " + format(a))
b = 5
b = b - 3
print("b = 5, b = b - 3     => a = " + format(b))

print(color.BLUE + "x *= 3, x = x * 3" + color.END)
x = 2
x *= 3	    
print("x = 2, x *= 3        => x = " + format(x))
x = 2
x = x * 3
print("x = 2, x = x * 3     => x = " + format(x))

print(color.BLUE + "x /= 3, x = x / 3" + color.END)
x = 9
x /= 3	    
print("x = 9, x *= 3        => x = " + format(x))
x = 9
x = x / 3
print("x = 9, x = x * 3     => x = " + format(x))

# x %= 3	    x = x % 3
print(color.BLUE + "x %= 3	    x = x % 3" + color.END)
x = 5
x %= 3	    
print("x = 5, x %= 3       => x = " + format(x))
x = 5
x = x % 3
print("x = 5, x = x % 3     => x = " + format(x))

#  x //= 3	    x = x // 3
print(color.BLUE + "x //= 3, x = x // 3" + color.END)
x = 5
x //= 3	    
print("x = 5, x //= 3       => x = " + format(x))
x = 5
x = x // 3
print("x = 5, x = x // 3     => x = " + format(x))


# x **= 3	    x = x ** 3	
print(color.BLUE + " x **= 3, x = x ** 3	" + color.END)
x = 5
x **= 3	    
print("x = 5, x **= 3      => x = " + format(x))
x = 5
x = x ** 3
print("x = 5, x = x ** 3     => x = " + format(x))

# x &= 3	    x = x & 3
print(color.BLUE + "x &= 3, x = x & 3 - что делает этот оператор?" + color.END)
x = 5
x &= 3	    
print("x = 5, x &= 3     => x = " + format(x))
x = 5
x = x & 3
print("x = 5, x = x & 3     => x = " + format(x))

# x |= 3	    x = x | 3
print(color.BLUE + "x |= 3, x = x | 3 - что делает этот оператор?" + color.END)
x = 5
x |= 3	    
print("x = 5, x |= 3     => x = " + format(x))
x = 5
x = x | 3
print("x = 5, x = x | 3     => x = " + format(x))


# x ^= 3	    x = x ^ 3
print(color.BLUE + "x ^= 3, x = x ^ 3 - что делает этот оператор?" + color.END)
x = 5
x ^= 3	    
print("x = 5, x ^= 3     => x = " + format(x))
x = 5
x = x ^ 3
print("x = 5, x = x ^ 3     => x = " + format(x))

# x >>= 3	    x = x >> 3	
print(color.BLUE + "x >>= 3, x = x >> 3 - что делает этот оператор?" + color.END)
x = 5
x >>= 3	    
print("x = 5, x >>= 3     => x = " + format(x))
x = 5
x = x >> 3
print("x = 5, x = x >> 3     => x = " + format(x))

# x <<= 3	    x = x << 3
print(color.BLUE + "x <<= 3, x = x << 3 - что делает этот оператор?" + color.END)
x = 5
x <<= 3	    
print("x = 5, x <<= 3     => x = " + format(x))
x = 5
x = x << 3
print("x = 5, x = x << 3     => x = " + format(x))


"""
Comparison Operators
Операторы сравнения используются для сравнения двух значений:
==	   Equal	                        x == y         Равный
!=	   Not equal	                  x != y         Не равный
>	   Greater than	               x > y	
<	   Less than	                  x < y	
>=	   Greater than or equal to	   x >= y         Больше или равно
<=	   Less than or equal to	      x <= y         Меньше или равно
"""

# example4
print(color.PURPLE+"example 4 - Comparison Operators" +color.END)
x = 4
y = 5

print(color.RED + "x = 4, y = 5, x == y" + color.END)
print(x == y)     # will be False

print(color.RED + "x = 4, y = 5, x != y" + color.END)
print(x != y)     # will be True

print(color.RED + "x = 4, y = 5, x > y" + color.END)
print(x > y)     # will be False

print(color.RED + "x = 4, y = 5, x < y" + color.END)
print(x < y)     # will be True

print(color.RED + "x = 4, y = 5, x >= y" + color.END)
print(x >= y)     # will be False

print(color.RED + "x = 4, y = 5, x <= y" + color.END)
print(x <= y)     # will be True


"""
Logical Operators
and 	   Returns True if both statements are true	                  x > 5 and  x < 10	
or	      Returns True if one of the statements is true	            x < 5 or x < 4	
not	   Reverse the result, returns False if the result is true	   not(x < 5 and x < 10)
"""
# example5
print(color.PURPLE+"example 5 - Logical Operators" +color.END)

x = 5
print(color.RED + "x = 5, x > 3 and  x < 10" + color.END)
print(x > 3 and  x < 10)     # will be returns True

print(color.RED + "x = 5, x > 3 or x < 4" + color.END)
print(x > 3 or x < 4)
# returns True because one of the conditions are true 
# (5 is greater than 3, but 5 is not less than 4)

print(color.RED + "x = 5, not(x > 3 and x < 10)" + color.END)
print(not(x > 3 and x < 10))

print(color.RED + "x = 5, x > 3 and x < 10" + color.END)
print(x > 3 and x < 10)

# example6 - Identity Operators
print(color.PURPLE+"example 6 - Identity Operators" +color.END)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("x = " + format(x) + "\ny = " + format(y) + "\nz = x, \nx is z?")
print(x is z)
# returns True because z is the same object as x

print("x = " + format(x) + "\ny = " + format(y) + "\nz = x, \nx is not z?")
print(x is not z)
# returns False because z is the same object as x


print("x = " + format(x) + "\ny = " + format(y) + "\nz = x, \nx is y?")
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
# возвращает False, потому что x не является тем же объектом, что и y, 
# даже если они имеют одинаковое содержимое

print("x = " + format(x) + "\ny = " + format(y) + "\nz = x, \nx is not y?")
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content


print("x = " + format(x) + "\ny = " + format(y) + "\nz = x, \nx == y?")
print(x == y)
# to demonstrate the difference betweeen "is" and "==": 
# this comparison returns True because x is equal to y

print("x = " + format(x) + "\ny = " + format(y) + "\nz = x, \nx != y?")
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": 
# this comparison returns False because x is equal to y


# example7 - Membership Operators - проверка наличия файла в объекте
print(color.PURPLE+"example 7 - Membership Operators" +color.END)

x = ["apple", "banana"]
print("x = " + format(x) + "\n'banana' in x?")
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

print("x = " + format(x) + "\n'pineapple' not in x?")
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

# Bitwise Operators - сравнения (двоичных) чисел
"""
& 	      AND	      Sets each bit to 1 if both bits are 1	               x & y	
|	      OR	         Sets each bit to 1 if one of two bits is 1	         x | y	
^	      XOR	      Sets each bit to 1 if only one of two bits is 1	      x ^ y	
~	      NOT	      Inverts all the bits	                                 ~x	
<<	      Zero fill left shift	   Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	      Signed right shift	   Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""

# example8 - Operator Precedence - Круглые скобки имеют наивысший приоритет
print(color.PURPLE+"example8 - Operator Precedence - Круглые скобки имеют наивысший приоритет" +color.END)
print((6 + 4) - (6 + 3))
print(color.BLUE + "Умножение * имеет более высокий приоритет, чем сложение +" + color.END)
print(2 + 5 * 3)

# Порядок приоритета описан в таблице ниже, начиная с самого высокого приоритета вверху:
print(color.BLUE + "Порядок приоритета описан в таблице ниже, начиная с самого высокого приоритета вверху:" + color.END)
"""
()	                  Parentheses	
**	                  Exponentiation	
+x  -x  ~x	         Unary plus, unary minus, and bitwise NOT	
*  /  //  %	         Multiplication, division, floor division, and modulus	
+  -	               Addition and subtraction	
<<  >>	            Bitwise left and right shifts	
&	                  Bitwise AND	
^	                  Bitwise XOR	
|	                  Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	               Logical NOT	
and	               AND	
or	                  OR
"""
print(5 + 4 - 7 + 3)
