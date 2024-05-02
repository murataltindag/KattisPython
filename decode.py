"""
decode.py
Author: Murat Altindag
Date: 2024-04-23

This module contains functions for decoding messages from files.
"""

import math


def reverse_triangle(x):
    """
    Given a number x, this function calculates the number n such that x = n(n+1)/2.
    
    Parameters:
    x (int): The input number.

    Returns:
    float: The number n such that x = n(n+1)/2. 
    If x is not a triangle number, the return value will not be an integer.
    """
    
    # Calculate n using the quadratic formula
    n = (-1 + math.sqrt(1 + 8*x)) / 2 
    return n

def decode(message_file):
    """
    This function decodes a message from a file. The file should contain lines of the message
    in the format "x word", where x is a triangle number and word is a word in the message. 
    The position of each word in the message is determined by the integer n such that x = n(n+1)/2.
    
    The file may contain other lines with numbers that are not triangle numbers. These lines will be ignored.
    
    Parameters:
    message_file (str): The name of the file containing the message.

    Returns:
    None
    """
    # Open the file
    f = open(message_file, "r")
    
    # Read all lines from the file into a list
    lines = f.readlines()
    
    # Close the file
    f.close()
    
    # Calculate the size of the message
    message_size = int(reverse_triangle(len(lines)))
    
    # Create a list to store the message
    message = [""] * (message_size + 1)
    
    # For each line in the file
    for word in lines: 
        # Calculate the index of the word in the message
        index_float = reverse_triangle(int(word.split()[0])) 
        # If the index is an integer
        if(index_float.is_integer()): 
            # Convert the index to an integer (0-based)
            index = int(index_float) - 1 
            # Add the word to the message list
            message[index] = word.split()[1]
            
    # return " ".join(message) # Return the message as a string
    print(" ".join(message)) # Print the message

decode("coding_qual_input.txt")
