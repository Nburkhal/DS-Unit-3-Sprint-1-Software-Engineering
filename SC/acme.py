import random


class Product:

    '''Blueprint of a product

    Parameters
    ----------------------------------
    - `name` (string with no default)
    - `price` (integer with default value 10)
    - `weight` (integer with default value 20)
    - `flammability` (float with default value 0.5)
    - `identifier` (integer, automatically genererated as a random (uniform) number
       anywhere from 1000000 to 9999999, includisve)(inclusive).
    '''

    def __init__(self, name=None, price=10, weight=20, flammability=0.5, 
                 identifier=random.randint(1000000, 10000000)):

        '''Instantiate the class'''
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier


    def stealability(self):
        '''calculates the price divided by the weight, and then
           returns a message: if the ratio is less than 0.5 return "Not so stealable...",
           if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
           and otherwise return "Very stealable!"
        '''
        result = self.price / self.weight

        if result < 0.5:
            return "Not so stealable..."
        elif result >= 0.5 and result < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"


    def explode(self):
        '''calculates the flammability times the weight, and then
           returns a message: if the product is less than 10 return "...fizzle.", if it is
           greater or equal to 10 but less than 50 return "...boom!", and otherwise
           return "...BABOOM!!"
        '''
        result = self.flammability * self.weight
        if result < 10:
            return "...fizzle."
        elif result >= 10 and result < 50:
            return "...boom!"
        else:
            return "...BABOOM!"


class BoxingGlove(Product):
    '''Make a subclass of `Product` named `BoxingGlove` that does the following:

       - Change the default `weight` to 10 (but leave other defaults unchanged)
       - Override the `explode` method to always return "...it's a glove."
       - Add a `punch` method that returns "That tickles." if the weight is below 5,
         "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, and
         "OUCH!" otherwise
    '''

    
    def __init__(self, name=None, price=10, weight=10, flammability=0.5, 
                 identifier=random.randint(1000000, 10000000)):
        '''Instantiate the class object'''
        super().__init__(name=name, price=price, weight=weight, 
                         flammability=flammability, identifier=random.randint(1000000, 
                         10000000))

        self.weight = weight

    
    def explode(self):
        '''Always return "...it's a glove."'''
        return "...it's a glove."


    def punch(self):
        '''Add a `punch` method that returns "That tickles." if the weight is below 5,
           "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, and
           "OUCH!" otherwise
        '''
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
