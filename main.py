# A TO-DO application like many others
# by Matej Music 2023
# ------------------------------------

todos = []

while True:
    user_action = input('Type add, show, edit, complete or exit(x): ')
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a TO-DO: ')
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                item = item.title()
                row = f'{index + 1}-{item}'
                print(row)
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
