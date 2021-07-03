# Giraffe language
# vowels ===> g
# e.g dog = dgt, cat== cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation


print(translate(input("Enter a phrase:")))
