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
    print('Hello World')
    """
    Prints "Hello World"
    :return: None
    """
print('1.Program1->Hello World')
hello()
def percent_decimal(i):
    if i>1:
        print('percent to decimal')
        i=i/100
    elif i>100:
        print("The value you entered is out of range << greater than 100")
    elif i<0:
        print("The value you entered is out of range << less than 0")
    else:
        print('decimal to percent')
        i=i*100
    """
    Converts a percentage to a decimal or a decimal to a percentage depending on the input i
    :param i: a float between 0 and 100
    :return: a float between 0 and 100
    """
    return i
print('2.Program2->percent/decimal Conversion')
result_i=percent_decimal(104)
print('For input 104 the o/p is:',result_i)
def exponent(integer, power):
    temp=integer;
    for x in range(power-1):
        integer=integer*temp
    """
    Using a loop (no imports!), raise the integer given to the power provided. (integer^power)
    :param integer: a positive, non zero, integer
    :param power: a positive, non zero, integer
    :return: an integer
    """
    return integer
print('3.Program3->Exponent Function')
result_exponent=exponent(5,4)
print('For input 5,4 the o/p is:',result_exponent)
def complement(dna):
    str = ''
    for char in dna:
        if char == 'C':
            str = str + 'G'
        elif char == 'G':
            str = str + 'C'
        elif char == 'A':
            str = str + 'T'
        elif char == 'T':
            str = str + 'A'
        else :
            str = 'invalid character entered, please check the input'
            break
    """    Returns the complement strand of DNA to the input.  C <--> G,  A <--> T
    :param dna: String containing only C, T, A, and G
    :return: String containing only C, T, A, and G
    """
    return str
print('4.Program4->Complement Function')
result_complemet=complement('ACTG')
print('For input ACTG the o/p is :',result_complemet)
