import random

choices = ['scissors', 'paper', 'rock']
score = 0
name = input('Enter your name: > ')
print('Hello,', name)

file = open('rating.txt', 'r')
for line in file:
    splitted_line = line.split()
    if splitted_line[0] == name:
        score = int(splitted_line[-1])
        break
    else:
        score = 0
        break
file.close()

list_of_options = input('> ').split(',')
print("Okay, let's start")

if list_of_options[0] != '':
    while True:
        user_choice = input('> ')
        computer_choice = random.choice(list_of_options)
        if user_choice == '!exit':
            print('Bye!')
            break
        elif user_choice == '!rating':
            print("Your rating:", score)
        elif user_choice in list_of_options:
            new_list = list_of_options[list_of_options.index(user_choice) + 1:]
            new_list.extend(list_of_options[0:list_of_options.index(user_choice)])
            defeating_chosen = new_list[0:(len(new_list) // 2)]
            if user_choice == computer_choice:
                score += 50
                print(f'There is a draw ({user_choice})')
            elif computer_choice in defeating_chosen:
                print('Sorry, but computer chose', computer_choice)
            else:
                score += 100
                print(f'Well done. Computer chose {computer_choice} and failed')
        else:
            print('Invalid input')

elif list_of_options[0] == '':
    while True:
        pc_choice = random.choice(choices)
        player_choice = input('> ')

        if player_choice == "!rating":
            print("Your rating:", score)
        elif player_choice == '!exit':
            print("Bye!")
            break
        elif player_choice == pc_choice:
            score += 50
            print(f"There is a draw ({pc_choice})")
        elif player_choice not in choices and player_choice != '!exit':
            print("Invalid input")
        elif player_choice != pc_choice:
            if player_choice == 'scissors' and pc_choice == 'rock' \
                    or player_choice == 'rock' and pc_choice == 'paper' \
                    or player_choice == 'paper' and pc_choice == 'scissors':
                print(f"Sorry, but computer chose {pc_choice}")
            elif pc_choice == 'scissors' and player_choice == 'rock' \
                    or pc_choice == 'rock' and player_choice == 'paper' \
                    or pc_choice == 'paper' and player_choice == 'scissors':
                score += 100
                print(f"Well done. Computer chose {pc_choice} and failed")