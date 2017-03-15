from content.recipe import Recipe
import os

class CookBook(object):

    def __init__(self):
        self.recipe_list = list()

    def read_directory(self, path):
        """

        :param path: The path to the raw recipefiles (either .txt or .rcp [own invention])
        :return: a list of all file paths
        """
        for f in os.listdir(path):
            filename = path + '\\' + f
            r = Recipe()
            r.read_recipe(filename)
            self.recipe_list.append(r)

    def write_cookbookindex(self):
        """
        creates a new folder CBX (if not existent) in that a cbx.file ist written containing all information on the recipes in the open CookBook

        :return:
        """

    def read_cookbookindex(self,path):
        """
        reads a .cbx file containing the rating, the
        :param path:
        :return:
        """
        pass

    def cook_into_latex(self):                      #a certain parameterset will be given to specify a certain range of recipes to write into one latexcookbook
        """
        This function should run the available code from the texing package to write all the files

        :return:
        """
        pass

    def get_random_recipe(self):
         """
         gives a random recipe out of the opened cookbook_index #e certain set of parameters should be specified to not end up with getting steak proposed as dessert
         :return:
         """
         pass