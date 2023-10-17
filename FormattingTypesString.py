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

# 1. {:<..}  - Выравнивает результат по левому краю (в пределах доступного пространства)
txt = "We have {:<4} chickens."
print(txt.format(49))

# 2. {:>..} - По правому краю выравнивает результат (в пределах доступного пространства)
txt = "We have {:>15} chickens."
print(txt.format(49))

# 3. {:^..} - По центру выравнивает результат (в пределах доступного пространства)
txt = "We have {:^5} chickens."
print(txt.format(49))

# 4. {:=..} - Размещает знак в крайнем левом положении.
txt = "We have {:=10} chickens."
print(txt.format(49))

# 5. {:+..} - Добовляет знак плюс при выводе положительного числа.
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

# 6. {:-} - Выводит положительное число без знака плюс
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))