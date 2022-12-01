# This script is optimized for usability and readability
import numpy as np


def gear_script(input_diametral_pitch, sun_gear_1_tooth_count, annulus_gear_1_tooth_count, num_planets_in_carrier,
                second_stage_multiplier, check_if_reasonable=False):
    [planet_gears_1_tooth_count,
     output_diametral_pitch,
     sun_gear_2_tooth_count,
     planet_gears_2_tooth_count,
     annulus_gear_2_tooth_count,
     output_teeth,
     ratio_first_stage_output,
     ratio_second_stage_output,
     final_output_ratio_output_shaft,
     ratio_first_stage_input,
     ratio_second_stage_input,
     final_output_ratio_input_shaft,
     ratio_overall] = np.array(np.zeros(13))

    # Calculations
    # These are inherited from the Excel sheet
    planet_gears_1_tooth_count = (annulus_gear_1_tooth_count - sun_gear_1_tooth_count) / 2
    planet_gears_2_tooth_count = planet_gears_1_tooth_count * second_stage_multiplier
    annulus_gear_2_tooth_count = (second_stage_multiplier * annulus_gear_1_tooth_count) + num_planets_in_carrier
    planet_gears_1_tooth_count = (annulus_gear_1_tooth_count - sun_gear_1_tooth_count) / 2
    sun_gear_2_tooth_count = annulus_gear_2_tooth_count - (2 * planet_gears_2_tooth_count)
    # Checking for division-by-zero in denominator of planet_gears_2_tooth_count.
    # Division by zero is impossible to define mathematically, and as such, Python will throw an exception if one tries to
    #   divide by zero.

    if (annulus_gear_1_tooth_count == planet_gears_1_tooth_count) and check_if_reasonable:
        print("Division by Zero: Annulus gear 1 and Planet gears 1 must not have the same number of teeth")
    else:
        # Checking for zero output_diametral_pitch.
        # It is used as a divisor later in the calculation
        if (annulus_gear_2_tooth_count == planet_gears_2_tooth_count) and check_if_reasonable:
            print("Division by zero: Annulus gear 2 and planet gears 2 must not have same number of teeth")
        else:
            output_diametral_pitch = (
                        (input_diametral_pitch * (annulus_gear_2_tooth_count - planet_gears_2_tooth_count)) /
                        (annulus_gear_1_tooth_count - planet_gears_1_tooth_count))
            ratio_first_stage_output = (annulus_gear_1_tooth_count / sun_gear_1_tooth_count) + 1

            # Checking for division by zero in ratio_second_stage_output
            if (annulus_gear_2_tooth_count == second_stage_multiplier * annulus_gear_1_tooth_count) and check_if_reasonable:
                print(
                    "Division by zero: Annulus Gear 2 tooth count must not equal second stage multiplier times Annulus gear",
                    "1 tooth count")

            else:
                ratio_second_stage_output = (second_stage_multiplier * annulus_gear_2_tooth_count) / (
                            annulus_gear_2_tooth_count -
                            (second_stage_multiplier * annulus_gear_1_tooth_count))
                final_output_ratio_output_shaft = ratio_first_stage_output * ratio_second_stage_output

                ratio_overall = input_diametral_pitch / output_diametral_pitch
                output_teeth = ratio_overall * input_diametral_pitch

                ratio_first_stage_input = (annulus_gear_2_tooth_count / sun_gear_2_tooth_count) + 1
                # Checking for division by zero in ratio_second_stage_input
                if (annulus_gear_1_tooth_count == (second_stage_multiplier * annulus_gear_2_tooth_count)) and check_if_reasonable:
                    print(
                        "Division by zero: Annulus Gear 1 must not have the same number of teeth as (second stage multiplier times annulus gear 2)")
                else:
                    ratio_second_stage_input = (
                                (second_stage_multiplier * annulus_gear_1_tooth_count) / (annulus_gear_1_tooth_count -
                                                                                          (
                                                                                                      second_stage_multiplier * annulus_gear_2_tooth_count)))
                    final_output_ratio_input_shaft = ratio_first_stage_input * ratio_second_stage_input

    return np.array([planet_gears_1_tooth_count,
     output_diametral_pitch,
     sun_gear_2_tooth_count,
     planet_gears_2_tooth_count,
     annulus_gear_2_tooth_count,
     output_teeth,
     ratio_first_stage_output,
     ratio_second_stage_output,
     final_output_ratio_output_shaft,
     ratio_first_stage_input,
     ratio_second_stage_input,
     final_output_ratio_input_shaft,
     ratio_overall])



