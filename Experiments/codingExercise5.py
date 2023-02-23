# 1 exercise - Create a program that reads that file and prints out its text. The first letter of each word in the
# output should be uppercase.

file = open('TextFiles/essay.txt', 'r')
words = file.read()
print(words.title())
file.close()

# 2 exercise - Write a program that reads the essay.txt file and returns the number of characters contained in the file.

file = open('TextFiles/essay.txt', 'r')
file_read = file.read()
print(f'There are {len(file_read)} characters in the file')
file.close()

# 3 exercise - Create a program that, whenever executed, asks the user to enter a new member in the command line:

file = open('TextFiles/members.txt', 'r')
print('Members in the file are: ')
display_members = file.read()
print(display_members.title())
file.close()

file = open('TextFiles/members.txt', 'r')
existing_members = file.readlines()
file.close()

new_member = input('Please add a new member: ')
existing_members.append(new_member + '\n')
file = open('TextFiles/members.txt', 'w')
file.writelines(existing_members)
print(f'New member {new_member} added.')

# 4 Create a program that generates multiple text files by iterating over the filenames list. The text Hello should
# be written inside each generated text file.

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f'TextFiles/{filename}', 'w')
    file.write('Hello')
    file.close()

# 5 Create a program that reads each text file and prints out the content of each in the command line. The expected
# output would be like the following:

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f'TextFiles/{filename}', 'r')
    file_content = file.readline()
    print(file_content)
    file.close()