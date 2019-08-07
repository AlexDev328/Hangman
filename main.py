from random import choice

max_steps = 6

words = ["скала", "деревня", "доска"]
alphabet_lower = [chr(ord("а") + i) for i in range(32)]
alphabet_lower.append('ё')
alphabet = ''.join(alphabet_lower)

PICT = ['''
    +---+
    |   |
        |
        |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 =========''']


def drow(step, word, letters):
    print(PICT[step])
    print('\n')
    for i in word:
        if i in letters:
            print(" " + i + " ", end="")
        else:
            print(" * ", end="")
    print("\nВведите букву:")


def check_win(word, letters):
    for i in range(len(word)):
        if word[i] not in letters:
            return False
    return True


def main():
    word = choice(words)
    step = 0
    tryletters = ''
    drow(step, word, tryletters)
    while (step < max_steps):
        guess = input()
        if guess in tryletters:
            print("Вы уже пробовали эту букву")
            continue
        tryletters += guess
        if guess in word:
            print("Вы угадали букву")
        else:
            step += 1
            print("Вы не угадали букву")
        drow(step, word, tryletters)
        if check_win(word, tryletters):
            print("Вы угадали слово!")
            exit()
    print("Вы проиграли")


if __name__ == "__main__":
    main()
