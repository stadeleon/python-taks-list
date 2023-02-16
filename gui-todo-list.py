import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo', enable_events=True)

add_button = sg.Button("Add", disabled=True, disabled_button_color='gray')
edit_button = sg.Button("Edit", disabled=True, disabled_button_color='gray')

tasks_list_display_box = sg.Listbox(values=functions.get_todos(),
                                    size=(45, 10),
                                    key='edit_item',
                                    enable_events=True)

layout = [[label], [input_box, add_button, edit_button], [tasks_list_display_box]]
window = sg.Window('My To-Do GUI Application',
                   layout=layout,
                   font=('Helvetica', 20))

last_selection = ''

while True:
    event, values = window.read()
    print(event, values)
    todos = functions.get_todos()

    match event:
        case sg.WINDOW_CLOSED:
            break
        case 'todo':
            window['Add'].update(disabled=not bool(len(values['todo'])))
        case "Add":
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case 'edit_item':
            window['todo'].update(value=values['edit_item'][0].strip())
            window['Edit'].update(disabled=False)
        case "Edit":
            search = values['edit_item'][0] if (len(values['edit_item'])) else last_selection
            index = todos.index(search)

            new_value = values['todo'] + "\n"
            last_selection = new_value
            todos[index] = new_value

            functions.write_todos(todos)
            window['edit_item'].update(values=todos)
            window['todo'].update(value='')
            window['Edit'].update(disabled=True)
window.close()
