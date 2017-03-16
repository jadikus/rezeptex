from content.recipe import Recipe
from content.CookBook import CookBook
from fraction.fraction import Fraction, read_fraction_from_string
import re




cb = CookBook()
cb.read_directory("recipes_raw")

print(len(cb.recipe_list))


#for key in r.relevant_keys():
#    print('-'*6 + key +'-'* 6 + '\n' + r.value_of_key(key))





