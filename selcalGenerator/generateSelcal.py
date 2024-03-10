import random


def generate_selcal():
    selcal_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'P', 'Q', 'R', 'S']

    for i in range(2):
        first_letter = random.choice(selcal_letters[:-1])
        letters_avail = [letter for letter in selcal_letters if letter > first_letter]
        second_letter = random.choice(letters_avail)
        if i == 0:
            segment_a = first_letter + second_letter
        else:
            segment_b = first_letter + second_letter

    return segment_a + "-" + segment_b
