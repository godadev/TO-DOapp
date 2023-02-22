# A TO-DO application like many others
# by Matej Music 2023
# ------------------------------------
# Added some functionality to save and read from a file

while True:
    user_action = input('Type add, show, edit, complete or exit(x): ')
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a TO-DO: ') + '\n'

            file = open('todo-data.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todo-data.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todo-data.txt', 'r')
            todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.title()
                row = f'{index + 1}-{item}'
                print(row)
            file.close()
        case 'edit':
            number = int(input('Enter the number of TODO to edit: '))
            number -= 1
            new_todo = input('Enter new TODO: ')
            todos[number] = new_todo
        case 'complete':
            number = int(input('Enter the number of TODO to edit: '))
            todos.pop(number - 1)
        case 'exit' | 'x':
            break
