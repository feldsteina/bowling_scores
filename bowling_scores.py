# Bowling Score Calculator
# By: Adam Feldstein
# Last Modified: 2020-12-09 18:01


def parse_string(input_string):

    frame_data_list = input_string.split("-")

    return frame_data_list


def bonus_check(bonus_score_list, bonus_throws, score_list_index):
    bonus_score_data = bonus_score_list.copy()

    print(str(bonus_score_data[score_list_index]) + " at index " +
          str(score_list_index) + " triggered bonus_check")

    if score_list_index < len(bonus_score_data):
        del bonus_score_data[0:score_list_index+1]

    else:
        del bonus_score_data[0:score_list_index]

    bonus_score = 0

    print("bonus_check list: " + str(bonus_score_data))

    throws_remaining = bonus_throws

    for frame_bonus in bonus_score_data:

        if throws_remaining > 0:

            for pin_bonus in frame_bonus:

                if throws_remaining > 0:

                    if (pin_bonus == "X" or pin_bonus == "x"):
                        bonus_score += 10

                        throws_remaining -= 1

                        print("Bonus so far = " + str(bonus_score))

                        print("bonus_check Throws Remaining: " +
                              str(throws_remaining))

                    if (pin_bonus == "/"):
                        spare_remainder = 10 - int(frame_bonus[0])

                        print("bonus_check Spare Remainder: " +
                              str(spare_remainder))

                        bonus_score += spare_remainder

                        throws_remaining -= 1

                        print("Bonus so far = " + str(bonus_score))

                        print("bonus_check Throws Remaining: " +
                              str(throws_remaining))

                    if pin_bonus.isdigit():
                        pin_int_bonus = int(pin_bonus)

                        bonus_score += pin_int_bonus

                        throws_remaining -= 1

                        print("Bonus so far = " + str(bonus_score))

                        print("bonus_check Throws Remaining: " +
                              str(throws_remaining))

    print(str(score_list_index) + " end bonus score: " + str(bonus_score))

    return bonus_score


def score_total(score_list):
    total_score = 0

    for idx, frame_score in enumerate(score_list):

        for pin_score in frame_score:

            if (pin_score == "X" or pin_score == "x"):
                bonus_pins = bonus_check(score_list, 2, idx)

                total_score += 10

                total_score += bonus_pins

            if pin_score == "/":
                bonus_pins = bonus_check(score_list, 1, idx)

                print(10 - frame_score[1][0])

                spare_remainder = 10 - int(frame_score[1][0])

                print("score_total Spare Remainder: " + str(spare_remainder))

                total_score += spare_remainder

                total_score += bonus_pins

            if pin_score.isdigit():
                pin_int = int(pin_score)

                total_score += pin_int

            print("Total Score so far = " + str(total_score))

            if idx >= len(score_list):
                break

    return total_score


scores = parse_string("09-18-27-36-45-54-63-72-81-90")

final_score = score_total(scores)

print("final score: " + str(final_score))
