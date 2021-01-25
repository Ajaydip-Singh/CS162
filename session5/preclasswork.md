# Question 2

A tomato can be a feature because if we have tomatoes in the fruit salad, the fruit salad effectively becomes a tomato fruit salad (which is a recipe of itself)

However, originally fruit salads do not have tomatoes and therefore it is a bug if a tomato is in the fruit salad.

# Question 3

It does not work with an instance of a list

It does work with integers if the integer is not zero

It does work with floats as well if the float is not zero.zero

It does not work with strings


# Question 4

The bug is that the default weight of a tomato is 3.0 kg which is terribly high.

We can correct this by putting a more sensible value such as 0.3 kg

'''
class Tomato(Fruit, Vegetable):
    def __init__(self, name='Tomato', weight_kg=0.3):
        super().__init__(name=name, weight_kg=weight_kg)
'''
