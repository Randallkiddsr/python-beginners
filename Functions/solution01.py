#!/usr/bin/env python3

def askWords():
    """Asks the user for three strings. Returns the words in a list."""

    noun = input("Please enter a noun: ")
    verb = input("Please enter a verb: ")
    adjective = input("Please enter an adjective: ")

    return [verb, adjective, noun]

def fillWords(story, verb = "", adjective = "", noun = ""):
    """Fills in the placeholders in a given String."""

    return story.format(verb, adjective, noun)

# For example: "I open a large box."
story = "I {} a {} {}."

# Enter: "Box", "open" and "large"!
words = askWords()
completedStory = fillWords(story, words[0], words[1], words[2])

print(completedStory)

