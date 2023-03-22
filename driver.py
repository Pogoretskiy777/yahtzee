"""Yahtzee Driver Program.

This class provides a command line interface for demonstrating the function of
the yahtzee program.

Author: Ralph Grove, Chris Mayfield, Alvin Chao(python conversion)
Version: 02/08/2017, 10/7/2022
"""
import yahtzee
import random


if __name__ == '__main__':
    """Simulates one turn of a yahtzee game:
    1. generate random values to instantiate a list of five dice values
    2. display the dice and ask the user how to score them
    3. invoke yahtzee.calculateScore() to score the dice
    4. display the dice score based on the user's choice
    """
    die1 = int(random.randrange(1, 6))
    die2 = int(random.randrange(1, 6))
    die3 = int(random.randrange(1, 6))
    die4 = int(random.randrange(1, 6))
    die5 = int(random.randrange(1, 6))
    dice = [die1, die2, die3, die4, die5]
    print("You rolled:", die1, ",", die2, ",", die3, ",", die4, ",", die5)
    print("How would you like to play them?")
    print("Ones:", yahtzee.ONES)
    print("Twos:",  yahtzee.TWOS)
    print("Threes:", yahtzee.THREES)
    print("Fours:", yahtzee.FOURS)
    print("Fives:", yahtzee.FIVES)
    print("Sixes:", yahtzee.SIXES)
    print("Three of a kind:", yahtzee.THREE_OF_A_KIND)
    print("Four of a kind:", yahtzee.FOUR_OF_A_KIND)
    print("Full House:", yahtzee.FULL_HOUSE)
    print("Small Straight:", yahtzee.SMALL_STRAIGHT)
    print("Large Straight:", yahtzee.LARGE_STRAIGHT)
    print("Yahtzee:", yahtzee.YAHTZEE)
    print("Chance:", yahtzee.CHANCE)
    print("-----")
    choice = int(input("Selection: "))
    print("The value of your roll is:", yahtzee.calculate_score(dice, choice))