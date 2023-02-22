# Sorting a list alphabetically
# sort.() Sorts a list ascending or descending whit reverse = True

waiting_list =['Matej', 'Ben', 'John', 'Mike']
waiting_list.sort()

for index, item in enumerate(waiting_list):
    print(f'{index + 1}.{item.capitalize()}')
