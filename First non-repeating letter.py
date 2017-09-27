def first_non_repeating_letter(string):
    lowercase=string.lower()
    for i,letter in enumerate(lowercase):
        if lowercase.count(letter)==1:
            return string[i]
    return ''



'''
Write a function named firstNonRepeatingCharacter that takes a string input, and returns the first character that is not
 repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the str
ing, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return th
e correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return the empty string ("").
sTreSS
'''
