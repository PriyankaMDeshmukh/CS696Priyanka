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

def my_sum(input):
    return sum(input)

def my_mean(input):
    return my_sum(input)/len(input)

def all_int(input):
    return all(isinstance(item, int) for item in input)


switch_dict = {
    'sum': my_sum,
    'mean': my_mean,
    'all_int': all_int
}

def compute(**kwargs):
    if switch_dict['all_int'](kwargs['input']):
        if kwargs['action']=='sum':
            result = switch_dict['sum'](kwargs['input'])
        elif kwargs['action']=='mean':
            result = switch_dict['mean'](kwargs['input'])
        if ('return_float' in kwargs) and kwargs['return_float']== True:
            return float(result)
        else:
            return result
    else:
        return "Please input only integers"
print(compute(input = [0,1,2,3],action='mean', return_float=True))
print(compute(input = [0,1,2,3],action='sum'))
print(compute(input = [0,1,2,3],action='sum', return_float=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Program to multiply or add integers in a list')
    parser.add_argument('-m', '--multiply', help='use -m or --multiply for multiplying all integers in list.', type=int)
    parser.add_argument('-s', '--sum', help='use -s or --sum for adding all integers in list.', action='store_true')
    parser.add_argument('remainder', help='', nargs=argparse.REMAINDER,type=int)

    try:
        args = parser.parse_args()
        if args.sum:
            print("Sum of all the integers is:",compute(input=args.remainder, action='sum'))
        if args.multiply:
            a=[i*args.multiply for i in args.remainder]
            print("Multiplication of all integers with given integer yields: ")
            for i in a:
                print(i)
    except:
        parser.print_help()
        sys.exit(1)
