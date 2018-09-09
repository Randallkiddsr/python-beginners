#!/usr/bin/env python3
def iterate_dict(dict):
    print()
    for key in dict:
        print("{}: {}".format(key, dict[key]))

people = { "Jeff": "Is afraid of clowns.",
           "David": "Plays the piano.",
           "Jason": "Can fly an airplane." }

iterate_dict(people)

people["Jill"] = "Can hula dance."

iterate_dict(people)

