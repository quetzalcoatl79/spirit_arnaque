# python3 -m venv env 
# pip install playsound
# pip install gTTS

import random
from data import data_dictionnary as DICT
from gtts import gTTS
from playsound import playsound

mot_aleatoire = random.choice(DICT)

print(mot_aleatoire)

filename = 'mot_aléatoire.mp3'
tts = gTTS(text=f"{mot_aleatoire}",lang='fr', tld='fr')
tts.save(filename)
playsound(filename)