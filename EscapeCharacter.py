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
print(color.BOLD, color.GREEN+"Python Escape Characters start" +color.END)


# Escape Characters
# Example
# txt = "We are the so-called "Vikings" from the north." - Type Error
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Escape Characters
# \'	    Single Quote	   Одинарная цитата
# \\	    Backslash	      обратная косая черта
# \n	    New Line	      Новая строка
# \r	    Carriage Return	  Обрізало текст, що попереду \r
# \t	    Tab	              Всавить табуляція після \t
# \b	    Backspace	
# \f	    Form Feed	      Подача формы
# Не розібралась у цих:
# \ooo	    Octal value	      Восьмеричное значение
# \xhh	    Hex value         Шестнадцатеричное значение


txt = "We are the so-called \'Vikings\' from the north."
print(txt)

txt = "We are the so-called \\Vikings\\ from the north."
print(txt)

# Перехід на нову строку після \n
txt = "We are the so-called Vikings \n from the north."
print(txt)

# Обрізало текст, що попереду \r та надрукувала що після.
txt = "We are the so-called \r Vikings from the north."
print(txt)

# Всавить табуляція після \t
txt = "We are the so-called \t Vikings from the north."
print(txt)

# Видалить один пробіл перед \b
txt = "We are the so-called \bVikings from the north."
print(txt)

# Вставило символ ♀ на місці \f
txt = "We are the so-called \f Vikings from the north."
print(txt)
