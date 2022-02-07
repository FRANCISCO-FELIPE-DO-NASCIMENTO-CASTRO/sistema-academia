from tkinter import Event, Widget
import PySimpleGUI as sg

layout = [
    [sg.Text('Text')]
]


window = sg.Window('Teste', layout=layout)

while True:
    event, values = window.Read()

window.close()
