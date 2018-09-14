#!/usr/bin/env python3

def say_something():
    user_input = input("\nWhat would you like the cat to say? ")
    print("{0:10}{1}".format(" ", "_" * 20))
    print("\n{0:11}{1}\n".format("", user_input))
    print("{0:10}{1}".format(" ", "-" * 20))
    print("{0:9}{1}".format(" ", "/"))
    print("{0:2}{1}{2}{3}{4}{5}".format(" ", "/", "\\", "_", "/", "\\"))
    print("{0}".format(" ( o.o )"))
    print("{0}".format("  > ^ <"))

if __name__ == "__main__":
    say_something()