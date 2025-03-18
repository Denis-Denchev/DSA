# Data Structures and Algorithms (DSA) with Python

Welcome to my DSA repository! This repository contains implementations of various data structures and algorithms in Python.
Here, I will submit and document solutions for different DSA tasks and problems, showcasing both basic and advanced concepts.

## Table of Contents

- [Introduction](#introduction)
- [Technologies](#technologies)
- [Structure of the Repository](#structure-of-the-repository)
- [Binary search tree](#binary-search-tree)
- [How to Run the Code](#how-to-run-the-code)


## Introduction

This repository is aimed at practicing and implementing various data structures and algorithms using Python. The goal is to provide a comprehensive understanding of the core principles of computer science, such as searching, sorting, tree structures, graph traversal, dynamic programming, etc., with hands-on code examples.

## Technologies

- **Programming Language**: Python 3.13
- **Libraries**: None required (all implementations are written using basic Python constructs)

## Structure of the Repository

The repository is organized as follows:

##Binary search tree

Binary Search Tree (BST) Implementation
In this file, I have implemented a Binary Search Tree (BST), which is a fundamental data structure for efficiently storing and searching data. The tree supports the insertion of values and provides various traversal methods for exploring the tree in different ways. Below are the key features and explanations of the code:

1. TreeNode Class
The TreeNode class defines the structure of a node in the binary tree. Each node contains:

value: The value stored in the node.
left and right: Pointers to the left and right child nodes.
data: Optional additional data associated with the node.
2. Insert Method
The insert method is used to add values into the tree. It follows the BST property where:

Values less than the node value are inserted into the left subtree.
Values greater than the node value are inserted into the right subtree.
This method ensures that the tree remains sorted as values are added.

3. Traversal Methods
The tree supports three types of tree traversal methods:

Inorder Traversal (inorder_traversal):

This method visits nodes in ascending order, making it ideal for displaying the sorted sequence of values stored in the tree.
The method first visits the left child, then the node itself, and finally the right child. This results in an ordered output.
Example output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15.
Post-order Traversal (post_order):

This method visits the left child, then the right child, and finally the node itself. It is often used for operations like deletion or tree cleanup since it ensures the children are processed before the node.
Pre-order Traversal (preorder_traversal):

This method first visits the node, then recursively visits the left and right subtrees. It is commonly used for operations like tree cloning or copying the structure of the tree.
4. Find Method
The find method searches for a node with a specific value in the tree. If the value is found, it returns the node containing that value. If the value is not found, it returns None. This method efficiently traverses the tree based on the BST properties.
