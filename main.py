# A TO-DO application like many others
# by Matej Music 2023
# ------------------------------------

while True:
    user_action = input('Type add, show, edit, complete or exit(x): ')
    user_action = user_action.strip()

    match user_action:

        # add command to add a new to-do item and store it in a file
        case 'add':
            todo = input('Enter a TO-DO: ') + '\n'

            file = open('SaveFiles/todo-data.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('SaveFiles/todo-data.txt', 'w')
            file.writelines(todos)
            file.close()

        # show command to show all items in the file
        case 'show':
            file = open('SaveFiles/todo-data.txt', 'r')
            todos = file.readlines()

            # new empty list to store the to-dos in to prepare for cleanup because in the add command we must add a
            # newline character but when we print it with show the print function automatically adds another new line

            new_todos = []
            # List comprehension to clean the file of unwanted newlines
            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                item = item.title()
                row = f'{index + 1}-{item}'
                print(row)
            file.close()

        # edit command to edit an existing entry in to-dos
        case 'edit':
            number = int(input('Enter the number of TODO to edit: '))
            number -= 1
            new_todo = input('Enter new TODO: ')
            todos[number] = new_todo

        # complete command to complete a task in to-dos and remove it from the file
        case 'complete':
            number = int(input('Enter the number of TODO to edit: '))
            todos.pop(number - 1)

        # exit command to quit the program
        case 'exit' | 'x':
            break
