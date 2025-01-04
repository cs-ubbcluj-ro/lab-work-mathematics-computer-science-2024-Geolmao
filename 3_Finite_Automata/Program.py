class FiniteAutomata:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.initial_state = None
        self.final_states = set()

    def loadFile(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("states:"):
                self.states = set(line[len("states:"):].strip()[1:-1].split(", "))
            elif line.startswith("alphabet:"):
                self.alphabet = set(line[len("alphabet:"):].strip()[1:-1].split(", "))
            elif line.startswith("transitions:"):
                self.transitions = {}
            elif line.startswith("initial:"):
                self.initial_state = line[len("initial:"):].strip()
            elif line.startswith("final:"):
                self.final_states = set(line[len("final:"):].strip()[1:-1].split(", "))
            elif line and ',' in line:  
                state, symbol, next_state = map(str.strip, line.split(","))
                if (state, symbol) not in self.transitions:
                    self.transitions[(state, symbol)] = []
                self.transitions[(state, symbol)].append(next_state)

    def display(self):
        print("Set of States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Transitions:")
        for (state, symbol), next_states in self.transitions.items():
            print(f"  δ({state}, {symbol}) -> {next_states}")
        print("Initial State:", self.initial_state)
        print("Final States:", self.final_states)

    def isValid(self, token):
        current_state = self.initial_state
        for symbol in token:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)][0]
            else:
                return False
        return current_state in self.final_states


if __name__ == "__main__":
    fa = FiniteAutomaton()
    fa.loadFile("FA.in")
    fa.display()

    #bonus
    test_string = input("Enter a string to validate: ")
    if fa.isValid(test_string):
        print(f"The string '{test_string}' is a valid token.")
    else:
        print(f"The string '{test_string}' is NOT a valid token.")
