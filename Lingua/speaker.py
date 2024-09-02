from win32com.client import Dispatch

# With the Speech API and the Windows engine Dispatch, the speack method gives the audio version of the passed text
def speak(text):
    speaker = Dispatch("SAPI.SpVoice") #Id del objeto del sintetizador
    speaker.Speak(text)

