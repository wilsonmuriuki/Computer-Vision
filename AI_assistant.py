import speech_recognition as sr
import pyaudio
import pyttsx3
import wikipedia
import pywhatkit
import datetime

#dictionary
phone_numbers={"ravi":"0791528199",
              "ken":"0791828129",
              "john":"0791808199",
              "joy":"0791828699",
              "james":"0711828199",
              "juma":"0791828199"}

bank_account_numbers={"wilson":"318389791528199",
              "mm":"318389791528199"
              }

engine=pyttsx3.init()
r=sr.Recognizer()

def speak(command):
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone()as source:
            r.adjust_for_ambient_noise(source)
            print('Listening...Ask now...')
            audioin=r.listen(source)
            my_text=r.recognize_google(audioin)
            my_text=my_text.lower()
            print(my_text)

            #recognize a couple of 6 things
            #ask to play song
            if 'play' in my_text:
                my_text=my_text.replace('play','')
                speak('playing'+my_text)
                pywhatkit.playonyt(my_text)
            #ask date
            elif 'date' in my_text:
                today=datetime.date.today()
                speak(today)
            #ask time
            elif 'time' in my_text:
                now=datetime.datetime.now().strftime('%H:%M')
                speak(now)
            #ask details about person
            elif "who is" in my_text:
                person=my_text.replace('who is','')
                info=wikipedia.summary(person,1)
                speak(info)
            #ask phone numbers
            elif "phone number" in my_text:
                names=list(phone_numbers)
                for name in names:
                    if name in my_text:
                        print(name + " phone number is " +phone_numbers[name])
                        speak(name + " phone number is " +phone_numbers[name])

            #ask personal back account numbers
            elif "account number" in my_text:
                account_numbers=list(bank_account_numbers)
                for x in account_numbers:
                    if x in my_text:
                        print(x + " account number is " +bank_account_numbers[x])
                        speak(x + " account number is " +bank_account_numbers[x])

            #if not recognized
            else:
                speak("I do not understand")


    except:
        print('Error handling Microphone...')

commands()

    