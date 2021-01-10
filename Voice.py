import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def cria_audio(audio):
	tts = gTTS(audio, lang='pt-br')
	tts.save('playback/Pb.mp3')
	print("Analisando Voz")
	playsound('playback/Pb.mp3')

def ouvir_microfone():

	microfone = sr.Recognizer()
	with sr.Microphone() as source:

		microfone.adjust_for_ambient_noise(source)
		print("Microfone Ativo")
		audio = microfone.listen(source)

	try:
		frase = microfone.recognize_google(audio, language='pt-BR')
		print("Frase: " + frase)
	except sr.UnkownValueError:
		print("Não entendi")

	return frase

frase = ouvir_microfone()

cria_audio(frase)