# Exchange calculator

amount = int(input('Please input a dollar amount: '))
exchange_rate = 0.95


name = 'Mujo'
print(name)

amount_in_euros = amount * exchange_rate

print(f'You have {amount_in_euros} euros.')

# ------------------------------------------------------

# Rankings

ranking = ['John', 'Sen', 'Lisa']

rank_number = int(input('Please enter the rank number of the athlete: '))
rank_number -= 1
print(ranking[rank_number])

# ------------------------------------------------------

# Rankings-2
print(ranking)
rank_name = input('Enter the athletes name: ')
rank = ranking.index(rank_name) + 1

print(rank)
