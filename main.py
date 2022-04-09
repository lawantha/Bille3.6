
import speech_recognition as sr


listener = sr.Recognizer()

print('one')
with sr.Microphone() as source:
    print('2')
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
try:
    print(command)
except:
    pass
    print('passed')