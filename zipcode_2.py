from banner import banner

banner("ZIP CODE SORTER", "Rhianna Jenkins")

zc = {49309: 'Bitely', 49312: 'Brohman', 49337: 'Croton and Newaygo', 49412: 'Fremont', 49413: 'Fremont', 49327: 'Grant', 49349: 'Whitecloud'}

print('')
print('Welcome to the Newaygo County zip code sorter.')

answer = 'Y'

while answer == 'Y':
    zc = {49309: 'Bitely', 49312: 'Brohman', 49337: 'Croton and Newaygo', 49412: 'Fremont', 49413: 'Fremont', 49327: 'Grant', 49349: 'Whitecloud'}

    zip_code = int(input('Please enter a zip code: '))
    zc.keys = zip_code

    print(f'The zip code {zip code} is for {zc[zip_code]}.')
    answer = input('Would you like to enter another zip code (Y/N)? ')
    if answer == 'Y':
        pass
    else:
        print('')
        print('Thank you for using the Newaygo County zip code sorter. Goodbye!')

