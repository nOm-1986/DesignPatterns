from cook_director import Cook
from pizza_builder import MargueritaBuilder

cook = Cook()
marguerita_builder = MargueritaBuilder()
pizza1 = cook.make_pizza(marguerita_builder)
print(pizza1)