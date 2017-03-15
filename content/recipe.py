#this is rezeptex 0.1


from tools.stringtools import striplr, is_int, is_float
from fraction.fraction import read_fraction_from_string, is_fraction
import re

class Recipe(object):

    keys = ['NAME','CATEGORY','DESCRIPTION','INGREDIENTS', 'STEPS', 'SERVINGS' \
        , 'RATING', 'VARIATION', 'TIPS']           #this is the default
    ingredient_key = 'INGREDIENTS'
    steps_key = 'STEPS'
    and_key = 'AND'

    class Ingredient(object):

        def __init__(self, line=None):
            self.name = ''
            self.quantity = Recipe.Quantity()
            self.unit = ''

            if line is not None:
                self.from_line(line)

        def __repr__(self):
            return '{0:>4} {1:>4} {2}'.format(self.quantity, self.unit, self.name)

        def __str__(self):
            return '{0:>4} {1:>4} {2}'.format(self.quantity, self.unit, self.name)

        def from_line(self, string):
            parts = string.split()

            try:

                self.quantity.read_quantity_from_string(
                    parts[
                        0])  # todo: read_quantity function to be able to read 1.5, 3/2, 1 1/2 as the same quantity
                if parts[1].upper() in Recipe.IngredientList.units:
                    self.unit = Recipe.IngredientList.units[parts[1].upper()]
                    name = ''
                    for part in parts[2:]:
                        name += (part + ' ')
                    self.name = striplr(name)
                else:
                    name = ''
                    for part in parts[1:]:
                        name += (part + ' ')
                    self.name = striplr(name)
            except ValueError:
                name = ''
                for part in parts:
                    name += part + ' '

                self.name = striplr(name)

    class IngredientList(object):

        units1 = ['g', 'kg', 'l', 'cl', 'ml', 'EL', 'TL', 'Msp',
                  'Stck']  # todo: read this from a file to change default
        units = dict()
        for u in units1:
            units[u.upper()] = u

        units['TEEL'] = 'TL'  # todo: also read the alias abbreviations to have one conform style

        def __init__(self, string=None):
            self.header = ''
            self.ingredients = list()

            if string is not None:
                self.make_list_from_string(string)

        def make_list_from_string(self, string):
            lines = string.split('\n')
            if string.find(':') is not -1:
                self.header = lines[0]
                lines = lines[1:]
            for line in lines:
                if line is not '':
                    self.ingredients.append(Recipe.Ingredient(line))

        def print_list(self):
            if self.header is not '':
                print(self.header)
            for ingredient in self.ingredients:
                print(ingredient)

    class Quantity(object):

        _representation_mode = 'default'  # in the default mode the value of the quantity will be printed as is (i.e. a float)
        _list_of_modes = ['default', 'd', 'mixed', 'fi', 'fraction', 'frac', 'if', 'intfrac', 'fracint']

        @classmethod
        def set_representation_mode(cls, mode):
            """
            changes the way a quantity is formatted

            :param string mode: name of the mode
            """
            if mode.upper() in [string.upper() for string in cls._list_of_modes]:
                cls._representation_mode = mode
            else:
                raise NameError(
                    "The user specified mode '{0}' doesn't exist. Chose from {1}.".format(mode, cls._list_of_modes))

        def __init__(self, string='', value=0):
            self.value_as_float = float(value)
            self.value = value
            if string is not '':
                self.read_quantity_from_string(string)

        def __repr__(self):
            if Recipe.Quantity._representation_mode.upper() in ['D', 'DEFAULT']:
                return str(self.value_as_float)
            if Recipe.Quantity._representation_mode.upper() in ['MIXED', 'FI', 'IF', 'INTFRAC', 'FRACINT']:
                if type(self.value) == int:
                    return str(self.value)
                else:
                    return str(self.value_as_float)

        def read_quantity_from_string(self, string):
            """
            function should read ints as ints, floats as floats and fractions as fractions
            :param string:
            :return:
            """
            if is_int(string):
                self.value = int(string)
                self.value_as_float = float(string)
            elif is_float(string):
                self.value = float(string)
                self.value_as_float = float(string)
            elif is_fraction(string):
                self.value = read_fraction_from_string(string)
                self.value_as_float = self.value.as_float()
            else:
                raise ValueError

    class Step(object):

        def __init__(self, string=''):
            self.header = None
            self.bodytext = None

            if string is not '':
                self.read_step_from_string(string)

        def read_step_from_string(self, string):
            self.bodytext = string

    @classmethod
    def set_keys(cls, recipe_keys, ikey = 'INGREDIENTS', skey = 'STEPS', akey = 'AND'):
        """
        set the keywords for the style of a default recipe

        :param recipe_keys:  list of strings with capital letters (according to the style of the desired recipe)
        :param string ikey: keyword to look for, that begins the list of ingredients
        :param string skey: keyword to look for, that begins the list of steps
        """
        Recipe.keys = recipe_keys
        Recipe.ingredient_key = ikey
        Recipe.steps_key = skey
        Recipe.and_key = akey

    def __init__(self, filepath = None):

        for key in Recipe.keys:
            setattr(self, key, None)
        self.ingridientlists = list()
        self.steps = list()
        self.keys_found = list()

        if filepath is not None:
            self.read_recipe(filepath)

    def _make_list_from_given_ingredients(self):
        if Recipe.ingredient_key in self.keys_found:
            s = getattr(self, Recipe.ingredient_key)
            raw = s.split(Recipe.and_key)
            for part in raw:
                if striplr(part) is not '':
                    self.ingridientlists.append(Recipe.IngredientList(striplr(part)))
        else:
            print('The expected ingredient_key was not given! Expected: '+Recipe.ingredient_key)

    def _make_steps_from_given_steps(self):
        if Recipe.steps_key in self.keys_found:
            s = getattr(self, Recipe.steps_key)
            regex = Recipe.and_key+'|\n\n'
            raw = re.split(regex,s)
            for part in raw:
                if striplr(part) is not '':
                    self.steps.append(Recipe.Step(part))


    def read_recipe(self, filepath, store = False):
        """
        This function opens the given file to get the raw Material for a recipe. This recipe can then be stored by its ID

        :param string filepath:  The path to the file, that should be read
        :param bool store:  indicates wheter the recipe will be added to a list of recipes or not
        :return:
        """

        f = open(filepath, 'r')
        text = f.read()
        f.close()
        keys_not_found = list()
        for key in Recipe.keys:
            if text.find(key) == -1:
                keys_not_found.append(key)
            else:
                self.keys_found.append(key)
        print("In <{}>: The keywords {} might be missing!.".format(filepath, keys_not_found))  #todo: write a function that expects to add information about the servings
        keys_ordered = list()


        for key in Recipe.keys:
            position = text.find(key)
            if position >= 0:
                keys_ordered.append((position, key))

        keys_ordered.sort()
        keys_ordered.append((len(text), 'EOF'))

        for i in range(0, len(keys_ordered) - 1):
            ko = keys_ordered
            setattr(self, ko[i][1], striplr(text[ko[i][0]+len(ko[i][1]):ko[i + 1][0]]))

        self._make_list_from_given_ingredients()
        self._make_steps_from_given_steps()

    def value_of_key(self, key):
        return getattr(self, key)

    def relevant_keys(self):
        return [key for key in Recipe.keys ]








