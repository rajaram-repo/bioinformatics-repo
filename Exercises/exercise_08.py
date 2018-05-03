"""
Exercise 8


1) Write a definition called 'compute' which takes in only **kwargs and meets the following specifications:
    - ensure that the key word 'input' is always be a list of integers before proceeding
    - if the key word 'action' is 'sum' then return the sum of all integers
    - if the key word 'action' is 'mean' then return  the mean of all integers
    - if the key word 'return_float' is 'True', then any return value should be a float

2) Implement an argument parser as a main function that meets the following requirements:
    - when run from terminal, your program should be able to accept any number of arguments
    - if -s is used, your program should print the sum of all arguments
        python3 exercise_08.py -s 1 5 20
        26
    - if -m is used, your program should multiply each value by the value of -m and print the result
        python3 exercise_08.py -m 5 1 5 20
        5
        25
        100
    - your program should also have descriptions and help attributes for each argument

"""
import sys
import argparse

def compute(**kwargs):
    if (kwargs['action'] == 'sum'):
        result = sum(kwargs['input'])
    elif (kwargs['action'] == 'mean'):
        result =sum(kwargs['input'])/len(kwargs['input'])
    else:
        result = "Please enter a valid name"

    # print(kwargs.get('return_float'))
    if (kwargs.get('return_float', False)):
        return (result)
        # return result
    return float(result)

# print(compute(action='sum', input=[0,1,2,3,2,1,0], return_float=True))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-m', '--multiply', help='', type=int)
    parser.add_argument('-s', '--sum', help='', action='store_true')
    parser.add_argument('remainder', help='', nargs=argparse.REMAINDER)

    # print("sjdbhjsdb")
    try:
        args = parser.parse_args()
        print(args)
        sum = 0
        mul = args.multiply
        if (args.sum == True):
            for i in args.remainder:
                sum = sum + int(i)
            print("The Sum is : ",sum)
        elif (args.multiply) :
            for i in args.remainder:
                mul = mul * int(i)
                print("The Multiplied value is : ",mul)
    except:
        parser.print_help()
        sys.exit(1)
