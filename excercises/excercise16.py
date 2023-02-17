import PySimpleGUI as sg

def convert(feet, inches):
    meeters = feet * 0.3048 + inches * 0.0254
    return meeters

feet_label = sg.Text('Enter feet:')
feet_input = sg.Input(key='feet')
inch_label = sg.Text('Enter inches:')
inch_input = sg.Input(key='inches')
result = sg.Text('0 m', key='result')
button = sg.Button('Convert')

layout = [[feet_label, feet_input], [inch_label, inch_input], [button, result]]

window = sg.Window('Convertor', layout, font=('Helvetica', 20))
while True:
    event, value = window.read()

    match event:
        case sg.WINDOW_CLOSED:
            break
        case 'Convert':
            meeters = convert(float(value['feet']), float(value['inches']))
            window['result'].update(value=f"{meeters} m")
window.close()
