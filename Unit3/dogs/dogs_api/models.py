from django.db import models


class Breed(models.Model):

    TINY = 'T'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'

    SIZES = {
        TINY: "Tiny",
        SMALL: "Small",
        MEDIUM: "Medium",
        LARGE: "Large",
    }

    LEVELS = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
    }

    name_breed = models.CharField(max_length=50)
    size = models.CharField(max_length=1, choices=SIZES, default=MEDIUM)
    friendliness = models.IntegerField(choices=LEVELS, default=3)
    trainability = models.IntegerField(choices=LEVELS, default=3)
    shedding_amount = models.IntegerField(choices=LEVELS, default=3)
    exercise_needs = models.IntegerField(choices=LEVELS, default=3)

    def __str__(self):
        return self.name_breed


class Dog(models.Model):
    GENDERS = {
        'M': "male",
        'F': "female",
    }

    name = models.CharField(max_length=35)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')
    color = models.CharField(max_length=30)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)


def __str__(self):
    return self.name
