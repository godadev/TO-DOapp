# Exercises
# Lists and List manipulation


# Exercise 1

filenames = ['document', 'report', 'presentation']

for index, item in enumerate(filenames):
    print(f'{index}.{item.capitalize()}.txt')


def file_handler_v1(command):
    match command.split():
        case ['show']:
            print('List all files and directories: ')
            # code to list files
        case ['remove', *files]:
            print('Removing files: {}'.format(files))
            # code to remove files
        case _:
            print('Command not recognized')


# function call params show, remove (files)
# file_handler_v1('show')

# Exercise 3

ips = ['100.122.133.105', '100.122.133.111']

while True:
    user_input = input('Please enter a number to display the IP address or (x) to exit: ')
    match user_input:
        case user_input:
            if user_input == 'x':
                print('Goodbye')
                break
            else:
                print(f'You chose to display the IP: {ips[int(user_input)]}')
