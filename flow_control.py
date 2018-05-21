#!/usr/bin/env python

# Flow control is a term for selectively choosing what "branches" of
# code to run conditionally and/or multiple times

# Functions

# While not strictly flow control, functions provide a way to segregate
# a portion of code.

# Functions are defined as follows.  def specifies we are defining a function;
# my_function is the name of our function, which must be unique
# inside the () will be the arguments; we'll cover this more when we get
# to functions specifically.  For now, just know that when you call a
# function, you pass in values to these arguments, which will be available
# inside the function as variables.
def my_function(my_arg):
	print("My arg is " + str(my_arg))

print("Trying out my_function()")

my_function("Turkey")
my_function(42)

print()
# I introduce functions here, because I'll use them below.

#----------------

# If statements
def do_if(x):
	if (x==1):
		# Do some code if conditional is True
		# Skips the rest of the code blocks in the if/elif/else statement
		print("Hello from my if statement!")
	elif (x==2):
		# If the original if was true, checks the second conditional
		# If true, runs, then skips all remaining codeblocks
		print("Hello from my elif statement!")
	else:
		print("Hello from my default code block!")

print("Trying out do_if()")

do_if(1)
# Prints the statement from the if block

do_if(2)
# Prints the statement from the elif block

do_if(42)
# Prints the statement from the else block

print()


def tricky_if(x):
	if (x>=1):
		print("x is bigger than one!")
	elif (x>=10):
		print("x is bigger than 10!")
	else:
		print("x is very sad")

print("Trying out tricky_if()")

tricky_if(5)
# This will print x is bigger than one

tricky_if(50)
# This will print x is bigger than one, because it's the first
# conditional it matched

tricky_if(0)
# This will tell us that x is very sad.

print()

#--------------------

# for loops
# Python differs from many languages in that for loops in python always
# iterate over a sequence.  This can be any iterable object.  Every for
# is similar to a "foreach" in other languages.

print("Counting some word lengths")

words = ['cat', 'window', 'defenestrate']

for word in words:
	print(word, len(word))

print()

# If you do need to iterate over a numerical range, there'a range() function

print("Iterating over a range")
for i in range(5):
	print(i)

print()

# while
# While loops continue until a given condition is no longer true

print("Trying out a while loop")
i = 0
while i < 5:
	print("i is " + str(i))
	i += 1

print()

# break / continue / else
# break and continue are tools you can use to modify when a loop exits
# or skips to the next iteration

# for loops can also have an else.  The else will be hit at the exhaustion
# of the iterable, or in this case, list, when used on a for loop.

# break statements terminate the innermost loop they are contained in, and
# do not cause an else clause to trigger.

# Try to explain the the break and else play together in this for loop to
# find prime numbers.
print("Trying out break with a for/else")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print()

# continue statements exit a given iteration of the loop early, to begin the
# next iteration sooner

print("Trying out continue")
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

print()

# https://docs.python.org/3/tutorial/controlflow.html
