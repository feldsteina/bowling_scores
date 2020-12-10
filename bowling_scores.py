# Bowling Score Calculator
# By: Adam Feldstein
# Last Modified: 2020-12-09 18:01

def parse_string(input_string):

    frame_data_list = input_string.split("-")

    return frame_data_list


def bonus_check(score_list, bonus_throws, score_list_index):
    print(str(score_list[score_list_index-1]) + " triggered bonus score")

    del score_list[0:score_list_index]

    bonus_score = 0

    print(score_list)

    print("bonus score: " + str(bonus_score))

    throws_remaining = bonus_throws

    for frames in score_list:

        if throws_remaining > 0:

            for pins in frames:

                if throws_remaining > 0:

                    if (pins == "X" or pins == "x"):
                        bonus_score += 10
                        throws_remaining -= 1

                    if (pins == "/"):
                        spare_remainder = 10 - int(frames[0])
                        bonus_score += spare_remainder
                        throws_remaining -= 1

                    if pins.isdigit():
                        pin_score = int(pins)
                        bonus_score += pin_score
                        throws_remaining -= 1

                else:
                    break

        else:
            break

    return bonus_score


def score_total(score_list):
    total_score = 0

    for idx, frames in score_list:

        for pins in frames:

            if (pins == "X" or pins == "x"):
                bonus_pins = bonus_check(score_list, 2, idx+1)
                total_score += 10
                total_score += bonus_pins

    return total_score


scores = parse_string("01-23-45-x-8/-x-35-51-x-09")

# print(score_total(scores))

print("total bonus: " + str(bonus_check(scores, 2, 6)))
