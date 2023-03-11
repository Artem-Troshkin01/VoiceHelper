import random
import sys
import webbrowser

import pyttsx3
import requests
import speech_recognition


class VoiceHelper:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.microphone = speech_recognition.Microphone()

        self.voice = pyttsx3.init()
        self.voice.say('Здравствуйте, я голосовой помощник')
        self.voice.runAndWait()

    def _films_parser(self):
        # TODO: Реализовать парсер фильмов
        pass

    def _send_voice_message(self, message: str) -> None:
        # TODO: реализовать озвучивание сообщения голосом
        pass

    def _open_youtube(self):
        # TODO: реализовать открытие youtube
        pass

    def _recognition_of_key_commands(self):
        # TODO: обработка ключевых команд
        pass

    def _record_and_recognize_audio(self):
        # TODO: запись и воспроизведение аудио
        pass


if __name__ == '__main__':
    helper = VoiceHelper()
