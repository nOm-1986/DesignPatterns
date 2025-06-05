from BurgerDirector import BurgerDirector
from ClassicBugerBuilder import ClassicBurgerBuilder
from VeggieBurgerBuilder import VeggieBurgerBuilder

if __name__ == '__main__':
    chef = BurgerDirector()
    classic_builder = ClassicBurgerBuilder()
    print('Making a classic burger')
    chef.make_burger(classic_builder)
    classic_burger = classic_builder.get_buger()
    print(classic_burger)
    print('\n Making a veggie burger... \n')
    veg_builder = VeggieBurgerBuilder()
    chef.make_burger(veg_builder)
    print(veg_builder.get_buger())

    
