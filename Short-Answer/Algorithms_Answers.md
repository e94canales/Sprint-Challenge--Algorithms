#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - This is dependent on input size, so as the input increases so does the amount, resulting in linear time


b) O(n log n) - There are two nested loops, but the inner loop runs independently from the outer loop


c) O(n) - This will run depending on n size, it will recurse with n -1 each time resulting in linear time

## Exercise II

Using a Binary Search Tree,

Declare the first drop at the midpoint of the building,
if the egg breaks return true,
recurse n - 1,
if the egg still doesn't break, recurse n + 1
if the egg doesn't break, return false,
recurse n + 1

O(n log n) - because each recurse is dividing in half