#!/usr/bin/env python3
lines = []

try: 
    with open("animals.txt") as source_ref:
        for line in source_ref:
            lines.append(line.rstrip())
except:
    print("Reading from animals.txt has failed.")

lines.sort()

try:
    with open("animals-sorted.txt", "w+") as target_ref:
        for line in lines:
            target_ref.write(line + "\n")
    print("\nFile 'animals-sorted.txt' has been created and written.")
except:
    print("Writing to file animals-sorted.txt has failed.")