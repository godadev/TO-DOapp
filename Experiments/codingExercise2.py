while True:
    user_country = input('Please enter the country you live in (or "q" to quit.)')
    match user_country:
        case 'USA':
            print('Hello')
        case 'India':
            print('Namaste')
        case 'Germany':
            print('Hallo')
        case 'q':
            print('Goodbye')
            break
