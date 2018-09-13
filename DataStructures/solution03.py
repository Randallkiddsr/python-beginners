#!/usr/bin/env python3

message = "The code for {} is {}."
airports = [ ("O’Hare International Airport", "ORD"),
             ("Los Angeles International Airport", "LAX"),
             ("Dallas/Fort Worth International Airport", "DFW"),
             ("Denver International Airport", "DEN") ]

for (name, abbreviation) in airports:
    print(message.format(name, abbreviation))