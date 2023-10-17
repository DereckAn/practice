"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return (EXPECTED_BAKE_TIME - elapsed_bake_time)

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - preparation time in minutes.

    Function that takes the number of layers in the lasagna as an argument
    and returns how long it will take to prepare the lasagna.
    """
    return (number_of_layers * 2)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).

    Function that takes the number of layers in the lasagna and the actual
    minutes the lasagna has been in the oven as arguments and returns how
    many minutes have elapsed since preparation began.
    """
    return (preparation_time_in_minutes(number_of_layers) + bake_time_remaining(elapsed_bake_time))

    
print(elapsed_time_in_minutes(3,20))
