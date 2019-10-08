from banner import banner
import random

banner('LOTTERY', 'Rhianna Jenkins')
print('Welcome to the Lottery game. Choose a number between 1 and 999. If you choose the same as the computer, you will win 10 times your bet amount')

balance = 20

while 0 < balance < 1000000:
    print(f'BALANCE: ${balance}')
    bet_amount = int(input('How much do you want to bet? '))
    lot_num = int(input('What number do you pick? '))

    com_num = random.randint(1, 999)
    win_amount = bet_amount * 10

    if lot_num != com_num:
        print(f"I'm sorry, but you chose {lot_num} and the computer chose {com_num}. You lose {bet_amount}.")
    else:
        print(f"Awesome! You chose {lot_num} and so did the computer! You win {win_amount}")