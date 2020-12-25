# Patrick Apgar

import wolframalpha
import PySimpleGUI as sg
import wikipedia

app_id = '7RQEH5-E64LEQHTY8'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)

sg.theme('Topanga')
# Define the window's contents
layout = [  [sg.Text("Enter a command")],
            [sg.Input()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the window
window = sg.Window('Alexandra', layout)      

while True:
    # Display and interact with the Window
    event, values = window.read()                  

    if event in (None, 'Cancel'):
        break
    # Do something with the information gathered
    res = client.query(values[0])
    sg.popup(next(res.results).text) # Create a popup window to display information

    #print(next(res.results).text)

# Finish up by removing from the screen
window.close() 