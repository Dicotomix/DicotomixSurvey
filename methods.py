#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unidecode import unidecode

# spell a word
def spell_word(word, method, max_letter = -1):
    count_letter = 0
    total_steps = 0
    
    for letter in word:
        count_letter += 1
        total_steps += method(letter)
        print letter, method(letter)

        if(max_letter >= 0 and count_letter >= max_letter):
            return total_steps
        
    return total_steps


# remove accents and uppercase
def minimize_letter(s):
    s.encode(encoding='UTF-8',errors='strict')
    s = unidecode(s)
    return s.lower()

# dichotomy on letter
def letter_dichotomy(letter):
    first, last = ord('a'), ord('z') + 1
    letter = minimize_letter(letter)

    goal, cur = ord(letter), (first + last) / 2
    counter = 0

    while cur != goal:
        counter += 1
        cur = (first + last) / 2
        
        if cur <= goal:
            first = cur
        else:
            last = cur

    if counter == 0:
        counter = 1
    return counter

# the other methods all work in the same way, let's make a function that iterate through row then columns of a 2D table "letters" containing the letters
def abstract_method(letter, letters):
    letter = minimize_letter(letter)

    row = 0
    col = 0

    while not letter in letters[row]:
        row += 1

    while letter != letters[row][col]:
        col += 1

    # row + 1 to choose row
    # col + 1 to choose column
    # row + col + 2 steps total
    return row + col + 2

# method 1
def letter_ejasint(letter):
    letters = [['e', 'a', 'n', 'r', 'c', 'v'], 
               ['j', 'i', 'l', 'p', 'h', 'w'],
               ['s', 'u', 'd', 'g', 'k'],
               ['t', 'm', 'b', 'z'],
               ['o', 'f', 'x'],
               ['q', 'y']]

    return abstract_method(letter, letters)

# method 2
def letter_clignement(letter):
    letters = [['a', 'e', 'i', 'o', 'u', 'y'],
               ['b', 'c', 'd', 'f'],
               ['g', 'h', 'j', 'k', 'l'],
               ['m', 'n', 'p', 'q', 'r', 's'],
               ['t', 'v', 'w', 'x', 'z']]

    return abstract_method(letter, letters)

# method 3
def letter_keyboard(letter):
    letters = [['a','z','e','r','t','y','u','i','o','p'],
               ['q','s','d','f','g','h','j','k','l','m'],
               ['w','x','c','v','b','n']]

    return abstract_method(letter, letters)

# method 4
def letter_4(letter):
    letters = [['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k'],
               ['l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'],
               ['a', 'e', 'i', 'o', 'u', 'y']]

    return abstract_method(letter, letters)

# method 5
def letter_5(letter):
    letters = [['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm'],
               ['n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'],
               ['a', 'e', 'i', 'o', 'u', 'y']]

    return abstract_method(letter, letters)

# mean by letter for spelling the whole alphabet (no considerations of frequency)
def check_alphabet(count_steps):
    s = 0
    c = ord('a')
    while c != ord('z') + 1:
        cur = count_steps(chr(c))
        s += cur
        c += 1
    print s
