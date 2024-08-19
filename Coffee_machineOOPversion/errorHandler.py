#personnalized exceptions to handle error of entry
class NonValidEntry(Exception):
    pass


def choose_right_option():
    print("WHAT DO YOU WANT : ", " ".join(possible_entry))
    choice = input("Report : to display the available resources of the machine\n"
                   "Off : to switch the machine off\n"
                   "Or simply a coffee name to enjoy ☕️\n")
    #Verify if the choice is in options list
    if choice not in possible_entry:
        raise NonValidEntry(f"The option {choice} is not a valid option")

    return choice


possible_entry = ["report", "off", "latte", "espresso", "cappuccino"]
