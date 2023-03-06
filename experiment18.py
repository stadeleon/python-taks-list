import functions
import PySimpleGUI as sg
import time

def change_buttons_status(buttons, status='active'):
    status = not (status == 'active')
    for button in buttons:
        window[button].update(disabled=status)


sg.theme("DarkBlue2")

clock = sg.Text(time.strftime('%b %d, %Y %H:%M:%S'), key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo', enable_events=True)

add_button = sg.Button(key="Add", image_source='images/add.png',
                       disabled=True,
                       mouseover_colors=('LightBlue2', 'green'), tooltip='Add to do')
edit_button = sg.Button("Edit", disabled=True, mouseover_colors=('LightBlue2', 'green'))
complete_button = sg.Button(key="Complete", image_source='images/complete.png',
                            disabled=True, disabled_button_color='gray',
                            mouseover_colors=('LightBlue2', 'green'), tooltip='Complete to do')
exit_button = sg.Button("Exit", mouseover_colors=('LightBlue2'))

status = sg.Text('', key='status')

tasks_list_display_box = sg.Listbox(values=functions.get_todos(),
                                    size=(45, 10),
                                    key='edit_item',
                                    enable_events=True)

left_column = sg.Column([[tasks_list_display_box], [status]])
right_column = sg.Column([[complete_button], [exit_button]])
layout = [[clock], [label], [input_box, add_button, edit_button], [left_column, right_column]]
window = sg.Window('My To-Do GUI Application',
                   layout=layout,
                   font=('Helvetica', 20))

last_selection = ''

while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    # print(event, values)
    todos = functions.get_todos()

    match event:
        case sg.WINDOW_CLOSED | sg.WIN_CLOSED | 'Exit':
            break
        case 'todo':
            window['Add'].update(disabled=not bool(len(values['todo'])))
        case "Add":
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['edit_item'].update(values=todos)
            window['status'].update(value="New task added")
            window['todo'].update(value='')
            change_buttons_status(['Add', 'Edit', 'Complete'], 'inactive')
        case 'edit_item':
            window['todo'].update(value=values['edit_item'][0].strip())
            change_buttons_status(['Edit', 'Complete'], 'active')
        case "Edit":
            try:
                search = values['edit_item'][0] if (len(values['edit_item'])) else last_selection
                index = todos.index(search)
                new_value = values['todo'] + "\n"
                last_selection = new_value
                todos[index] = new_value
                functions.write_todos(todos)
                window['edit_item'].update(values=todos)
                window['todo'].update(value='')
                change_buttons_status(['Add', 'Edit', 'Complete'], 'inactive')
                window['status'].update(value=f"Task {index + 1} updated")
            except IndexError:
                sg.PopupNoButtons('Select item before editing',
                                  auto_close=True, no_titlebar=True, modal=True, font=('Helvetica', 20))
        case "Complete":
            try:
                task = values['edit_item'][0]
                index = todos.index(task)
                todos.pop(index)
                functions.write_todos(todos)
                window['edit_item'].update(values=todos)
                window['todo'].update(value='')
                window['status'].update(value=f"Task {task.strip()} completed")
                change_buttons_status(['Add', 'Edit', 'Complete'], 'inactive')
            except IndexError:
                sg.PopupNoButtons('Select item to complete',
                                  auto_close=True, no_titlebar=True, modal=True, font=('Helvetica', 20))
window.close()
