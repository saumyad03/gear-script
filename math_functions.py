# Tells if a number is an integer (True) or not (False)
# is_integer() queries the datatype the variable is stored at, and was throwing annoying errors when used instead
# This function compares the content of the variable to an integer version of the variable.
def is_int(x):
    return (int(x) == x)


# Tells if a number is a natural number (True) or not (False)
# To change where natural numbers
def is_natural(n):
    k = 1  # "beginning" of natural numbers, typically 1 or 0. k must be included in natural numbers
    return is_int(n) and int(n) >= int(k)


# Returns string "GOOD" if natural number, "NOT A NATURAL NUMBER" if something else
def print_natual_num(n):
    return ("GOOD" if is_natural(n) else "NOT A NATURAL NUMBER")


# Checks if e is even
def is_even(e):
    return is_int(e / 2)

# All numbers representable as floating points are rational numbers. \
# Saying that the result needs to be a rational number is vacuous, in the sense that even if an irrational number like
#   pi or e is entered as one of the parameters, it will be (or has already been) truncated to a finite precision as a
#   binary number.
# As a reminder, a binary number is written as a sum of powers of two times an integer coefficient less than 2 (0 or 1).
# The finite addition of rational numbers will always result in a rational number, so any finite binary representation,
#   such as IEEE floating point, must be expressible as a ratio of two numbers.
# However, we wouldn't consider a number like 0.123456789 (or 123456789/1000000000) as an acceptable ratio because the
#   integers in the numerator and denominator are enormous, implying tiny gear teeth.
# Thus, this function takes in a maximum number of teeth and returns True if the integers in both numerator and
#   denominator are under the maximums specified by the user
# It will also return False immediately for any negative rational numbers.
# Change accept_negatives to true to disable this behavior.
# Input max_numerator := float('inf') to have numerator of any size, and likewise for max_denominator
def is_small_rat(r, numerator_max, denominator_max):
    accept_negatives = False
    if r < 0 and not accept_negatives:
        return False
    else:
        num_den = r.as_integer_ratio()  # expresses float as reduced ratio of integers, stored as a 2-tuple
        # numerator = num_den[0], denominator = num_den[1]
        return abs(num_den[0]) <= numerator_max and abs(num_den[1]) < denominator_max

# The Python method as_integers() is not reliable when working with truncated rational numbers, such as
#   round(1/3), so the software is going to miss some genuine rational numbers if it is allowed to say so.
# To enable printing if rational, set print_if_rational := True
def ratio_string(label_string, r ,max_gear_teeth = 1000):
    num_den = r.as_integer_ratio()  # expresses floating point number as reduced ratio of
    #   integers, stored as a 2-tuple
    # numerator = num_den[0], denominator = num_den[1]
    return label_string + " " + str(r) + " = (" + str(num_den[0]) + " / " + str(num_den[1]) + ")" + (("\tRATIONAL" if is_small_rat(abs(r), max_gear_teeth,
            max_gear_teeth) else "\tPRACTICALLY IRRATIONAL") + " AND " + ("POSITIVE" if r > 0 else "NEGATIVE OR 0"))


