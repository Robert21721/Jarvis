import PySimpleGUI as sg
import jarvis_functions
import switcher

jarvis_functions.wishme()

no = 0

layout1 = [[sg.Text("Do you want to use the speech recognition?", size = (50, 5))],
           
            [sg.Button("YES"), sg.Button("NO"), sg.Button("EXIT")]]

layout2 = [[sg.Text("Write your command here"), sg.InputText()],
            
            [sg.Button("SEND"), sg.Button("EXIT")] ]

window = sg.Window("Meow", layout1)

while True:
    event, values = window.read()

    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

    if event == "YES":
        jarvis_functions.speak("I am listening")
        jarvis_functions.takeCommand_loop()
        break

    if event == "NO":
        no = True
        break
        
window.close()


if no == True:
    window = sg.Window("Meow", layout2)

    while True:
        event, values = window.read()

        if event == "EXIT" or event == sg.WIN_CLOSED:
            break

        if event == "SEND":
            switcher.simple_switcher(values[0])

        
window.close()
