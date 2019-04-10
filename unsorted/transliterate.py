# -*- coding: utf-8 -*-



#from transliterate import translit, get_available_language_codes
import os
##import transliterate
##import translit
##import get_available_language_codes
#
file_path = os.path.expanduser("~/Desktop/WOF-Language/Regions/")
text = file_path + "russian.csv "
#
#print(translit(u"Ⴊორემ იფსუმ დოლორ სით ამეთ", reversed=True))







symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")

tr = {ord(a):ord(b) for a, b in zip(*symbols)}

# for Python 2.*:
# tr = dict( [ (ord(a), ord(b)) for (a, b) in zip(*symbols) ] )

#text = u'Добрый Ден'
x = text.translate(str(tr))  # looks good
print str(x)