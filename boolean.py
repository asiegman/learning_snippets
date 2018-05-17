#!/usr/bin/env python

# Truth in python means the built-in boolean True, or a non-zero, non-None value
# False means zero, none, or the boolean False
# "Truthiness" may vary from language to language, but boolean logic does not
true = True
true = bool(17)
true = bool(-1.25)

false = bool(None)
false = bool(0)
false = False


# 'and' operations must both be True or non-zero to equate to True
true = True and True
false = True and False
false = False and False
false = False and True

# 'or' operations must have one or the other "True"
false = False or False
true = True or False
true = False or True

# boolean operations go from inside to outside of (), and left to right
true = True and False or True
# work: (True and False) or True
#          False or True
#              True
false = True and False and True
# work: (True and False) and True
#            False and True
#                 False

# Using paranthesis () can help clarify things if you want something to
# evaluate first, just like order of operations in math
true = True or (False and True)
# work:   True or (False)
# work:        True


# Be explicit, wrap things in () if it helps readability
# This prevents unintended order-of-operations bugs
boolean = (2 <= 2) and ("Alpha" == "Bravo")
# work: boolean = (True) and (False)
# work: boolean = False

