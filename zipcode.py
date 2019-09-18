from banner import banner

banner("ZIP CODE SORTER", "Rhianna Jenkins")

print('')
print('Welcome to the Newaygo County zip code sorter.')

answer = 'Y'

while answer == 'Y':
    zip_code = input('Please enter a zip code: ')

    if zip_code == '49309':
        print(f'The zip code {zip_code} is for Bitely.')
        answer = input('Would you like to enter another zip code (Y/N)? ')
        print('')
        if answer == 'Y':
            pass
        else:
            print('')
            print('Thank you for using the Newaygo Country zip code sorter. Goodbye!')

    elif zip_code == '49312':
        print(f'The zip code {zip_code} is for Brohman.')
        answer = input('Would you like to enter another zip code (Y/N)? ')
        print('')
        if answer == 'Y':
            pass
        else:
            print('')
            print('Thank you for using the Newaygo Country zip code sorter. Goodbye!')

    elif zip_code == '49337':
        print(f'The zip code {zip_code} is for Croton and Newaygo.')
        answer = input('Would you like to enter another zip code (Y/N)? ')
        print('')
        if answer == 'Y':
            pass
        else:
            print('')
            print('Thank you for using the Newaygo Country zip code sorter. Goodbye!')

    elif zip_code == '49412':
        print(f'The zip code {zip_code} is for Fremont.')
        answer = input('Would you like to enter another zip code (Y/N)? ')
        print('')
        if answer == 'Y':
            pass
        else:
            print('')
            print('Thank you for using the Newaygo Country zip code sorter. Goodbye!')

    elif zip_code == '49413':
        print(f'The zip code {zip_code} is for Fremont.')
        answer = input('Would you like to enter another zip code (Y/N)? ')
        print('')
        if answer == 'Y':
            pass
        else:
            print('')
            print('Thank you for using the Newaygo Country zip code sorter. Goodbye!')

    elif zip_code == '49327':
        print(f'The zip code {zip_code} is for Grant.')
        answer = input('Would you like to enter another zip code (Y/N)? ')
        print('')
        if answer == 'Y':
            pass
        else:
            print('')
            print('Thank you for using the Newaygo Country zip code sorter. Goodbye!')

    elif zip_code == '49349':
        print(f'The zip code {zip_code} is for Whitecloud.')
        answer = input('Would you like to enter another zip code (Y/N)? ')
        print('')
        if answer == 'Y':
            pass
        else:
            print('')
            print('Thank you for using the Newaygo Country zip code sorter. Goodbye!')

    else:
        print(f'The zip code {zip_code} is not in Newaygo County.')
        print('')