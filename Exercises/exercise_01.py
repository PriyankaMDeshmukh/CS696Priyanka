"""
Exercise 1
Place this script inside a new folder in your github repository called "Exercises".
This will be the directory for all of your in-class exercises this semester.

By the end of class on Thursday 1/25, students should have:
    - Created a private github repo for this class
    - Added their information to this sheet:
        https://docs.google.com/spreadsheets/d/1EKNYOqTnxelmBT4jqotRbUer5eVvWYM9RloN5doScyo/edit?usp=sharing
    - Added my github account (kylelevi) as a collaborator for their private repository
    - Completed these definitions and pushed this script to a folder called "Exercises" in their repo

"""

def hello():
    """
    Prints "Hello World"
    :return: None
    """
    print('Hello World')
    return

def percent_decimal(i):
    """
    Converts a percentage to a decimal or a decimal to a percentage depending on the input i
    :param i: a float between 0 and 100
    :return: a float between 0 and 100
    """
    conversion=0
    if i>=0 and i<=1:
        conversion=i*100
    else:
        conversion=i/100
    return conversion

def exponent(integer, power):
    """
    Using a loop (no imports!), raise the integer given to the power provided. (integer^power)
    :param integer: a positive, non zero, integer
    :param power: a positive, non zero, integer
    :return: an integer
    """
    expValue=1
    for i in range(0,power):
        expValue=expValue*integer
    return expValue

def complement(dna):
    """
    Returns the complement strand of DNA to the input.  C <--> G,  A <--> T
    :param dna: String containing only C, T, A, and G
    :return: String containing only C, T, A, and G
    """
    complement=""
    for c in dna:
        if c=='C':
            complement+='G'
        if c=='G':
            complement+='C'
        if c=='A':
            complement+='T'
        if c=='T':
            complement+='A'
    return complement


hello()
print(percent_decimal(.56))

print(exponent(4,2))
print(complement("CGAT"))
