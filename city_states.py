import re

path = 'city_states.txt'


cs_dict = {}


with open(path, "r") as file:

    for line in file:

        city_states = line.strip().split(", ")
        city, state = city_states
        cs_dict[city] = state

print(state, "\t", city)
