from t_pop.collections.adapters.location_cache import LocationCacheAdapter, LocationCacheType
from t_pop.collections.adapters.location_guard import TwoDLocationGuardAdapter



from t_pop.collections.components.car import Car
import random

environment_size = [(0, 2), (0, 2)]

location_cache = LocationCacheAdapter() 
location_adapter = TwoDLocationGuardAdapter(environment_size)

    

#TODO: need to remove itself from the list of neighbours, or add this as a check into TPOP.
#do the check in tpop function

#Need to bear in mind that I should use an efficient method to remove that item from the list, otherwise it will add complexity.

#TODO: add the simulator functions. 




""" car = Car(x = 3, y =10, coerced=False)
print(car.true_x, car.true_y)
car.set_as_fake(fake_x=0, fake_y=5)
print(car.fake_x, car.fake_y) """

number_of_cars = 100
from t_pop.processes.agent_generator import coerced

cars = [Car(coerced=coerced(0), bounds = environment_size) for _ in range(number_of_cars)]

for i in range(number_of_cars):
    if i%2 == 0:
        cars[i].set_as_fake(fake_x=random.randint(0, 1), fake_y= random.randint(0, 1))
    #print(cars[i].honest)
    #print(location_adapter.location_cache.fake_cache)
    
        
    location_adapter.add_car(cars[i])
    location_adapter.move_car(cars[i], time=1)
    #print(cars[i].true_x, cars[i].true_y)
#print(location_adapter.location_cache.true_cache)
neighbours_dict = location_adapter.location_cache.get_neighbours(cars[87])
print(neighbours_dict.keys())
print(neighbours_dict[LocationCacheType.TRUE])
    #print(f'car {i} neighbours are: {location_adapter.location_cache.get_neighbours(cars[i])}')

