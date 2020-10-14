# ResponseBot program for the command-line interface
# Desc:   This program simply grabs input from the user and 
#   asks the response bot for a response to the input. 
# Author: Amy Burnett
# Date:   2020/10/13
##########################################################################
# Imports

from responsebot import ResponseBot

##########################################################################
# Constants 

# Colors for printing variation
USER_PROMPT_COLOR  = "\033[1;34m"
BOT_PROMPT_COLOR  = "\033[1;32m"
ERROR_COLOR   = "\033[91m"
SUCCESS_COLOR = "\033[92m"
NORMAL_COLOR  = "\033[0m"

##########################################################################

# Runs a Read-Eval-Print-Loop for the user to continuously 
# send and receive messages to and from the responsebot
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
        print(USER_PROMPT_COLOR, "> ", NORMAL_COLOR, sep="", end="")
        try:
            user_input = input()
        # exit on EOF 
        except EOFError:
            print()
            exit()
        # dont exit with ctrl+c
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt");
            continue

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
        print(BOT_PROMPT_COLOR, "Bot> ", NORMAL_COLOR, response, sep="")

##########################################################################

if __name__ == "__main__":
    REPL()