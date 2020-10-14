# ResponseBot program
# Desc:   This file handles sanitizing user input to remove things like 
#    punctuation and break up contractions 
# Author: Amy Burnett
# Date:   2020/10/13
##########################################################################
# Imports

import json

##########################################################################

VALID_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/-"

##########################################################################

class Sanitizer:

    def __init__(self, shouldMakeLowercase=True, shouldRemovePunctuation=True, shouldBreakUpContractions=True):
        self.shouldMakeLowercase = shouldMakeLowercase
        self.shouldRemovePunctuation = shouldRemovePunctuation
        self.shouldBreakUpContractions = shouldBreakUpContractions
        # load known contractions
        with open("contractions.json", "r") as file:
            self.contractions = json.load(file)

    def sanitize(self, words):
        newwords = words
        # make every word lowercase
        if self.shouldMakeLowercase:
            newwords = self.makeLowerCase(newwords)
        # break up known contractions
        if self.shouldBreakUpContractions: 
            newwords = self.breakUpContractions(newwords)
        # Remove any punctuation
        if self.shouldRemovePunctuation:
            newwords = self.removePunctuation(newwords)
        return newwords

    def makeLowerCase(self, words):
        newwords = []
        for word in words:
            newwords += [word.lower()]
        return newwords 

    def breakUpContractions(self, words):
        # break up contractions
        newwords = []
        for word in words:
            if word in self.contractions:
                newwords += self.contractions[word]
            else:
                newwords += [word]
        return newwords

    def removePunctuation(self, words):
        newwords = []
        for word in words:
            newword = ""
            for c in word:
                if c in VALID_CHARS:
                    newword += c
            newwords += [newword]
        return newwords

##########################################################################