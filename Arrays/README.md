# Data-Structures And Algorithms


### 01. Greedy Algorithms: Optimal Task Assignment

    Assign tasks to workers such that the time it takes to complete all tasks is minimized.
    here, the elements in an array is duration of time

### 02. Sorting Algorithms: Intersection of Two Sorted Arrays

    Given two arrays, A and B, determine their intersection. That is, what elements are common to A and B?


### 03. Binary Search: Find Closest Number

    given a sorted array and a target number. we need to find a number in the array that is closest to the target number.

    The array may contain duplicate values and negative numbers.

    Example 1:
        Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
        Target number = 11
        Output : 9
        9 is closest to 11 in given array

    Example 2:
        Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
        Target number = 4
        Output : 5

### 04. Binary Search: Find Fixed Point

    A fixed point in an array "A" is an index "i" such that A[i] is equal to "i".

    Given an array of n distinct integers sorted in ascending order, write a function that returns a "fixed point" in the array. If there is not a 
    fixed point return "None".

    Problem is to find only one fixed point.

    Examples:
        # Fixed point is 3:
        A = [-10, -5, 0, 3, 7]

        # Fixed point is 0:
        A = [0, 2, 5, 8, 17]

        # No fixed point. Return "None":
        A = [-10, -5, 3, 4, 7, 9]

### 05. Binary Search: Find Bitonic Peak

    Define a bitonic sequence as a sequence of integers such that:
        x_1 <= ... <= x_k >= ... >= x_n-1 for some k, 0 <= k < n.

    For example:
        1, 2, 3, 4, 5, 4, 3, 2, 1

    is a bitcoin sequence. write a program to find the largest element in
    such a sequence. In the above example, the program should return "5".

    we assume that such a peak element exists.

### 06. Binary Search: Find First Entry in List with Duplicates

    writing a function that takes an array of sorted integers and a key and returns the index of the first occurrence of that key from the array.

    Example:
        Index:      0   1   2   3    4    5    6    7    8    9
        Array:   [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        Target:  108

        Returns index 3 since 108 appear for the first time at index 3.

### 07. Arrays: Array Advance Game

    "array advance game"

    you are given an array of non-negative integers. For example:
    
    [3,3,1,0,2,0,1].

    Each number represents the maximum you can advance in the array. 

    Question:
    Is it possible to advance from the start of the array to the last element?

### 08. Arrays: Arbitrary Precision Increment

    Given:
        An array of non-negative digits that represent a decimal integer.

    Problem:
        Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.

### 09. Binary Search: Cyclically Shifted Array

    An array is "cyclically sorted" if it is possible to cyclically shift
    its entries so that it becomes sorted.

    The following list is an example of a cyclically sorted array:

        A = [4, 5, 6, 7, 1, 2, 3]

    Write a function that determines the index of the smallest element
    of the cyclically sorted array.

### 10. Arrays: Two Sum Problem

    Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

### 11. Arrays: Buy and Sell Stock

    Problem:
        Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made from buying on one day and selling on another day.

        We consider two approaches to this problem. In the first, we consider a brute force approach that solves the problem in O(N^2), where N is the size of the array of numbers. We then improve upon this solution to take our solution to a time complexity of O(N).


