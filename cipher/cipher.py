from colorama import Fore, Back  #FOR COLORS
from art import logo
from art import bye
from letters import alphabet
print(Back.BLUE + Fore.BLACK + logo)
print("WELCOME TO THE CAESAR CIPHER PROGRAM")
restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(ps_text, ps_shift, ps_direction):
        cipher_array = []
        if ps_direction == "encode":
            for letter in ps_text:
                if letter in alphabet:
                    # create the variable position to return the index of the new coded letter
                    # assuming that position is higher than 25 or lower than zero
                    # we should restart and use the first or last letters of alphabet
                    position = (alphabet.index(letter) + ps_shift) % len(alphabet)
                    cipher_array.append(alphabet[position])
                else:
                    cipher_array.append(letter)
            cipher_text = ''.join(cipher_array)
            print(f"The encoded text is : {cipher_text}")
        elif ps_direction == "decode":
            ps_shift *= -1
            for letter in ps_text:
                if letter in alphabet:
                    # create the variable indices to return the index of the new coded letter
                    position = (alphabet.index(letter) + ps_shift) % len(alphabet)
                    cipher_array.append(alphabet[position])
                else:
                    cipher_array.append(letter)
            cipher_text = ''.join(cipher_array)
            print(f"The decoded text is : {cipher_text}")
        else:
            print("choice not available, make sure your entry is correct : encode or decode")

    caesar(text, shift, direction)
    will_is_yes = True
    while will_is_yes:
        will = input("Do you want to restart? ").lower()
        if will == 'yes':
            restart = True
            will_is_yes = False
        elif will == 'no':
            restart = False
            will_is_yes = False
        else:
            print("ERROR, Please type 'yes' or 'no' ")
print(bye)
