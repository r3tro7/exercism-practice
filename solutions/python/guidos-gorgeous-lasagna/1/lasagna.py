"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time.

    :param number_of_layers: int - layers of the lasagna.
    :return: int - total preparation time required derived from `number_of_layers`.

    Function that takes the number of layers of the lasagna as
    an argument and returns how many minutes the are needed to prepare
    based on the `number_of_layers`.
    """
    return number_of_layers * PREPARATION_TIME


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed bake time.

    :param number_of_layers: int - layers of the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time including preparation.

    Function that takes the number of layers of the lasagna and time the lasagna has been in the oven as
    an argument and returns how many minutes have elapsed since in the kitchen
    based on the `number_of_layers` and `elapsed_bake_time`).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time