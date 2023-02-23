contents = ['Need to know how to cook carrots on the stove,',
            'in the microwave, or in the slow cooker?',
            'Check out our Test Kitchens expert tips on how to cook carrots.']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f'../SaveFiles/{filename}', 'w')
    file.write(content)
