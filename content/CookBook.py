from content.recipe import Recipe

class CookBook(object):

    def read_directory(self, path):
        """

        :param path: The path to the raw recipefiles (either .txt or .rcp [own invention])
        :return: a list of all file paths
        """
        pass

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