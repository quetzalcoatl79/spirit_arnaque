import speech_recognition as sr
from hugchat import hugchat
from hugchat.login import Login
from elevenlabs import voices, generate
from elevenlabs import generate, play
from gtts import gTTS
from playsound import playsound
from Key_liste import user, password

"""
####################################
Partie écoute 
####################################
"""
# Créez un objet Recognizer
recognizer = sr.Recognizer()

# Ouvrez le microphone comme source audio
with sr.Microphone() as source:
    print("Parlez maintenant. Je vous écoute...")
    try:
        # Écoutez l'audio du microphone en temps réel et transcrivez-le en texte
        audio_data = recognizer.listen(source)
        text = recognizer.recognize_google(audio_data, language="fr-FR")
        print("Texte transcrit : " + text)
    except sr.UnknownValueError:
        print("Impossible de reconnaître la parole")
    except sr.RequestError as e:
        print("Erreur lors de la demande de reconnaissance vocale ; {0}".format(e))

prompt = f"tu est un fantôme ! Fais une reponse très courte de trois à cinq mots, en francais, en me tuttoyant et choisi \
    les reponse par toi même soit cohérent avec la question: < {text} >"


"""
####################################
Partie IA
####################################
"""

# Log in to huggingface and grant authorization to huggingchat
sign = Login(user, password)
cookies = sign.login()

# Save cookies to the local directory
cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

# non stream response
query_result = chatbot.query(prompt)
print(query_result) # or query_result.text or query_result["text"]


"""
####################################
partie reponse
####################################
"""
filename = 'mot_aléatoire.mp3'
tts = gTTS(text=f"{query_result}",lang='fr', tld='fr')
tts.save(filename)
playsound(filename)
