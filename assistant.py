# Patrick Apgar

# import wolframalpha


# app_id = '7RQEH5-E64LEQHTY8'  # get your own at https://products.wolframalpha.com/api/
# client = wolframalpha.Client(app_id)


# res = client.query('temperature in Washington, DC on October 3, 2012')
# print(next(res.results).text)

import PySimpleGUI as sg

# Define the window's contents
layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close() 