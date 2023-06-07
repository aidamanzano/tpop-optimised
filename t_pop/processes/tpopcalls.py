from t_pop.collections.adapters.location_cache import LocationCacheAdapter
from t_pop.collections.adapters.location_guard import TwoDLocationGuardAdapter

from t_pop.collections.components.car import Car
import random

location_cache = LocationCacheAdapter() 
location_adapter = TwoDLocationGuardAdapter(0, 2, 0, 2)

cars = [Car(random.randint(0,2), random.randint(0,2), False) for _ in range(100)]
for i in range(100):
    if i%2 == 0:
        cars[i].set_as_fake(random.randint(1, 2), random.randint(1, 2))
        
    location_adapter.add_car(cars[i])

print('true location cache before moving the cars')
print(location_adapter.location_cache.true_cache)

print('fake location cache before moving')
print(location_adapter.location_cache.fake_cache)

for i in range(100):

    location_adapter.move_car(cars[i], 1)
    
print('true location caches after moving the cars')
print(location_adapter.location_cache.true_cache, len(location_adapter.location_cache.true_cache))

print('fake location cache after moving')
print(location_adapter.location_cache.fake_cache, len(location_adapter.location_cache.fake_cache))



for i in range(100):
    print(f'car {i} neighbours are: {location_adapter.location_cache.get_neighbours(cars[i])}')
    

#TODO: need to remove itself from the list of neighbours, or add this as a check into TPOP.
#do the check in tpop function

#Need to bear in mind that I should use an efficient method to remove that item from the list, otherwise it will add complexity.

#TODO: add the simulator functions. 