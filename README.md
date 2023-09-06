# Sliding-Puzzle-Solver

A python program implementing any Search strategy to solve the arrange square puzzle.

![image](https://miro.medium.com/v2/resize:fit:1400/1*W7jg4GmEjGBypd9WPktasQ.gif)

This Python script is designed to solve a square puzzle using the Greedy Best First Search (GBFS) algorithm. The puzzle consists of a grid with numbers, and the goal is to rearrange the numbers to reach a specific target configuration. This README provides an overview of the script's functionality and usage.


## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [File Input](#file-input)
- [Implementation Details](#implementation-details)
- [Example](#example)

## Introduction

The Python script includes the following components:

The Python script includes the following components:

1. `Node` class: Represents a node in the puzzle-solving process. It stores the current state, parent node, action taken, and a heuristic value.

2. `StackFrontier` class: Implements a stack data structure for managing the frontier nodes during the search process.

3. `gbfsFrontier` class: Extends `StackFrontier` to implement the Greedy Best First Search algorithm by selecting nodes with the lowest heuristic value.

4. `SquarePuzzle` class: Manages the square puzzle solving process. It includes methods for finding neighbors, solving the puzzle, and printing the solution.
5. Heuristic Function:
Number of Misplaced Tiles: This heuristic counts the number of tiles that are out of place in the current state compared to the goal state.
It considers the correctness of each tile's position independently.


## Prerequisites

Before using this script, ensure you have the following:

- Python 3 installed on your system.
- `numpy`: You can install it using pip:
- `copy`: This library is included in Python's standard library, so no separate installation is required.

## Usage

To use the script, follow these steps:

1. Run the script using Python 3.

2. You will be prompted to enter the location of a text file containing the initial puzzle configuration. The text file     should have the following format:  
681  
473  
5 2
  - Use numbers to represent the puzzle tiles.
  - Use spaces or tabs to separate the numbers.
  - Replace the empty space with the number `0`.

3. The script will then display the unsolved puzzle and proceed to solve it using the Greedy Best First Search algorithm.

4. Once the puzzle is solved, the script will display the solved puzzle, the number of explored states, and the number of steps taken to reach the solution. 

## File Input

The script reads the initial puzzle configuration from a text file. The provided text file should contain a valid puzzle configuration as described in the Usage section. You can create your own puzzle configurations in text files and provide the file path when prompted.

## Implementation Details

- The script uses the Greedy Best First Search (GBFS) algorithm to solve the puzzle. The heuristic used is the count of the number of elements in the wrong position in the current state compared to the goal state.

- The `Node` class stores information about each state, including its parent state, action taken to reach it, and the heuristic value.

- The `StackFrontier` class implements a stack for managing nodes in the search process.

- The `SquarePuzzle` class manages the solving process, finding neighbors, and printing the solution.


## example
Example Testcases for the code is been uploaded as 'one.txt' and 'two.txt' files in the repository
