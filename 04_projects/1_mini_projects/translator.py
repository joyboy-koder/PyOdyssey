#This programs receives a piece of text from a user and replaces whatever vowel in the piece of text with the letter 'g'. (I CALL THIS BABY LANGUAGE, HAHA!)

vowels = 'aeiou'
result = ''

def translate(text):
    '''
    Description: This functions loops through every letter of the word or sentence you input, and whenever it finds a vowel it replaces it with the letter 'g'. Else it is made to display your exact text you inputed.
    '''
    global result
    for letter in text:
        if letter.lower() in vowels:
            result += 'g'
        else:
            result += letter
    print(result)
translate(input("What do you want to translate: "))