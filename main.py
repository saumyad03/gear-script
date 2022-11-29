# This script is optimized for usability and readability

# Insert license info here (who can use this script and for what purposes)

# Inputs
# input_name = value  # {variable on Excel sheet}
input_diametral_pitch = 2  # Dp1
sun_gear_1_tooth_count = 12  # Ns1
annulus_gear_1_tooth_count = 27  # Na1

num_planets_in_carrier = 3  # P
second_stage_multiplier = 1  # n

max_gear_teeth = 1000


# Comment out the six next lines to disable user input. Then, set parameters above
input_diametral_pitch = int(input("Input Diametral Pitch = "))
sun_gear_1_tooth_count = int(input("Sun Gear 1 Tooth Count = "))
annulus_gear_1_tooth_count = int(input("Annulus Gear 1 Tooth Count = "))

num_planets_in_carrier = int(input("Number of Planets in Carrier = "))
second_stage_multiplier = float(input("Second Stage Multiplier = "))

# Outputs
# planet_gears_1_tooth_count = Np1

# output_diametral_pitch = Dp2
# sun_gear_2_tooth_count = Ns2
# planet_gears_2_tooth_count = Np2
# annulus_gear_2_tooth_count = Na2

# ratio_first_stage_output = R1
# ratio_second_stage_output = R2
# final_output_ratio_output_shaft = Rf

# ratio_overall =  ratio
# output_teeth = output teeth

# ratio_first_stage_input = R1
# ratio_second_stage_input = R2
# final_output_ratio_input_shaft = Rf

# input_name = value  # {variable on Excel sheet}
input_diametral_pitch = 2  # Dp1
sun_gear_1_tooth_count = 12  # Ns1
annulus_gear_1_tooth_count = 27  # Na1

num_planets_in_carrier = 3  # P

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
def ratio_string(label_string,r):
    num_den = r.as_integer_ratio()  # expresses floating point number as reduced ratio of
    #   integers, stored as a 2-tuple
    # numerator = num_den[0], denominator = num_den[1]
    return label_string + " " + str(r) + " = (" + str(num_den[0]) + " / " + str(num_den[1]) + ")" + (("\tRATIONAL" if is_small_rat(abs(r), max_gear_teeth,
            max_gear_teeth) else "\tPRACTICALLY IRRATIONAL") + " AND " + ("POSITIVE" if r > 0 else "NEGATIVE OR 0"))


# The logic below checks if gear tooth number specifications are natural numbers.
# Specifically, it prints a text whenever a number is equal to or less than 0, or greater than 0 but not an integer.
# Depending on the construction used, natural numbers "begin" at 1 or 0. We will use the natural numbers starting at 1
#   because a gear with zero teeth is not a gear, whereas a practical gear with one tooth is a single-start worm drive.
if (not is_natural(num_planets_in_carrier)):
    print("Error: Number of planets in carrier is not a natural number")

if (not is_natural(sun_gear_1_tooth_count)):
    print("Error: Number of teeth in sun gear is not a natural number")

if not is_natural(annulus_gear_1_tooth_count):
    print("Error: Number of teeth in annulus gear is not an integer")


# Calculations
# These are inherited from the Excel sheet
planet_gears_1_tooth_count = (annulus_gear_1_tooth_count - sun_gear_1_tooth_count)/2
planet_gears_2_tooth_count = planet_gears_1_tooth_count * second_stage_multiplier
annulus_gear_2_tooth_count = (second_stage_multiplier * annulus_gear_1_tooth_count) + num_planets_in_carrier
planet_gears_1_tooth_count = (annulus_gear_1_tooth_count - sun_gear_1_tooth_count) / 2
sun_gear_2_tooth_count = annulus_gear_2_tooth_count - (2 * planet_gears_2_tooth_count)
# Checking for division-by-zero in denominator of planet_gears_2_tooth_count.
# Division by zero is impossible to define mathematically, and as such, Python will throw an exception if one tries to
#   divide by zero.
if annulus_gear_1_tooth_count == planet_gears_1_tooth_count:
    print("Division by Zero: Annulus gear 1 and Planet gears must not have the same number of teeth")
else:
    # Checking for zero output_diametral_pitch.
    # It is used as a divisor later in the calculation
    if annulus_gear_2_tooth_count == planet_gears_2_tooth_count:
        print("Division by zero: Annulus gear 2 and planet gears 2 must not have same number of teeth")
    else:
        output_diametral_pitch = ((input_diametral_pitch * (annulus_gear_2_tooth_count - planet_gears_2_tooth_count)) /
                                 (annulus_gear_1_tooth_count - planet_gears_1_tooth_count))
        ratio_first_stage_output = (annulus_gear_1_tooth_count / sun_gear_1_tooth_count) + 1

        # Checking for division by zero in ratio_second_stage_output
        if (annulus_gear_2_tooth_count == second_stage_multiplier * annulus_gear_1_tooth_count):
            print("Division by zero: Annulus Gear 2 tooth count must not equal second stage multiplier times Annulus gear",
                  "1 tooth count")

        else:
            ratio_second_stage_output = (second_stage_multiplier * annulus_gear_2_tooth_count) / (annulus_gear_2_tooth_count -
                                        (second_stage_multiplier * annulus_gear_1_tooth_count))
            final_output_ratio_output_shaft = ratio_first_stage_output * ratio_second_stage_output

            ratio_overall = input_diametral_pitch / output_diametral_pitch
            output_teeth = ratio_overall * input_diametral_pitch

            ratio_first_stage_input = (annulus_gear_2_tooth_count / sun_gear_2_tooth_count) + 1
            # Checking for division by zero in ratio_second_stage_input
            if annulus_gear_1_tooth_count == (second_stage_multiplier * annulus_gear_2_tooth_count):
                print("Division by zero: Annulus Gear 1 must not have the same number of teeth as (second stage multiplier times annulus gear 2)")
            else:
                ratio_second_stage_input = ((second_stage_multiplier * annulus_gear_1_tooth_count) / (annulus_gear_1_tooth_count -
                                                                                                      (second_stage_multiplier * annulus_gear_2_tooth_count)))
                final_output_ratio_input_shaft = ratio_first_stage_input * ratio_second_stage_input

            # Friendly display script
            # Displays outputs, as well as information about whether certain parameters are natual numbers or not
            print("Planet Gears 1 Toothcount =", planet_gears_1_tooth_count, "\t", print_natual_num(planet_gears_1_tooth_count))
            print("Output Diametral Pitch =", output_diametral_pitch, "\t\t\t", print_natual_num(output_diametral_pitch))
            print("Sun Gear 2 Toothcount =", sun_gear_2_tooth_count, "\t\t\t", print_natual_num(sun_gear_2_tooth_count))
            print("Planet Gears 2 Toothcount =", planet_gears_2_tooth_count, "\t\t", print_natual_num(planet_gears_2_tooth_count))
            print("Annulus Gear 2 Toothcount =", annulus_gear_2_tooth_count, "\t\t", print_natual_num(annulus_gear_2_tooth_count))
            print("Output =", output_teeth, "\t\t", print_natual_num(output_teeth))
            print("")

            print(ratio_string("Ratio First Stage, Output =",  ratio_first_stage_output))
            print(ratio_string("Ratio Second Stage, Output =", ratio_second_stage_output))
            print(ratio_string("Final Ratio at Output Shaft =", final_output_ratio_output_shaft))
            print("")

            print(ratio_string("Ratio First Stage, Output =", ratio_first_stage_input))
            print(ratio_string("Ratio Second Stage, Output =", ratio_second_stage_input))
            print(ratio_string("Final Ratio at Output Shaft =", final_output_ratio_input_shaft))
            print("")

            print(ratio_string("Ratio =", ratio_overall))
