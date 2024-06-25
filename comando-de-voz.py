#Criando um sistema simples com função de comando de voz. BOOTCAMP DIO

print('testando')

#estamos importando o modulo speech_recognition da biblioteca SpeechRecognition para o sistema conseguir captar nossa voz
import speech_recognition as sr

#estamos importando o modulo os que nos permitirá usar funcionalidades do windows de forma simples
import os

#função para ouvir e reconhecer sua fala
def ouvir_microfone():
    #habilita e reconhece o microfone do usuário
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:

        #chama um algoritimo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        #frase para avisar o usuario que ele tem que dizer algo
        print('Diga Algo.')

        #armazena o que foi dito em uma variável
        audio = microfone.listen(source)

    try:

        #passa a variavel de audio para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language = 'pt-BR')

        if 'navegador' in frase:
            os.system('start Chrome.exe')
            return False
        elif 'Excel' in frase:
            os.system('start Excel.exe')
            return False
        elif 'PowerPoint' in frase:
            os.system('start POWERPNT.exe')
            return False
        elif 'edge' in frase:
            os.system('start msedge.exe')
            return False
        elif 'fechar' in frase:
            os.system('exit')
            return True
        
        #retorna a frase pronunciada
        print('Voce disse: ' +frase)

    #se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        print('Não Entendi, desculpe')

    return frase

while True:
    if ouvir_microfone():
        break