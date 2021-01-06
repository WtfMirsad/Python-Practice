import PySimpleGUI as sg

sg.theme('DarkAmber')



layout = [  [sg.Text('Enter the calculation and press ok when you want to see the result')],
            [sg.InputText(),sg.Text('='),sg.Text(size=(20,1) , key='-OUTPUT-')],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Button('Submit', visible=False, bind_return_key=True)] ] #postavlja nevidljivo dugme koje se aktivira sa pritiskom entera


window = sg.Window('Calculator',layout)

while True:
    event,values = window.read()
    calc = values[0]
    result = str(eval(calc)) #eval funkcija pretvara text u kalkulaciju i daje rezultat
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        window['-OUTPUT-'].update(result) # dio Window sa key = -OUTPUT- biva updejtovano sa vrijednoscu result
    print(result)

window.close()
