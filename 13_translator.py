# m language

from re import M


def translate(phrase):
    translation="" 
    for letter in phrase:
        if letter in "AEIOUaeiou" :
            traslation= traslation+ "m"
        else: 
            translation= translation+ letter
    return translation

print(translate(input("Enter a phrase :")))