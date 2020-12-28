# Patrick Apgar

import wolframalpha
import PySimpleGUI as sg
import wikipedia
from gtts import gTTS
from playsound import playsound

app_id = '7RQEH5-E64LEQHTY8'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)

v = gTTS(text="Hello! Maye I know your name please", lang="en", slow=False)
v.save("name.mp3")
playsound("name.mp3")
name = input("Enter name here: ")
s = gTTS(text="hello" + name + " I am Google Text To Speech", lang="en")
s.save("welcome.mp3")
playsound("welcome.mp3")

# sg.theme('Topanga')
# # Define the window's contents
# layout = [  [sg.Text("Enter a command")],
#             [sg.Input()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]

# # Create the window
# window = sg.Window('Alexandra', layout)      

# while True:
#     # Display and interact with the Window
#     event, values = window.read()                  

#     if event in (None, 'Cancel'):
#         break

#     # Do something with the information gathered
#     res = client.query(values[0])
#     wolfram_response = next(res.results).text

#     wikipedia_response = wikipedia.summary(values[0], sentences=2)
#     sg.popup("Result from Wolfram Alpha show that " + values[0] + " is " + wolfram_response, "A result from Wikipedia also shows that: " + wikipedia_response) # Create a popup window to display information

#     # print(values[0])
# # Finish up by removing from the screen
# window.close() 
