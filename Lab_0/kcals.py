#Räkna ut antalet kalorier, cals är en dict och receipe är en lista
#multiplicera kalorierna med antalet
# cals ={"ägg":137} receipe=["2","ägg"]


def kcals(cals, recipe):
  sum = 0
  for ingredient in recipe:
    ingredient_name = ingredient[1]
    ingredient_amount = ingredient[0]
    sum += ingredient_amount*cals[ingredient_name]
  return sum
