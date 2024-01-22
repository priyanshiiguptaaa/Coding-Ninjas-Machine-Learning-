def reverse_words(sentence):
    words = sentence.split()  # Split the sentence into a list of words
    reversed_words = [word[::-1] for word in words]  # Reverse each word using slicing
    reversed_sentence = ' '.join(reversed_words)  # Join the reversed words into a sentence
    print(reversed_sentence)

# Take input from the user
input_sentence = input()

# Call the function with user input
reverse_words(input_sentence)
        
