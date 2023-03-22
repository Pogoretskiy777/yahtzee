"""
Computes the scores for Yahtzee, a dice game by Milton Bradley.

Author: Joseph Pogoretskiy
Version: 11/8/2022
Honor Code: All modifications to the original code are of my own work.
"""

ONES = 1

TWOS = 2

THREES = 3

FOURS = 4

FIVES = 5

SIXES = 6

THREE_OF_A_KIND = 9

FOUR_OF_A_KIND = 10

FULL_HOUSE = 11

SMALL_STRAIGHT = 12

LARGE_STRAIGHT = 13

YAHTZEE = 14

CHANCE = 15


def add_values(dice):
    """Add the values of the five dice in the list.

    Args:
        dice(list): list of 5 int dice values.

    Returns:
        (int):added value of the dice (index 0 to 4)
    """
    value = 0
    value += sum(dice)
    return value


def calculate_score(dice, category):
    """Score calculation for the given turn.

    Args:
        dice(list): list of 5 dice values.
        category(int): category selected by the player

    Returns:
        score(int): number of points, or 0 if N/A
    """
    # Write a decision statement to evaluate the score for each category.
    # Cases that require more than several lines of code should be done
    # in separate methods below. Each case should set the value of the
    # score variable, so that you will have only one return statement.
    score = 0
    if 1 <= category <= 6:
        score += dice.count(category) * category
    elif category == 9 and three_of_a_kind(dice):
        score += add_values(dice)
    elif category == 10 and four_of_a_kind(dice):
        score += add_values(dice)
    elif category == 11 and full_house(dice):
        score += 25
    elif category == 12 and small_straight(dice):
        score += 30
    elif category == 13 and large_straight(dice):
        score += 40
    elif category == 14 and dice.count(dice[0]) == 5:
        score += 50
    elif category == 15:
        score += add_values(dice)
    return score


def three_of_a_kind(dice):
    """Check if atleast three of five values of the dice are identical.

    Args:
        dice(list): list of 5 int dice values.

    Returns:
        boolean: true if there are atleast three of a kind, false if not
    """
    first = dice[0]
    second = dice[1]
    third = dice[2]
    fourth = dice[3]
    fifth = dice[4]
    if (dice.count(first) >= 3 or dice.count(second) >= 3 or
        dice.count(third) >= 3 or dice.count(fourth) >= 3 or
            dice.count(fifth) >= 3):
        return True
    else:
        return False


def four_of_a_kind(dice):
    """Check if atleast four of five values of the dice are identical.

    Args:
        dice(list): list of 5 int dice values.

    Returns:
        boolean: true if there are atleast four of a kind, false if not
    """
    first = dice[0]
    second = dice[1]
    third = dice[2]
    fourth = dice[3]
    fifth = dice[4]
    if (dice.count(first) >= 4 or dice.count(second) >= 4 or
        dice.count(third) >= 4 or dice.count(fourth) >= 4 or
            dice.count(fifth) >= 4):
        return True
    else:
        return False


def full_house(dice):
    """Check if the dice values equate to a full house.

    Args:
        dice(list): list of 5 int dice values.

    Returns:
        boolean: true if the values are a full house, false if not
    """
    min_num = min(dice)
    max_num = max(dice)
    if min_num == max_num:
        return False
    elif ((dice.count(min_num) == 3 and dice.count(max_num) == 2) or
          (dice.count(min_num) == 2 and dice.count(max_num) == 3)):
        return True
    else:
        return False


def small_straight(dice):
    """Go through the dice values to determine if there is a small straight.

    This function sorts the dice and then removes any duplicates. The function
    uses the large_straight to determine if the dice values equate to a small
    straight. The function then goes through other possible lengths of the new
    list with no duplicates and does the proper calculations to determine if
    the dice values are a small straight.

    Args:
        dice(list): list of 5 int dice values.

    Returns:
        boolean: true if the dice values equate to a small straight, or false
        if not
    """
    dice_sorted = sorted(dice)
    i = 0
    while i < 5:
        if dice_sorted.count(i) > 1:
            dice_sorted.remove(i)
            i += 1
        else:
            i += 1
    if large_straight(dice):
        return True
    elif len(dice_sorted) < 4:
        return False
    elif len(dice_sorted) == 5:
        first = dice_sorted[0]
        second = dice_sorted[1]
        third = dice_sorted[2]
        fourth = dice_sorted[3]
        fifth = dice_sorted[4]
        first_calc = second - first
        second_calc = third - second
        third_calc = fourth - third
        fourth_calc = fifth - fourth
        if (first_calc == 1 and second_calc == 1 and third_calc == 1) or (
                second_calc == 1 and third_calc == 1 and fourth_calc == 1):
            return True
        else:
            return False
    elif len(dice_sorted) == 4:
        j = len(dice_sorted)
        difference_total = 0
        while j > 1:
            difference_total += (dice_sorted[j - 1] - dice_sorted[j - 2])
            j -= 1
        if difference_total == 3:
            return True
        else:
            return False


def large_straight(dice):
    """Go through the dice values to determine if there is a large straight.

    This function sorts the dice values and then removes any duplicates. If the
    length of the new list is less than possible to achieve a large straight,
    the function returns false. Otherwise, the new list is then ran through a
    loop to determine the total difference of the values, which can be used to
    determine if the values of the dice are a large straight or not.

    Args:
        dice(list): list of 5 int dice values.

    Returns:
        boolean: true if the dice values equate to a large straight, or false
        if not
    """
    dice_sorted = sorted(dice)
    i = 0
    while i < 5:
        if dice_sorted.count(i) > 1:
            dice_sorted.remove(i)
            i += 1
        else:
            i += 1
    j = len(dice_sorted)
    difference_total = 0
    while j > 1:
        difference_total += (dice_sorted[j - 1] - dice_sorted[j - 2])
        j -= 1
    if len(dice_sorted) < 5:
        return False
    elif difference_total == 4:
        return True
