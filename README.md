# KnapsackAlgorithm
# Knapsack Problem Solver

This code implements a dynamic programming approach to solve the knapsack problem. The knapsack problem aims to maximize the total value of items placed into a knapsack with a limited capacity.

The code defines a function called `knapsackFunction` that takes values, weights, and capacity as inputs and returns the maximum value achievable and the weights of the items used.

The program reads the data from the "veriler.txt" file, which contains three lines:
- The first line contains a comma-separated list of values.
- The second line contains a comma-separated list of weights.
- The third line contains the knapsack capacity as an integer.

To use the code:
1. Clone the repository to your local machine:
https://github.com/HarunSekerci/KnapsackAlgorithm.git
2. Enter the appropriate data in the "data.txt" file to specify the values, weights, and capacity.
3. Run the code:
The program will output the maximum value and the weights of the items used in the knapsack.

This code provides a solution to the knapsack problem using dynamic programming. It allows for easy customization of the input data and can be used as a starting point for solving similar optimization problems.

Data Format

The program reads data from the "veriler.txt" file. The file should have the following format:
<values>
<weights>
<capacity>
Values: A comma-separated list of values.
Weights: A comma-separated list of weights.
Capacity: An integer representing the capacity of the knapsack.

Output
The program displays the maximum value achieved and the weights of the selected items.

Sample output => 
Maximum value: 150
Used weights: 10, 20, 30
