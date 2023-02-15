# from functions import get_todos, write_todos
# from functions import *
import functions
import time
now = time.strftime('%b %d, %Y %H:%M:%S')
print(now)

while True:
    action = input('Type add, show, edit, complete or exit: ')
    methodList = action.split(' ', 1)

    try:
        match methodList[0]:
            case 'add' | 'new':
                todo = methodList[1]
                todos = functions.get_todos()
                todos.append(todo + "\n")

                functions.write_todos(todos)

            case 'show':
                todos = functions.get_todos()

                for index, todo in enumerate([item.strip() for item in todos]):
                    print(f"{(index+1)}-{todo}")
                # for index, todo in enumerate(todos):
                #     print(f"{(index+1)}-{todo.strip()}")
            case 'exit':
                break
            case 'edit':
                todos = functions.get_todos()

                number = int(methodList[1])
                todos[number-1] = input('Enter todo Item:') + '\n'
                print(todos)
                functions.write_todos(todos)
            case 'complete':
                try:
                    todos = functions.get_todos()

                    item = int(methodList[1])-1
                    removedItemContext = todos[item].strip()
                    todos.pop(item)
                    functions.write_todos(todos)

                    message = f"Todo item {removedItemContext} was removed from list"
                    print(message)
                except IndexError:
                    print("There is no such index in list")
            case _:
                print('Enter correct action')
    except ValueError:
        print('Not valid command')

print('Bye')

# name = input('Enter Your Name:')
# while name:
#     print(name.capitalize())
#     name = input('Enter Your Name:')

# user_prompt = "Enter a todo:"
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
#
# todos = [todo1, todo2, todo3, "Hello", "World"]
#
# print(todos)
# print(type(todos))
#
#
