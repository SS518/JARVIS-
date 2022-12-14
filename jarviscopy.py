
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import requests
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

#import numbers.py 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#To convert voice into text
def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good morning, it's {tt}")
    elif hour >= 12 and hour <= 16:
        speak(f"Good afternoon, it's {tt}")
    else:
        speak(f"Good evening, it's {tt}")
    speak("Jarvis here. please tell how may I help you?")

""""    
#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ADDRESS', 'YOUR PASSWORD')
    server.sendmail('YOUR EMAIL ADDRESS', to, content)
    server.close()
"""
 
 

#for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="YOUR_API_HERE"'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")



if __name__ == "__main__": #main program
#def TaskExceution():
    wish()
    while True:
    # if 1:

        query = takecommand().lower()

#opening softwares

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            
        elif 'hi' in query or 'hello' in query:
            speak('Hello, how may I help you?')
        
        elif "open fl studio" in query:
            apath = "D:\\SHRESTH\\music\\FL STUDIO 20.8.3.2034\\FL.exe"
            os.startfile(apath)

        elif "edit" in query or "open filmora" in query:
            epath = "C:\\Program Files\Wondershare\\Filmora9\\Wondershare Filmora9.exe"
            os.startfile(epath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "open chrome" in query:
            cpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)

        elif "open game" in query:
            gpath = "D:\\SHRESTH\\GAMES\\JW\\Jurassic World Evolution\\JWE.exe"
            os.startfile(gpath)

            

    #    elif "where am i" in query or "where are we" in query:
    #        speak("wait ,let me check")
    #        try:
    #           ip = requests.get('https://api.ipify.org').text
    #           url = 'https://get.geojs.io/v1/ip'+ip+'.jason'
    #           geo_requests = requests.get(url)
    #           geo_data = geo_requests.jason()
    #           city = geo_data('city')
    #           country = geo_data('country')
    #           speak(f"Maybe we are in{city} of {country}")
    #        except Exception as e:
    #            speak("sorry I'm unable to get your ip")
    #            pass

        elif "wikipedia" in query or "about" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")
                                                                                                        
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

     #   elif "chats on instagram" in query or "messages on instagram":
      #      webbrowser.open("https://www.instagram.com/direct/inbox")            

        elif "open google" in query or "search" in query:
            speak("What should I search?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

      #  elif "send whatsapp message" in query:
      #     speak("To whom do you want to message ?")
      #     # pname = takecommand().lower()
      #    # kit.sendwhatmsg(f"{pname}", "this is testing protocol",4,13)
      #      kit.sendwhatmsg("+918400444054", "this is testing protocol",4,13)
      #      time.sleep(120)
      #      speak("message has been sent")

        elif "song" in query:
            speak("which song should I play ?")
            psong = takecommand().lower()
            kit.playonyt(psong)

        elif "search on youtube" in query:
            speak("What should I search?")
            pvideo = takecommand().lower()
            kit.playonyt(pvideo)
            
        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing =timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')

            time.sleep(timing)
            speak('Your time has been finished')
        
        elif "email to hex" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "shresthdps@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry,I am unable to send this mail to hex")
                
              

        elif "no thanks" in query or "stop" in query :
            speak("okay,please call me when needed.")
            print("JARVIS has left")
            sys.exit()

        elif "jarvis sleep" in query :
            speak("okay,pls call me when needed.")
            break        
            


#to close any application
        elif "close notepad" in query:
            speak("okay, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close fl studio" in query:
            speak("okay, closing flstudio")
            os.system("taskkill /f /im FL.exe")

        elif "close chrome" in query:
            speak("okay, closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif "close filmora" in query or "close edit" in query:
            speak("okay, closing filmora")
            os.system("taskkill /f /im Wondershare Filmora9.exe")

        elif "close game" in query:
            speak("okay, closing Jurrasic world evolution")
            os.system("taskkill /f /im JWE.exe")
           



#to set an alarm (currently for 10PM)
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            atime = takecommand().lower()
            if nn==atime: 
                music_dir = '"D:\\SHRESTH\\JARVIS\\ALARM SOUND.mp3"'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))


#to find a joke
        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

#system on or off
        elif "shut down" in query or "shutdown" in query:
            os.system("shutdown /s /t 5")

        elif "restart" in query:
            os.system("shutdown /r /t 5")

        elif "sleep" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


#switch window
        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
                   
#news
        elif "news" in query:
            speak("Please wait , feteching the latest news")
            news()


#taking screeshot 
        elif "screenshot" in query:
         speak("what should be the name of the ss?")
         ssname = takecommand().lower()
         speak("Please wait,I am taking the screenshot")
         time.sleep(2)
         img = pyautogui.screenshot()
         img.save(f"{ssname}.png")
         speak("I've taken the screenshot, you can view it in the code  Now please give me your next command")


#wishings part
        elif 'thank you' in query or 'thanx' in query:
            speak('My pleasure,please let me know how may I help you further')


        elif 'how are you' in query:
            speak('I am fine sir,what about you?')

        elif 'good' in query or 'fine' in query:
            speak('Glad to know!')

        elif 'good' in query or 'fine' in query:
            speak('Glad to know!')            

     

#if __name__ == "__main__":
#    while True:
#        permission = takecommand()
#        if "wake up" in permission:
#            TaskExceution()
#        elif "goodbye" in permission:
#            speak("Thanx for usimg me")
 #           sys.exit()    










































#        elif "calculate" in query or "calculation" in query or "calculations" in query:
#            speak("what do you want to calculate?")
#            cal = takecommand().lower()
#            print(cal)
#            def get_operator_fn(op):
#                return {
#                    '+' : operator.add,
#                    '-' : operator.sub,
#                    'x' : operator.mul,
#                    'divide' : operator._truediv_,
#                    }[op]
#            def eval_binary_expr(op1, oper, op2):
#                op1,op2 = int(op1),int(op2)
#                return get_operator_fn(oper)(op1,op2)
#            speak("Your result is ")
#             speak(eval_binary_expr(*(cal.split())))



 #       elif "Thank you" in query:
 #           speak("My pleasure,please let me know how may I help you further")


"""
        elif "email to hex" in query:
               
            speak("What should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'shresthdps@gmail.com' # Your email
                password = 'mJ12Q@p4OAj9wmE' # Your email account password
                send_to_email = 'shresthmusic123@gmail.com' # Whom you are sending the message to
                speak("okay, what is the subject for this email")
                query = takecommand().lower()
                subject = query   # The Subject in the email
                speak("and , what is the message for this email")
                query2 = takecommand().lower()
                message = query2  # The message in the email
                speak("Please enter the correct path of the file into the shell")
                file_location = input("please enter the path here")    # The File attachment in the email

                speak("please wait,i am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                # Setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                # Attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent")

            else:                
                email = 'shresthdps@gmail.com' # Your email
                password = 'mJ12Q@p4OAj9wmE' # Your email account password
                send_to_email = 'shresthmusic123@gmail.com' # Whom you are sending the message to
                message = query # The message in the email

                server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
                server.starttls() # Use TLS
                server.login(email, password) # Login to the email server
                server.sendmail(email, send_to_email , message) # Send the email
                server.quit() # Logout of the email server
                speak("email has been sent")
            
"""
        # speak("Do you have any other work for me?")