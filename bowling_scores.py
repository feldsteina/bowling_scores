# Bowling Score Calculator
# By: Adam Feldstein
# Created on: 2020-12-09 16:16
# Last Modified: 2020-12-10 09:44

# Split the input string into a list of strings, using hypens as the delimiter
# A list of strings is needed due to the possibility of relevant zeroes
# in the most significant digit of an int,
# as well as the appearance of non-int data.
# It is far easier to convert from a text character to an int,
# as opposed to handling the errors from going the other direction.


def parse_string(input_string):

    frame_data_list = input_string.split("-")

    return frame_data_list


# Fast forwards one or two throws as needed to gather the bonus points
# from strikes or spares.

def bonus_check(bonus_score_list, bonus_throws, score_list_index):
    bonus_score_data = bonus_score_list.copy()

    # Debug output to confirm parameters
    # Should be commented out for production

    # print(str(bonus_score_data[score_list_index]) + " at index " +
    #       str(score_list_index) +
    #       " triggered bonus_check")

    # Need to go forward from the frame that triggered this function.
    # Prior data not needed, and can be culled to allow for cleaner execution.
    # Removing prior data allows fewer variables to be used.

    # If statement used to check if this is the last frame.
    # This is used to prevent out-of-bounds errors.
    # Using list length as the benchmark allows arbitrary game lengths.

    # Could be used in the future as part of error checking for 10 frames only.

    if score_list_index < len(bonus_score_data):
        del bonus_score_data[0:score_list_index+1]

    else:
        del bonus_score_data[0:score_list_index]

    # Debug output to confirm remaining list data
    # print("bonus_check list: " + str(bonus_score_data))

    # Initializes the bonus score to be added later to the Strike or Spare.
    bonus_score = 0

    # Almost certainly not needed, but wanted to confirm no scope issues.
    throws_remaining = bonus_throws

    # Confirms valid number of bonus throws in parameters.
    if throws_remaining > 0 and throws_remaining < 3:

        # Iterate through the list
        for frame_bonus in bonus_score_data:

            # Checks if all bonus throws have been used, break out if needed.
            # Technically allows for calling this function with 0 bonus throws.
            if throws_remaining > 0:

                # Iterate through individial frame data.
                for pin_bonus in frame_bonus:

                    # Same as prior check.
                    if throws_remaining > 0:

                        # Check for strikes first.
                        # Earliest special case to trigger.
                        if (pin_bonus == "X" or pin_bonus == "x"):
                            bonus_score += 10

                            # Decrement bonus throws counter.
                            throws_remaining -= 1

                            # Debug output to confirm bonus score
                            # Should be commented out for production
                            # print("Bonus so far = " + str(bonus_score))

                            # Debug output to confirm bonus throws remaining.
                            # Should be commented out for production
                            # print("bonus_check Throws Remaining: " +
                            #   str(throws_remaining))

                        # Check for spares
                        # Happens later than strikes or a normal number,
                        # but is more specific than a normal throw.
                        if (pin_bonus == "/"):
                            # Only strikes cause a spare to be counted here.
                            # Result is 10 for the total bonus score.

                            # In case of invalid frame data,
                            # this will handle it gracefully.

                            # Invalid frame data examples:
                            # * Mislabeled strike
                            # * More than 2 throws in the frame
                            # * More than 3 total throws on final frame

                            # Take difference between 10 and current bonus.
                            spare_remainder = 10 - bonus_score

                            # Debug to confirm remainder calculated correctly
                            # print("bonus_check Spare Remainder: " +
                            #   str(spare_remainder))

                            # Add remainder to current bonus to get 10 total
                            bonus_score += spare_remainder

                            # Decrement bonus throws counter
                            throws_remaining -= 1

                            # Debug output to confirm bonus score
                            # Should be commented out for production
                            # print("Bonus so far = " + str(bonus_score))

                            # Debug output to confirm bonus throws remaining.
                            # Should be commented out for production
                            # print("bonus_check Throws Remaining: " +
                            #   str(throws_remaining))

                        # Handle as number and ignore if invalid data.
                        # This should fail to find a valid int quietly.
                        # Full error handling in enclosing function.
                        if pin_bonus.isdigit():
                            # Type cast str to int using dummy variable
                            pin_int_bonus = int(pin_bonus)

                            # Add to bonus score
                            bonus_score += pin_int_bonus

                            # Decrement bonus throws counter
                            throws_remaining -= 1

                            # Debug output to confirm bonus score
                            # Should be commented out for production
                            # print("Bonus so far = " + str(bonus_score))

                            # Debug output to confirm bonus throws remaining.
                            # Should be commented out for production
                            # print("bonus_check Throws Remaining: " +
                            #   str(throws_remaining))

    # Debug output to confirm final bonus score
    # Should be commented out for production
    # print(str(score_list_index) + " end bonus score: " + str(bonus_score))

    return bonus_score


def score_total(score_list):
    # For checking invalid data
    invalid_data_flag = False

    # Running total of score, used for final output
    total_score = 0

    for idx, frame_score in enumerate(score_list):
        # Checks for invalid data flag to gracefully end program
        # This is done to prevent wrong score output
        if invalid_data_flag:
            break

        for pin_score in frame_score:

            # Check for strikes first.
            # Earliest special case to trigger.
            if (pin_score == "X" or pin_score == "x"):
                # Calls bonus_check() to calculate the bonus score.
                # Strikes get 2 bonus throws added to the score.

                # idx is the current index of the overall list.
                # This is needed to cull data from a copy of score_list.
                bonus_pins = bonus_check(score_list, 2, idx)

                # Strikes have a base value of 10.
                total_score += 10

                # Adds bonus to previous result.
                total_score += bonus_pins

            # Check for spares.
            # More specific case than the generic number.
            # When checking cases, I go from "Most Specific" to "Most Generic".
            if pin_score == "/":
                # Same as the bonus_check in the strikes section.

                # Spares get 1 bonus throw added.
                bonus_pins = bonus_check(score_list, 1, idx)

                # Debug text, confirm initial data for spare remainder calc.
                # print(10 - int(frame_score[0]))

                # Easier to calculate difference needed to get 10,
                # compared to going back and changing earlier data.
                spare_remainder = 10 - int(frame_score[0])

                # Debug text, confirm spare remainder.
                # print("score_total Spare Remainder: " + str(spare_remainder))

                # Add to total score
                total_score += spare_remainder

                # Add bonus score to total
                total_score += bonus_pins

            if pin_score.isdigit():
                # Typecast to int if the char is an int
                pin_int = int(pin_score)

                # Add to total score.
                total_score += pin_int

            # Handles invalid frame data
            # First, confirm if no previous conditions were met
            if (pin_score.isdigit() is False and
                    pin_score != "X" and
                    pin_score != "x" and
                    pin_score != "/"):
                # Print 1-indexed frame in which invalid data was found
                print("Error at Frame " + str(idx + 1))

                # Print invalid data
                print("Invalid data found: " + str(pin_score))

                # Set flag to break out of loop
                invalid_data_flag = True

                break

            # Debug output to confirm running total
            # Should be removed for production
            # print("Total Score so far = " + str(total_score))

    return total_score


scores = parse_string("0/-90-81-72-63-54-45-36-27-XXX")

final_score = score_total(scores)

print(final_score)
