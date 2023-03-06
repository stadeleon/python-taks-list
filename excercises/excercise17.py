import PySimpleGUI as sg

sg.theme('DarkBlue2')
def km_to_miles(km):
    return km / 1.6


label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

output = sg.Text(key="output")

window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output], [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            try:
                km = float(values["kms"])
                result = km_to_miles(km)
                window['output'].update(value=result)
            except ValueError:
                sg.popup_no_buttons('Enter the Miles', auto_close=True, auto_close_duration=3, no_titlebar=True)
        case sg.WIN_CLOSED | 'Exit':
            break

window.close()
