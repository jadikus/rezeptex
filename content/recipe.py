from tools.stringtools import striplr
from fraction.fraction import read_fraction_from_string

class Recipe(object):

    keys = ['NAME','CATEGORY','DESCRIPTION','INGREDIENTS', 'STEPS']           #this is the default
    ingredient_key = 'INGREDIENTS'
    steps_key = 'STEPS'

    @classmethod
    def set_keys(cls, recipe_keys, ikey = 'INGREDIENTS', skey = 'STEPS'):
        """
        set the keywords for the style of a default recipe

        :param recipe_keys:  list of strings with capital letters (according to the style of the desired recipe)
        :param string ikey: keyword to look for, that begins the list of ingredients
        :param string skey: keyword to look for, that begins the list of steps
        """
        Recipe.keys = recipe_keys
        Recipe.ingredient_key = ikey
        Recipe.steps_key = skey

    def __init__(self, filepath = None):
        self.vardict = dict()
        for key in Recipe.keys:
            self.vardict[key] = None
        self.ingridientlists = list()
        self.steps = list()

        if filepath is not None:
            self.read_recipe(filepath)

    def make_list_from_given_ingredients(self):
        if Recipe.ingredient_key in Recipe.keys:
            raw = self.vardict[Recipe.ingredient_key].split('#')
            for part in raw:
                if striplr(part) is not '':
                    self.ingridientlists.append(IngredientList(striplr(part)))
        else:
            print('The expected ingredient_key was not given! Expected: '+Recipe.ingredient_key)

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
        for key in Recipe.keys:
            if text.find(key) == -1:
                print(key + ': this keyword might be missing in: ' + filepath)
        keys_ordered = list()


        for key in Recipe.keys:
            position = text.find(key)
            if position >= 0:
                keys_ordered.append((position, key))

        keys_ordered.sort()
        keys_ordered.append((len(text), 'EOF'))

        for i in range(0, len(keys_ordered) - 1):
            ko = keys_ordered
            self.vardict[ko[i][1]]= striplr(text[ko[i][0]+len(ko[i][1]):ko[i + 1][0]])

        self.make_list_from_given_ingredients()

    def value_of_key(self, key):
        return self.vardict[key]

    def relevant_keys(self):
        return [key for key in Recipe.keys ]

class Step(object):

    def __init__(self):
        self.number = None
        self.bodytext = None



class IngredientList(object):

    units1 = ['g', 'kg', 'l', 'cl', 'ml', 'EL','TL', 'Msp', 'Stck']  #todo: read this from a file to change default
    units = dict()
    for u in units1:
        units[u.upper()] = u

    units['TEEL'] = 'TL'    #todo: also read the alias abbreviations to have one conform style

    def __init__(self, string = None):
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
                self.ingredients.append(Ingredient(line))

    def print_list(self):
        if self.header is not '':
            print(self.header)
        for ingredient in self.ingredients:
            print(ingredient)


class Ingredient(object):

    def __init__(self, line = None):
        self.name = ''
        self.quantity = ''
        self.unit = ''

        if line is not None:
            self.from_line(line)

    def __repr__(self):
        return '{0:>4} {1:>4} {2}'.format(self.quantity, self.unit, self.name)

    def __str__(self):
        return '{0:>4} {1:>4} {2}'.format(self.quantity, self.unit, self.name)

    @staticmethod
    def is_quantity(string):
        """tests, whether the given string is a number or a fraction"""
        try:
            read_fraction_from_string(string)
            return True
        except:
            return False



    def from_line(self, string):
        parts = string.split()

        try:
            self.is_quantity(parts[0])
            self.quantity = read_fraction_from_string(parts[0])   #todo: read_quantity function to be able to read 1.5, 3/2, 1 1/2 as the same quantity
            if parts[1].upper() in IngredientList.units:
                self.unit = IngredientList.units[parts[1].upper()]
                name = ''
                for part in parts[2:]:
                    name += (part + ' ')
                self.name = striplr(name)
            else:
                name = ''
                for part in parts[1:]:
                    name += (part+' ')
                self.name = striplr(name)
        except ValueError:
            self.name = string



