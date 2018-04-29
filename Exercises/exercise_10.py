"""
Exercise 10 - Generators

For this exercise you will be writing a class for several different generator functions.

1) Write a class called "Gens".
    - This class is initialized with a single integer that is called "start"
    - Include a __str__() method so that when an instance of your class is printed, the returned string includes the value of "start"
        EX: "Start value for generators class is: 5"
    - All generator methods should start at the "start" value, if one is not provided, the class should default to a start value of 1

2) Include in this class, the following methods:
    doubles() - yields number * 2 to infinity, starting at self.start
        Gens(1).doubles() -> 1, 2, 4, 8, 16, ...

    fib() - Yields the next number in the fibonacci sequence to infinity, starting at 1
        Gens(100).fib() -> 1, 1, 2, 3, 5, 8, ...

    linear(n) - yields number + n to infinity, starting at self.start
        Gens(1).linear(2) -> 1, 3, 5, 7, 9, ...

    exponential(n) - yields number raised to the power n to infinity, starting at self.start
        Gens(2).exponential(2) -> 2, 4, 16, 256, ...

    sequence(list) - Ignores starting number, yields one value at a time in the list, looping infinitely many times
        Gens(0).sequence([2, 3, 4]) -> 2, 3, 4, 2, 3, 4, ...

    triple_half() -  Yields a number * 3, then the number / 2, repeating to infinity, starting at self.start
        Gens(2).triple_half() -> 2, 6, 3, 9, 4.5, 13.5, ...

"""
class Gens:

    def __init__(self,start=1):
        self.start=start

    def __str__(self):
        return "Start value for generators class is: {}".format(self.start)

    def double(self):
        i = self.start
        yield i
        while(True):
            yield i*2
            i=i*2

    def fib(self):
        fib1=0
        fib2=1
        while True:
            yield fib2
            temp=fib1
            fib1=fib2
            fib2=temp+fib2

    def linear(self,n):
        num=self.start
        yield num
        while True:
            num=num+n
            yield num

    def exponential(self,n):
        num = self.start
        yield num
        while True:
            num = num**n
            yield num

    def sequence(self,list):
        while True:
            for i in list:
                yield i

    def triple_half(self):
        num=self.start
        yield num
        while True:
            yield num*3
            num=num*3
            yield num/2
            num=num/2





