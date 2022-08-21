import speech_recognition as sr

FILE = 'audio.wav'


def audio_to_text(file):
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)
    try:
        print(r.recognize_google(audio, language='ru-RU'))
    except sr.UnknownValueError:
        print('Гугл не понял')
    except sr.RequestError as e:
        print('Тут мне не понятно', e)


if __name__ == '__main__':
    audio_to_text(FILE)
