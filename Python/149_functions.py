def palindrome_sentence(sentence):
    string = ""

    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].casefold() == string.casefold()

word = input("Enter a sentence:")

if palindrome_sentence(word):
    print("{} is a palindrome sentence.".format(word))

else:
    print("{} is not a palindrome sentence.".format(word))