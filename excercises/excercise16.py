import PySimpleGUI as sg

feet_label = sg.Text('Enter feet:')
feet_input = sg.Input()
inch_label = sg.Text('Enter inches:')
inch_input = sg.Input()

button = sg.Button('Convert')

layout = [[feet_label, feet_input], [inch_label, inch_input], [button]]

window = sg.Window('Convertor', layout)

window.read()
window.close()
