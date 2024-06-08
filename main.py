import random

number_len = 3


def get_secret_num():
    secret_num = "".join([str(random.randint(0, 9)) for _ in range(3)])
    return secret_num


def get_clues(secret_num, user_input):
    clues = []

    if not any(digit in user_input for digit in secret_num):
        return 'All wrong'

    for i in range(3):
        if secret_num[i] == user_input[i]:
            clues.append('Fermi')
        elif user_input[i] in secret_num:
            clues.append('Pico')
        else:
            clues.append("Bagels")
    return clues


def main_game():
    max_guesses = 10
    secret_num = get_secret_num()
    print('I have thought up a number.')
    print(f'You have {max_guesses} guesses to get it.')
    print(secret_num)

    guesses_taken = 0

    while guesses_taken < max_guesses:
        user_input = input('Enter a three-digit number here: ').strip()
        if user_input.isdigit() and len(user_input) == 3:
            if secret_num == user_input:
                print('Congratulations, you won')
                return
            else:
                print('Hmm, not quite right, here is a clue')
                print(get_clues(secret_num, user_input))
                guesses_taken += 1
        else:
            print('Wrong input, try again.')
    print('You lost')


if __name__ == '__main__':
    print("Bagels, a deductive logic game. I am thinking of a 3-digit number. Try to guess what it is."
          "\nHere are some clues: When I say: That means: "
          "\nPico - one digit is correct but in the wrong position. "
          "\nFermi - one digit is correct and in the right position. "
          "\nBagels No digit is correct. "
          "\nI have thought up a number.You have 10 guesses to get it.")
    main_game()
