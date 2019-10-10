from banner import banner
import math

def main():
    banner('Pythagorean Calculator', 'Rhianna Jenkins')
    print('We will help you find the missing side of a right triangle. The lengths of the legs are "a" and "b", and the length of the hypotenuse is "c".')
    print('')

    def error_1():
        print('You have to have two side lengths for this to work!')


    def error_2():
        print('I have nothing to calculate!')


    calc_again = 'Y'

    while calc_again == 'Y':
        print("Please enter the length of each side, or leave it blank if you don't know.")

        length_a = input('a = ')
        if length_a == '':
            length_a = 0
        elif length_a != '':
            length_a = float(length_a)

        length_b = input('b = ')
        if length_b == '':
            length_b = 0
        elif length_b != '':
            length_b = float(length_b)

        length_c = input('c = ')
        if length_c == '':
            length_c = 0
        elif length_c != '':
            length_c = float(length_c)

        if length_a == 0 and length_b == 0:
            error_1()
            continue
        elif length_a == 0 and length_c == 0:
            error_1()
            continue
        elif length_b == 0 and length_c == 0:
            error_1()
            continue

        if length_a != 0 and length_b != 0 and length_c != 0:
            error_2()
            continue



        if length_a == 0:
            value_a = str(math.sqrt((length_c * length_c) - (length_b * length_b)))
            print(f"Your missing side is a and it's length is {value_a}.")
        elif length_b == 0:
            value_b = str(math.sqrt((length_c * length_c) - (length_a * length_a)))
            print(f"Your missing side is b and it's length is {value_b}.")
        elif length_c == 0:
            value_c = str(math.sqrt((length_a * length_a) + (length_b * length_b)))
            print(f"Your missing side is c and it's length is {value_c}.")

        calc_again = input('Would you like to calculate another triangle (Y/N)? ')
        print('')
        calc_again = calc_again.upper()
        if calc_again == 'Y':
            pass
        elif calc_again == 'N':
            print('Thank you for using the Pythagorean Calculator.')
        else:
            print('I hope that means no.')


if __name__ == '__main__':
    main()