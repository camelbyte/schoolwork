import re


path = "city_states.txt"


def load_valid_inputs(path):
    with open(path, 'r') as file:
        return {line.strip().lower() for line in file}


with open(path, "r") as file:
    data = file.read()
    print(data)
    
    data.rstrip("'")
    
    
    city_states = data.splitlines()
    
    clean_data = [c.replace(",", "").replace("'", "") for c in city_states]
    print(clean_data)



