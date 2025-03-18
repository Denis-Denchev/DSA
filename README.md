# Data Structures and Algorithms (DSA) with Python

Welcome to my DSA repository! This repository contains implementations of various data structures and algorithms in Python. Here, I will submit and document solutions for different DSA tasks and problems, showcasing both basic and advanced concepts.

## Table of Contents

- [Introduction](#introduction)
- [Technologies](#technologies)
- [Structure of the Repository](#structure-of-the-repository)
- [Recursive Factorial](#recursive-factorial)
- [Recursive Fibonacci](#recursive-fibonacci)
- [Recursive Reverse List](#recursive-reverse-list)
- [Recursive Sum of Numbers](#recursive-sum-of-numbers)
- [How to Run the Code](#how-to-run-the-code)
- [License](#license)

## Introduction

This repository is aimed at practicing and implementing various data structures and algorithms using Python. The goal is to provide a comprehensive understanding of core principles in computer science, such as recursion, searching, sorting, and basic data structures. In this repository, I focus primarily on recursive solutions to common problems.

The implementation examples in this repository cover tasks like calculating factorials, generating Fibonacci numbers, reversing lists, and summing numbers. Each section provides a clear, recursive solution to the task at hand.

## Technologies

- **Programming Language**: Python 3.13
- **Libraries**: None required (all implementations are written using basic Python constructs)

## Structure of the Repository

The repository is organized as follows:

- **Recursive Factorial**: A recursive approach to calculating the factorial of a number.
- **Recursive Fibonacci**: A recursive implementation of the Fibonacci sequence.
- **Recursive Reverse List**: A recursive solution to reverse a list.
- **Recursive Sum of Numbers**: A recursive function that computes the sum of a list of numbers.

### Recursive Factorial

This section demonstrates the calculation of the **factorial** of a number using recursion. The factorial of a number `n` is defined as the product of all positive integers less than or equal to `n`.

- **Base Case**: If `n` is less than or equal to 1, the result is 1.
- **Recursive Case**: The function calls itself, multiplying `n` by the factorial of `n-1`.

### Recursive Fibonacci

The **Fibonacci sequence** is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. This section demonstrates a recursive implementation of the Fibonacci sequence.

- **Base Case**: If `n` is 0 or 1, the result is `n`.
- **Recursive Case**: The function calls itself for `n-1` and `n-2`, and returns their sum.

### Recursive Reverse List

This function reverses a list using recursion. The list is broken down recursively, and elements are reassembled in reverse order.

- **Base Case**: If the list is empty, the function returns an empty list.
- **Recursive Case**: The function takes the first element, calls itself recursively for the rest of the list, and then appends the first element to the result.

### Recursive Sum of Numbers

This function calculates the sum of a list of numbers recursively. It adds the first element of the list to the sum of the remaining elements.

- **Base Case**: If the list is empty, the sum is 0.
- **Recursive Case**: The function adds the first element to the sum of the remaining elements in the list.

## How to Run the Code

To run the code in this repository:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/DSA-With-Python.git
