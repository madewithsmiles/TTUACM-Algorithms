# Algorithm 1 : Using a stack
The goal of this algorithm is to try and keep track of the level of nesting that we are on.
We can do this by looking at the top of our stack when we hit a `)`. It is also assumed that
every given string is valid

1. Iterate through the string character-by-character
2. If the character is a `(`, append a 0 since it currently has a score of 0
3. If the character is a `)`, pop off the `(` to signify a match, then add 1 or 2 times the value at that level

TC/SC: O(n)

# Algorithm 2 : Counting the Cores
Given some time and thought, you realize that the final sum is powers of two. Every nested parenthesis
set will have its value multiplied by 2. We keep track of the nesting using `bal`. It is a lot easier
draw out than it is to describe in words.

TC: O(n)
SC: O(1)
