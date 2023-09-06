import numpy as np
import copy

class Node():
    def __init__(self, state, parent, action, heuristic):
        # Defining state, parent, action and heuristic function of node
        self.state = state 
        self.parent = parent
        self.action = action
        self.heuristic = heuristic

class StackFrontier():
    # Implementing Stack Data Structure 
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(np.array_equal(node.state, state) for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier.pop()
            return node

class gbfsFrontier(StackFrontier):
    # Implementing Greedy Best First Search Algorithm
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = min(self.frontier, key=lambda x: x.heuristic)
            self.frontier.remove(node)
            return node

class SquarePuzzle():
    def __init__(self, size, initial_state, goal_state):
        self.size = size
        self.initial_state = initial_state  # Input as a 2D numpy array
        self.goal_state = goal_state  # Input as a 2D numpy array

        # Validate initial and goal states
        if self.initial_state.shape != (size, size) or self.goal_state.shape != (size, size):
            raise Exception("Initial and goal states must have the correct shape.")

        self.solution = None
        self.exp=0 # number of explored states
        self.steps=0 # number of steps taken

    def print(self):
        if self.solution is not None:
            
            print("Solution:")
            for state in self.solution:
#                 print(state)
                self.steps+=1
            print(state)
            print('No of Explored States',self.exp+1)
            print('No of Steps Taken:',self.steps-1)
        else:
            print("No solution found.")

    def neighbors(self, state):
        zero_position = np.argwhere(state == 0)[0] # finding out the position of space in matrix
        row, col = zero_position[0], zero_position[1]
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        # finding valid actions that can be performed based upon the conditions
        for action, (r, c) in candidates:
            if 0 <= r < self.size and 0 <= c < self.size: # edge condition
                new_state = state.copy()
                new_state[row, col], new_state[r, c] = new_state[r, c], new_state[row, col]
                result.append((action, new_state))
        return result

    def solve(self):
        # heuristic function is number of elements in the wrong position at the current state
        heuristic_calc = np.sum(self.initial_state != self.goal_state)
        # Initialize frontier to just the initial state
        start = Node(state=self.initial_state, parent=None, action=None, heuristic=heuristic_calc)
        frontier = gbfsFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until a solution is found
        while True:
            # If nothing left in frontier, then no path
            if frontier.empty():
                return

            # Choose a node from the frontier
            node = frontier.remove()

            # If node is the goal, then we have a solution
            if np.array_equal(node.state, self.goal_state):
                solution = []
                while node.parent is not None:
                    solution.append(node.state)
                    node = node.parent
                solution.append(self.initial_state)
                solution.reverse()
                self.solution = solution
                return

            # Mark node as explored
            self.explored.add(tuple(map(tuple, node.state)))
            

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and tuple(map(tuple, state)) not in self.explored:
                    heuristic_calc = np.sum(state != self.goal_state)
                    child = Node(state=state, parent=node, action=action, heuristic=heuristic_calc)
                    frontier.add(child)

            self.exp +=1 # incrementing the number of explored states

if __name__ == '__main__':

    filename=input('Enter the location of text file:')
    with open(filename,'r') as file:
        lines=file.readlines()
        # Remove leading and trailing whitespace from each line
        lines = [line.strip() for line in lines]
        # Determine the number of rows and columns based on the length of lines
        num_rows = len(lines)
        num_cols = max(len(line) for line in lines)
        # Create a NumPy array with dimensions determined by the number of rows and columns
        initial_state = np.zeros((num_rows, num_cols), dtype=int)
        # Fill the array with the numbers from the lines
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char.isdigit():
                    initial_state[i, j] = int(char)
                else:
                # Replace spaces with the length of the matrix
                    initial_state[i, j] = num_cols**2 
   

    size = len(initial_state)
    # creating a deep copy of intial state and sorting it to make the goal state
    goal_state=copy.deepcopy(initial_state) 
 
    # Flatten the matrix into a 1D array
    flat_array = goal_state.flatten() 

    # Sort the 1D array
    sorted_array = np.sort(flat_array)

    sorted_array[sorted_array == size**2]=0

    # Reshape the sorted 1D array back into the original matrix shape
    goal_state = sorted_array.reshape(goal_state.shape)
    
    # replacing the max element with 0
    initial_state[initial_state == size**2]=0

    puzzle = SquarePuzzle(size, initial_state, goal_state)
    print('Unsolved Puzzle:')
    print(initial_state)
    puzzle.solve()
    print('Solved Puzzle:')
    puzzle.print()