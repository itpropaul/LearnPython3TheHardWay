from sys import argv
script, cli_soup, cli_sandwich = argv

def one_more_function(soup, sandwich):
    print(f"Here's your delicious {soup} soup.")
    print(f"Your {sandwich} sandwich is an excellent choice.")
    print("Have a nice day.")

one_more_function("tomato", "ham")

one_more_function("tomato" + " and " + "cheese", "ham & " + "roast beef")

type_of_soup = "mushroom & chowder"
type_of_sandwich = "meat & the other meat"

one_more_function(type_of_soup, type_of_sandwich)

one_more_function(type_of_soup * 2, type_of_sandwich * 2)

user_sandwich = input("What type of sandwich would you like to eat?")
user_soup = input("What type of soup would you like to have?")

one_more_function(user_soup, user_sandwich)

print("Here's the input you gave at the command line:")
one_more_function(cli_soup, cli_sandwich)
