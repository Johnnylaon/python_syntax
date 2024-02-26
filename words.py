
def print_upper_words(words, must_start_with):
    ''' Print each word on seperate line, uppercase, only print words that
    start with the letter if given

    '''
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter.lower()):
                print(word.upper())




# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"H", "Y"})