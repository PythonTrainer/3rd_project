from transliterate import get_available_language_codes, translit
from num2words import num2words
from gtts import gTTS
import os

text = '''
Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes 
of fame once in a lifetime and I guess that this is mine. 
People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. 
Neither will happen. More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic 
Storage for last 40. When I was 8...
'''

tts = gTTS(text=text, lang='en')
tts.save('text.mp3')
os.system('text.mp3')
translit(text, 'ru')
[num2words(i) for i in [42, 51, 44]]
nums = [(sym, num2words(sym)) for sym in text.replace('.', ' ').split() if sym.isdigit()]
for num, value in nums:
    print(f"{num} - {translit(value, 'ru')}")
