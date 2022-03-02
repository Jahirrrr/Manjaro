# MANJARO Virtual Assistant Project
# OpenSource Project
# MIT License

import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import sys
import urllib
import requests
import brainlypy
import smtplib
import wolframalpha
from email.message import EmailMessage
from translate import Translator


recognizer = sr.Recognizer()
recognizer.non_speaking_duration = 0.8
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
Mic = sr.Microphone()

WIN_MESSAGE = "Congratulations, you won!"
LOSE_MESSAGE = "nice try sir, you have lose"
DRAW_MESSAGE = "Oh no, it's a draw."


app_id = 'your_wolframalpha_app_id'


nohp_list = {
'your_friend_name': '+0000000000',
'your_friend_name': '+0000000000',
'your_friend_name': '+0000000000'
}


friend_mail_list = {
'your_friend_name': 'your_friend_name@gmail.com',
'your_friend_name': 'your_friend_name@gmail.com',
'your_friend_name': 'your_friend_name@gmail.com'
}


def manjaro_talk(text):
    engine.say(text)
    engine.runAndWait()


def im_talk():
    try:
        with Mic as source:
            print('Manjaro Listening.......')
            recognizer.adjust_for_ambient_noise(source)
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice, language='en-id')
            command = command.lower()
            if 'manjaro' in command:
                command = command.replace('manjaro', '')
                print(command)
    except:
     pass
    return command




def mail(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_mail@gmail.com', 'your_password')
    email = EmailMessage()
    email['From'] = 'your_mail@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


def random_choice(options=["rock", "paper", "scissors"]):
    return random.choice(options)

def determine_winner(choice1, choice2):
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }

    winner = winners[choice1][choice2]

    return winner

def RockScissorsGame():
    print("-------------------")
    print("Running The RockScissors Game...")
    print("-------------------")
    options = ["rock", "paper", "scissors"]
    print("Please choose either 'rock', 'paper', or 'scissors'")
    manjaro_talk("Please choose either 'rock', 'paper', or 'scissors'")
    user_choice = im_talk()
    if 'rock' in user_choice or 'paper' in user_choice or 'scissors' in user_choice:
        print("You choose :" + user_choice)
        manjaro_talk("You choose :" + user_choice)
    else:
        print("You choose :" + user_choice)
        manjaro_talk("Expecting one of: 'rock', 'paper', or 'scissors' (lower case, without the quotation marks). Please try again.")
        exit()

    manjaro_choice = random_choice(options)
    manjaro_talk("manjaro chose:" + manjaro_choice)
    print("manjaro choose:" + manjaro_choice)
    print("-------------------")

    winning_choice = determine_winner(user_choice, manjaro_choice)

    if winning_choice:
        if winning_choice == user_choice:
            print(WIN_MESSAGE)
            manjaro_talk(WIN_MESSAGE)
        elif winning_choice == manjaro_choice:
            print(LOSE_MESSAGE)
            manjaro_talk(LOSE_MESSAGE)
    else:
        print(DRAW_MESSAGE)
        manjaro_talk(DRAW_MESSAGE)

    print("Thanks for playing the game. Please play again!")
    manjaro_talk("Thanks for playing the game. Please play again!")



while True:
    manjaro_command = im_talk()
    print(manjaro_command)
    if 'play on youtube' in manjaro_command:
        song = manjaro_command.replace('play on youtube', '')
        manjaro_talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'whats your name' in manjaro_command or 'what your name' in manjaro_command:
        manjaro_talk('my name is manjaro, how i can help you sir?')
    elif 'wake up' in manjaro_command or 'are you there' in manjaro_command:
        manjaro_talk('manjaro always online, sir!')
    elif 'time' in manjaro_command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        manjaro_talk('The time is' + time)
    elif 'search in wikipedia' in manjaro_command:
        person = manjaro_command.replace('search in wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        manjaro_talk(info)
    elif 'open youtube' in manjaro_command or 'open the youtube' in manjaro_command:
        webbrowser.open("https://youtube.com")
    elif 'open the github' in manjaro_command or 'open my github' in manjaro_command:
        webbrowser.open("https://github.com/Jahirrrr")
    elif 'open the browser' in manjaro_command or 'open my browser' in manjaro_command:
        webbrowser.open("https://google.com")
    elif 'open the stack overflow' in manjaro_command:
        webbrowser.open("https://stackoverflow.com")
    elif 'screenshot this image' in manjaro_command or 'screenshot the image' in manjaro_command or 'take screenshot' in manjaro_command:
        image = pyautogui.screenshot()
        image.save(
            'C:\\Users\\your_users_name\\Pictures\\Screenshots\\image.jpg'
            )
        manjaro_talk("image has been screenshot, sir!")
    elif 'can you translate' in manjaro_command or 'translate' in manjaro_command:
        ans = manjaro_command.replace('can you translate', '')
        translator = Translator(to_lang="id")
        translation = translator.translate(ans)
        manjaro_talk("here you translate :")
        print(translation)
    elif 'search in brainly' in manjaro_command:
        br = manjaro_command.replace('search in brainly', '')
        translator = Translator(to_lang='id')
        translation = translator.translate(br)
        brainlypy.set_lang("id")
        results = brainlypy.search(translation)
        question = results.questions[0]
        manjaro_talk("sir, here the answer: ")
        print('ANSWER 1:', question.answers[0])
        if question.answers_count == 2:
            print('ANSWER 2:', question.answers[1])
        if question.answers_count == 3:
            print('ANSWER 3:', question.answers[2])
        if question.answers_count == 4:
            print('ANSWER 4:', question.answers[3])
        if question.answers_count == 5:
            print('ANSWER 4:', question.answers[4])
    elif "calculator" in manjaro_command:
        try:
            manjaro_talk('okay sir, calculator mode is active')
            manjaro_talk('what do you want me to count?')
            client = wolframalpha.Client(app_id)
            quest = im_talk()
            question = quest.replace('calculate', '')
            answer = client.query(question)
            answer = next(answer.results).text
            print("the answer is: " + answer)
            manjaro_talk("the answer is" + answer)
        except Exception as e:
            manjaro_talk("can't get answer sir, please say the question again")
    elif 'stop' in manjaro_command:
        manjaro_talk('manjaro has been out sir, thank you for using me')
        sys.exit()
    elif 'up the volume' in manjaro_command:
        manjaro_talk('okay sir')
        pyautogui.press("volumeup")
    elif 'down the volume' in manjaro_command:
        manjaro_talk('okay sir')
        pyautogui.press("volumedown")
    elif 'mute the volume' in manjaro_command:
        manjaro_talk('okay sir')
        pyautogui.press("volumemute")
    elif 'close the manjaro_command prompt' in manjaro_command:
        os.system("TASKKILL /F /IM cmd.exe")
    elif 'open the sublime text' in manjaro_command:
        manjaro_talk('okay sir, opening sublime text 3')
        os.startfile('C:\\Program Files\\Sublime Text 3\\sublime_text.exe')
    elif "open the firefox" in manjaro_command or "open mozilla" in manjaro_command:
        manjaro_talk("okay sir, opening firefox")
        os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    elif 'open the whatsapp' in manjaro_command:
        os.startfile("C:\\Users\\your_users_name\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    elif 'email' in manjaro_command:
        try:
            manjaro_talk('who do you want to message?')
            name = im_talk()
            receiver = friend_mail_list[name]
            print(receiver)
            manjaro_talk('what is the subject of your message?')
            subject = im_talk()
            manjaro_talk('what message do you want to send?')
            message = im_talk()
            mail(receiver, subject, message)
            manjaro_talk('okay sir, your mail is sent successfully.')
        except Exception as e:
            print(e)
            manjaro_talk("sorry sir, Iam can't send to this email")
    elif 'whatsapp' in manjaro_command:
        manjaro_talk('who do you want to message on whatsapp?')
        name = im_talk()
        check_number = nohp_list[name]
        print(check_number)
        manjaro_talk('what message do you want to send?')
        message = im_talk()
        manjaro_talk('do you want to send it for now?')
        date_message = im_talk()
        if 'yes' in date_message:
            hour = datetime.datetime.now().time().hour
            min = datetime.datetime.now().time().minute
            pywhatkit.sendwhatmsg(check_number, message, hour, min + 1)
            print('okay sir, your message is sent successfully.')
        else:
            manjaro_talk('what time do you want?') # example one
            hour = im_talk()
            manjaro_talk('what minute do you want?') # example twenty
            min = im_talk()
            manjaro_talk('okay, i will process the message')
            print(check_number, message, hour, min)
            pywhatkit.sendwhatmsg(check_number, message, hour, min + 2)
            print('okay sir, your message is sent successfully.')
    elif 'rock' in manjaro_command or 'play' in manjaro_command or 'game' in manjaro_command:
        manjaro_talk('okay sir, running the game')
        RockScissorsGame()

    else:
        manjaro_talk('please say the command again, sir!')