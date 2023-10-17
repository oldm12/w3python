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

import random2

c = "raspberry"
print(c[:2]+ " _ _ " +c[4:])     # print will be simbol "ra _ _ berry"
print(c[:0]+ " _ _ " +c[2:])     # print will be simbol "ra _ _ berry"



print(color.BOLD, color.GREEN+"Метод с плавающим пробілом у дві літери" +color.END)
lenWord = len(c)
one = random2.randrange(0, lenWord - 2)
text = "Виводить до якого символу образало: " + str(one)
print(text)
print(c[:one]+ " _ _ " +c[one + 2:])     # print will be simbol "ra _ _ berry"
