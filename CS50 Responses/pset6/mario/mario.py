# Prints out a pyramid from Mario, according to a given height

# get_int required for error-checking input
from cs50 import get_int

# Global variables
gap = "  "
air = " "
block = "#"
spaces = 0


# Runs mario.c recursively
def recursively(height):
    # Makes global variable 'spaces' visible, and modifiable within function
    global spaces
    
    # Base case that terminates recursive calling, and prints the first line in the pyramid
    if height == 1:
        for space in range(spaces):
            print(air, end="")
        print(block, end="")
        print(gap, end="")
        print(block)
        
    # Recursively prints preceding lines, before printing current line
    else:
        spaces += 1
        recursively(height - 1)
        spaces -= 1
        for space in range(spaces):
            print(air, end="")
        for blocks in range(height):
            print(block, end="")
        print(gap, end="")
        for blocks in range(height):
            print(block, end="")
        print()


# Runs mario.c iteratively
def iteratively(height):
    # Iterates through entire height of tree
    for i in range(1, height + 1):
        
        # Prints empty spaces representing air
        for spaces in range(height - i):
            print(air, end="")
        # Prints blocks
        for blocks in range(i):
            print(block, end="")
        # Prints gap
        print(gap, end="")
        # Prints blocks
        for blocks in range(i):
            print(block, end="")
        # Prints newline
        print()


# Main function
def main():
    while True:
        # get_int() handles error checking for inputs that are not type int
        height = get_int("Height: ")
        if height > 0 and height <= 8:
            break

    # Alternative function: iteratively(height) 
    recursively(height)


# Runs main()
main()