from content.recipe import Recipe, Ingredient, IngredientList
from fraction.fraction import Fraction, read_fraction_from_string

#f = open('Zutaten', 'r')
#s = f.read()

#l = IngredientList(s)
#print(l.ingredients)
#l.print_list()

r = Recipe('recipexample')
for ind in r.ingridientlists:
    ind.print_list()




a = Fraction(2, 3)
b = read_fraction_from_string('51/50', 'b')

print (b)



#for key in r.relevant_keys():
#    print('-'*6 + key +'-'* 6 + '\n' + r.value_of_key(key))





