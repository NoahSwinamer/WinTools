import os
import PySimpleGUI as sg
import importlib
import runpy
import tkinter


#sg.Window(title="Wintools" , layout=[[sg.Text("trash and temp"), sg.Ok("Trash"), sg.Button("Temp"), ]], margins=(100, 50)).read()

layout = [[sg.Text("trash and temp"), sg.Button("ok"), sg.Button("Cancel")]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print(runpy.run_module(mod_name="trashtools"), values[0])

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'ok': # if user closes window or clicks cancel
        break
    print(runpy.run_module(mod_name="temp"), values[0])


window.close()

#Ok = event, values = runpy.run_module(mod_name="trashtools.py")   #                    runpy.run_module(mod_name="trashtools.py")#exec(open("trashtools.py").read()) 

#Temp = importlib.find_loader("temp.py")