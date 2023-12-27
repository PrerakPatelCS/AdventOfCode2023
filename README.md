# Advent Of Code 2023

This is a 25 day puzzle calender. Every day a new puzzle comes out at midnight from the first of
December to Christmas. Once you solve the puzzle part 2 is revealed. The creator of the puzzles
wants to introduce new concepts from different industries and makes every day harder and harder.
The puzzle inputs are text from a text file you have to parse through.

# Concepts Per Day

1. String Matching algorithms like KMP and Rabin karp for finding 'one' - 'nine' in a string
2. Getting used to parsing file input, easy problem
3. More parsing a bit harder, numbers in a matrix
4. Parsing and brute force
5. Intervals going through a graph
6. Binary Search, sort of Math or Physics for when the speed accelerates past a threshold and comes back
7. Sorting poker hands
8. LCM going through a graph and there are many cycles
9. Get the next number in a pattern, geometric pattern
10. Geometry Algorithm - Pick's theorem, Shoelace formula, scanline
11. Prefix Sum
12. All possible outcomes, Back tracking and dynamic programming
13. Reflection, Palindrome
14. Simulation
15. Parsing and mapping
16. laser and mirrors, Multi source traversal
17. Path finding, Augmented Dijkstra's or A*
18. Geometry Algorithm - Pick's theorem, Shoelace formula, scanline
19. Intervals and maps 
20. 
21. Simulation plus math, Tiling
22. Jenga
23. Find longest path, Binary Search
24. 
25. 


## Learning the geometry algorithms

There are many algorithms like flood fill, Shoelace theorem, Pick's theorem,
Ray Casting, and ScanLine

Flood fill - A BFS algorithm filling the area until you hit a border.
For Day 10 and 18 this is not good enough the problem is more complex
or too big

Shoelace Theorem - Get all the coordinates in clockwise or counterclockwise
fashion from point A all around back to A, multiply the first X1 by Y2
in a cross fashion for all X. Subtract that by the sum of cross products
Y1 * X2. Now divide that by 2 and you have the area of the polygon.

$$
\[
A = \frac{1}{2} \left| \sum_{i=1}^{n-1} (x_i y_{i+1} - x_{i+1} y_i) + x_n y_1 - x_1 y_n \right|
\]
$$

