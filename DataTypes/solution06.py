#!/usr/bin/env python3
miles = int(input("How far would you like to travel in miles? "))
answer = "I suggest {} to the destination."

if miles < 3:
    print(answer.format("walking"))
elif miles >= 3 and miles < 300:
    print(answer.format("driving"))
else:
    print(answer.format("flying"))