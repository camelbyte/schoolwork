import re
import random



def create_state_capital_dict(file_path):
    """ Open the text file and prepare the data.

    Params: takes a filepath as parameter, defined in 'Main'.

    Return: Returns a dictionary with the file data.

    """
    state_capital_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip()  
            city, state = line.split(', ')  
            state_capital_dict[state] = city
    return state_capital_dict

def learn_capitals(state_capital_dict):
    """
    Description: Uses a loop to continously prompt the user for a state, and checks it 
    against the respective dictionary key:value. User can start the quiz by typing 'quit'.

    Params: Dictionary we made above.

    Return: None

    """
    while True:
        state = input("Enter a state (or 'quit' to stop and start the quiz): ")
        if state.lower() == 'quit':
            break
        capital = state_capital_dict.get(state, "State not found")
        print(f"The capital of {state} is {capital}")

# Function to quiz user on the capitals
def quiz_user(state_capital_dict):
    """
    Desc: Set up a function to keep track on attempts, correct/incorrect. 

    Params: Dictionary 

    Return: None

    """
    states = list(state_capital_dict.keys())
    num_correct = 0
    num_incorrect = 0

    for _ in range(5):  # Quiz for 5 tries
        state = random.choice(states)
        capital = input(f"What is the capital of {state}? ")
        if capital.lower() == state_capital_dict[state].lower():
            print("Correct!")
            num_correct += 1
        else:
            print(f"Incorrect! The capital of {state} is {state_capital_dict[state]}")
            num_incorrect += 1

    print(f"Quiz over! You got {num_correct} correct and {num_incorrect} incorrect.")

def main():
    """
    Desc: Putting it all together into 1 function that I will call from 'Main'.

    Params: None

    Return: None
    """
    file_path = 'city_states.txt'
    state_capital_dict = create_state_capital_dict(file_path)
    
    print("Phase 1: Learn the Capitals")
    learn_capitals(state_capital_dict)
    
    print("\nPhase 2: Quiz on the Capitals")
    quiz_user(state_capital_dict)

if __name__ == "__main__":
    main()
