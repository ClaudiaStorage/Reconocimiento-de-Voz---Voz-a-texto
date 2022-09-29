import speech_recognition as sr
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Di algo por favor")
        audio = r.listen(source)
        print("Reconociendo .... ")
 
        # recognize speech using google
        try:
            print("Has dicho \n" + r.recognize_google(audio, language='es-ES'))
            print("Audio grabado exitosamente \n ")
 
        except Exception as e:
            print("Error :  " + str(e))
 
        # write audio
 
        with open("prueba3.wav", "wb") as f:
            f.write(audio.get_wav_data())
 
if __name__ == "__main__":
    main()
