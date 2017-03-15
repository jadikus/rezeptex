from content.recipe import Recipe
from fraction.fraction import Fraction, read_fraction_from_string
import re




r = Recipe('recipexample')


r.Quantity.set_representation_mode('FRACINT')

for ind in r.ingridientlists:
    ind.print_list()

for step in r.steps:
    print(step.bodytext)




#for key in r.relevant_keys():
#    print('-'*6 + key +'-'* 6 + '\n' + r.value_of_key(key))





