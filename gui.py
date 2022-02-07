import PySimpleGUI as sg

def main():
    layout = [
        [sg.Input("textbox", size = (20, 1), key = '-INPUT-')],
    ]
    window = sg.Window("Title", layout, finalize = True)
    
    window['-INPUT-'].Widget.configure(highlightcolor = 'red', highlightthickness = 2)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        
        print(event, values)

        window.close()

if __name__ == '__main__':
   main()
