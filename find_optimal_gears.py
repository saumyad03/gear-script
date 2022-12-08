import gear_script as gs
import math_functions as mt
import numpy as np
# NOTE: xlwt, the Excel file library, is *not* installed by default in ordinary Python or Anaconda!
# run pip3 install xlwt if Python throws an error.
import xlwt
# If Python throws an error like:
# PermissionError: [Errno 13] Permission denied: 'gears.xls'
# Then that likely means you have the Excel file open in Excel. Excel won't let you modify the file.
from xlwt import Workbook




# This is a function to find all the feasible split-ring planetary gear configurations and write them to an Excel file,
# based on both the inherent geometry of the gear configuration, as well as the constraints imposed for our particular
# project.

# Because there are some long lines and mild math going on, I have elected to use the shortened symbolic names as the
# variables in this program.
# The variable names are inherited from the original Excel sheet

# The program leverages the fact that Np2 = n*Np1 must be a natural number, and that both Np1 and Np2 can be constrained
# by minima and maxima on a physical basis, to enumerate all combinations of acceptable ratios.
# Thus, the ratio Np2/Np1 is calculated and input into the ratio parameter of the gear script function.
# The function iterates over all allowed pairs of P, Ns1, Na1, Np2

def find_optimal_gears(min_teeth = 13, max_teeth = 100, min_planets = 3, max_planets = 5, Dp1 = 1):
    # A xlwt Workbook class is instantiated
    wb = Workbook()
    # A sheet is added to the Excel file of the current workbook.
    sheet = wb.add_sheet('Sheet 1')

    # row and column are the "current" row and column position that the program is working with.
    # Indices start at *0*, not 1 as they are typically marked in an Excel sheet.
    row = 0
    column = 0

    # These lines create headings in the Excel files
    # They designate a column for each input of the optimization algorithm and each output
    input_heading = np.array(["P", "Ns1", "Na1", "Np2"])
    output_heading = np.array(["planet_gears_1_tooth_count",
     "output_diametral_pitch",
     "sun_gear_2_tooth_count",
     "planet_gears_2_tooth_count",
     "annulus_gear_2_tooth_count",
     "output_teeth",
     "ratio_first_stage_output",
     "ratio_second_stage_output",
     "final_output_ratio_output_shaft",
     "ratio_first_stage_input",
     "ratio_second_stage_input",
     "final_output_ratio_input_shaft",
     "ratio_overall"])
    heading = np.concatenate((input_heading, output_heading))

    # This for-loop writes each item in the heading to the "first" (0-th) row of the Excel sheet.
    for i in heading:
        sheet.write(row, column, heading[column])
        column = column + 1

    # set Excel Column to the leftmost (0), set row to the next one
    column = 0
    row = 1

    # Save the changes so far to an Excel file.
    wb.save('gears.xls')

    # P_space := the "space" of all possible numbers of planets
    # It should be some finite set of natural numbers represented as a numpy array
    # P_space defaults to the set {3,4,5}, although it is set to find the set procedurally by counting from a minimum to
    # a maximum, which can be specified as an optional argument (min_teeth and max_teeth respectively)
    # Note that the math in the argument of np.arange() will include the minimum and maximum in the set.
    P_space = np.arange(min_planets, max_planets + 1, 1).astype(dtype=int)

    # output = np.zeros((1, 13))
    # output = np.array([[]])
    # intermediate = np.concatenate((np.zeros((1, 5)), np.zeros((1, 13))), axis=1)
    # output = np.concatenate((output, np.zeros((1, 5))), axis=1)
    for P in P_space:
        # tooth_space is the set of permissible gear pairs based on the number of planets and
        # If every possible gear is represented as an ordered pair of its parameters, then the space of all possible gears is
        # the set defined by the for-loops below. The tooth_space set establishes the allowable integers for the
        # gears whose teeth must be evenly divisible by the number of planets.
        # A number n is evenly divisible by k if (n/k) is an integer. Usually, n and k are themselves integers.
        # For example, (6/3) = 2, so 6 is evenly divisible by 3.
        # As a non-example, (6/5) = 1.2, so 6 is not evenly divisible by 5.
        tooth_space = np.array([x for x in range(P, max_teeth + 1, P)]).astype(dtype=int)


        # Ns1 must be less than or equal to the minimum number of teeth
        for Ns1 in tooth_space[tooth_space >= min_teeth]:
            # Np1 = (Na1 - Ns1)/2
            # Np1 is the number of teeth in the planet gear of the input
            # Consequently, Np be a natural number and positive
            # This restricts the values of Na1 to be strictly greater than Ns1 and non-zero
            for Na1 in tooth_space[(tooth_space > Ns1)]:
                # Now, we only drop into the next nested for-loop if the previously mentioned tooth count is an integer
                Np1 = (Na1 - Ns1) / 2
                if (int(Np1) == Np1) and int(Np1) >= int(1):
                    # Ns2 must be divisible by P for geometrical reasons, and greater than or equal to the minimum.

                    # Np2 must be within the minimum or maximum, but it need not be evenly divisible by P
                    for Np2 in range(int(np.ceil(min_teeth/2)*2), int(np.floor(max_teeth/2)*2), 2):
                        Na2 = (Np2 * Na1 / Np1) + P
                        Ns2 = Na2 - (2 * Np2)

                        if (int(Na2) == Na2) and int(Na2) >= min_teeth and int(Na2) <= max_teeth\
                        and (int(Ns2/P) == Ns2/P) and int(Ns2) >= min_teeth and int(Ns2) <= max_teeth:
                            # As a reminder:
                            # gs.gear_script(input_diametral_pitch,
                            #                sun_gear_1_tooth_count,
                            #                annulus_gear_1_tooth_count,
                            #                num_planets_in_carrier=,second_stage_multiplier)
                            # From the spreadsheet, n = Np2/Np1
                            # The code below writes one row of data to a numpy array
                            intermediate = np.concatenate((np.array([P, Ns1, Na1, Np2]),
                                                         gs.gear_script(Dp1, Ns1, Na1, P, Np2/Np1)), axis = 0)

                            # The for-loop below writes one line of data to the Excel Sheet
                            for k in intermediate:
                                sheet.write(row, column, intermediate[column])
                                column = column + 1

                            row = row + 1
                            column = 0

                            # output = np.append(output,[intermediate],axis = 1)
                            # print([P, Ns1, Na1, Ns2, Np2])
    # The code below saves the data to the Excel file.
    # It runs much faster with the save function outside the loop.
    return wb.save('gears.xls');

# gs.gear_script(Dp1, Ns1, Na1, P, n)








print(find_optimal_gears(21,100))