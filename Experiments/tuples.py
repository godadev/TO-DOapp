# This is not about tuples but only shows that tuples would be better if used here instead of lists which are immutable

filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt']


new_filenames = []
for filename in filenames:
    filename = filename.replace('.', '-', 1)
    new_filenames.append(filename)

print(filenames)
print(new_filenames)

