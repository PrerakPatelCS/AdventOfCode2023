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

Shoelace Theorem - Finds the area of a simple polygon by doing a cross product
on all the vertices. Get all the coordinates in clockwise or counterclockwise
fashion from point A all around back to A.

$$
A = \frac{1}{2} \left| \sum_{i=1}^{n-1} (x_i y_{i+1} - x_{i+1} y_i)\right|
$$

Pick's Theorem

Gets the area of a lattice simple polygons whose vertices are points on a grid.
Need to count the number of lattice points:
b = number of lattice points on boundary
i = number of lattice points on inside
$$
A = \frac{b}{2} + i - 1
$$

Shoelace + Pick's theorem

To get the whole space a polygon occupies we use these in conjunction.
The whole space is the area inside and the circumference 
A = Area 
C = circumference
$$
S = A + \frac{C}{2} + 1
$$

RayCasting

Pick a coordinate and to check if it is inside the polygon by
checking how many times if you look at it from a ray perspective like a laser
going forward, how many times it crosses the polygon. If it is odd it is 
inside, even outside. There is a special case for vertices you cross you need
to check there the 2 sides of the vertex is going.

Scanline

Same thing as raycasting but you can get the area of a polygon by 
analyzing each line and finding which coordinates are inside via
how many times you cross the polygon. The vertices are tricky here as well.

## Some Tricks I learned

Learned some good python coding tricks

A really cool way to change direction with Complex numbers instead of tuples 
so when you want to change directions you can just add by the Complex number
and still have the pair. The logic goes like this.

Each coordinate in a map has X, Y and each complex number has 2 components
as well a real and imaginary number. So use real as X and imaginary as Y.

