# ResponseBot program for the command-line interface
# Desc:   This program simply grabs input from the user and 
#   asks the response bot for a response to the input. 
# Author: Amy Burnett
# Date:   2020/10/13
##########################################################################

from responsebot import ResponseBot

##########################################################################

def REPL():

    # Print welcome message 
    print("Welcome to the CLI ResonseBot program")
    print("Type anything below to see a response from the ResponseBot")
    print("You can exit the program by typing '/exit'")
    print("==========================================================")

    # Initialize resources
    responseBot = ResponseBot()

    while (True):

        # prompt user 
        print("> ", end="")
        try:
            user_input = input()
        # exit on EOF 
        except EOFError:
            print()
            exit()

        # trim input 
        user_input = user_input.strip()

        # reject empty input
        if user_input == "":
            continue

        # user entered exit command
        if user_input == "/exit":
            break

        # ask response bot for a response
        response = responseBot.respond(user_input)

        # print responseBot's response
        print("Bot>", response)

##########################################################################

if __name__ == "__main__":
    REPL()