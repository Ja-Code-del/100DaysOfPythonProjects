from cipher import letters
#greet
print("Hello\nAm LACY, A program tha can count down the number of letter into a given text and give you other "
      "information about it")
#vowels = ["a", "e", "i", "o", "u", "y"]
punctuations = [" ", ";", ".", "!", "?", ":", "'"]
numb_of_vowels = 0

#ask a text ; variable : user_text
user_text = input("Enter your text \n").lower()
user_text = user_text.replace("\n", " ")  #ignore the return

#count the vowels
text_length = len(user_text)
numb_of_punctuation = 0
for i in range(text_length):
    for j in range(len(tool.alphabet)):
        if user_text[i] == tool.alphabet[j]:
            numb_of_vowels += 1

#count the punctuations or other symbols using the "count" method
for i in range(len(punctuations)):
    numb_of_punctuation += user_text.count(punctuations[i])

#display the number of vowels : numb_of_vowels
text_length = text_length - numb_of_punctuation
consonant_numb = text_length - numb_of_vowels
print("Your word has " + str(text_length) + " letters\n" + str(numb_of_vowels) + " vowels\n" + str(
    consonant_numb) + " consonants\n" + str(numb_of_punctuation) + " punctuations")


#Add a function that shows the most repetitive vowels or consonants
#First we create a function that count the occurrence of vowels : occurrence(myVowel)
def occurrence(my_vowel):
    numb_of_occurrence = 0
    numb_of_occurrence = user_text.count(my_vowel)
    return numb_of_occurrence


#display the occurrence number of each vowel
for i in range(len(tool.alphabet)):
    print(f"Occurrence of {tool.alphabet[i]} : {occurrence(tool.alphabet[i])}")

#Now display the most and less rated vowels
#algorithme to get the max and the min of iteration number list and the most and less rated vowel
# first : initialize the variable "higher_rate" with the first number of the list
#Do the same for the variable "lower_rate"

higher_rate = occurrence(tool.alphabet[0])
lower_rate = occurrence((tool.alphabet[0]))
#set the starting index to point to the second element of the list
start_index = 1
most_rated_vowel = "a"
# a for loop to loop through the vowels array to compare the iteration of each vowel
for i in range(start_index, len(tool.alphabet)):
    if occurrence(tool.alphabet[i]) > higher_rate:
        higher_rate = occurrence(tool.alphabet[i])
        # declare and initialize the variable "most_rated_vowel" to get the most rated vowel each time we find the
        # highest rate
        most_rated_vowel = tool.alphabet[i]

for i in range(start_index, len(tool.alphabet)):
    if occurrence(tool.alphabet[i]) < lower_rate:
        lower_rate = occurrence(tool.alphabet[i])
        less_rated_vowel = tool.alphabet[i]
#
print("---------------------------------------------------------------------------------------------")
print("The most rated letter is :" + most_rated_vowel + " with " + str(higher_rate) + " occurrences\n")
print("The less rated letter is :" + less_rated_vowel + " with " + str(lower_rate) + " occurrence\n")
