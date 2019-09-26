import os
from banner import banner

banner('HTML TAG COUNTER', 'Rhianna Jenkins')

def load(filename):
    data = []
    print(f"..... loading from {filename}")
    if os.path.exists(filename):
        with open(filename) as fin:
            for line in fin.readlines():
                data.append(line)

    return data

def tag_count(line):
    count_tag = 0
    previous_char = None
    for char in line:
        if char != "/" and previous_char == "<":
            count_tag += 1
        previous_char = char
    return count_tag


print('Welcome to the HTML tag counter.')

count_another = 'Y'
while count_another.upper() == 'Y':
    html_file = input('Please enter the name of an HTML file: ')
    loaded_file = load(html_file)
    count = 0
    for line in loaded_file:
        count = count + tag_count(line)



    print(f'the file {html_file} contains {count} tags.')

    count_another = input("Would you like to count another HTML file (Y/N)?: ")

    if count_another.upper() == 'Y':
        pass
    elif count_another.upper() == 'N':
        print('')
        print('Thank you for using the HTML counter. Goodbye!')
        break
    else:
        print('That was not a valid answer.')