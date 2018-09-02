#!/usr/bin/env python3
kilometer = int(input("How far would you like to travel in miles? "))
answer = "I suggest {} to the destination."

if kilometer < 3:
    print(answer.format("walking"))
elif kilometer >= 3 and kilometer < 300:
    print(answer.format("driving"))
else:
    print(answer.format("flying"))