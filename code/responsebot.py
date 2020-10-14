# ResponseBot program
# Desc:   This program acts as the core to the response bot.
#   This accepts input and uses other modules to generate and
#   return a response for the input. 
# Author: Amy Burnett
# Date:   2020/10/13
##########################################################################
# Imports 

from sanitizer import Sanitizer

##########################################################################

class ResponseBot:

    def __init__(self):
        self.sanitizer = Sanitizer()

##########################################################################

    def respond(self, user_input:str):

        # tokenize input
        print("=== Tokenizing Input ==============")
        words = user_input.split()
        print("words =>", words)

        # sanitizing input
        print("=== Sanitizing Words ==============")
        clean_words = self.sanitizer.sanitize(words)
        print(clean_words)

        return "I am but an empty mind!"

##########################################################################