from t_pop.collections.adapters.location_cache import LocationCacheAdapter
from t_pop.collections.adapters.location_guard import TwoDLocationGuardAdapter

from t_pop.algorithms.tree import Tree

from t_pop.collections.components.car import Car
from t_pop.collections.components.containers import Containers

import random


environment_size = [(0, 2), (0, 2)]

location_cache = LocationCacheAdapter() 
location_adapter = TwoDLocationGuardAdapter(environment_size)



number_of_cars = 100
from t_pop.processes.agent_generator import coerced


cars = [Car(coerced=coerced(0), bounds = environment_size) for _ in range(number_of_cars)]

true_car_container_dict = {}
fake_car_container_dict = {}


for i in range(number_of_cars):

    if i%2 == 0:
        cars[i].set_as_fake(fake_x=random.randint(0, 1), fake_y= random.randint(0, 1))
    
    location_adapter.add_car(cars[i])
    location_adapter.move_car(cars[i], time=1)

    true_car_container_dict.update( {cars[i].true_position_index : cars[i]} )
    if cars[i].honest is False:
        fake_car_container_dict.update( {cars[i].fake_position_index : cars[i]} )


#neighbours_dict = location_adapter.location_cache.get_neighbours(cars[8])



containers = Containers(true_car_container_dict, fake_car_container_dict)

tree = Tree(cars[0], 2, [2, 2], location_adapter, containers)

print('hello')

#get by ID/true position index
#dictionary with Position index as the key and the values are the car IDs
#call the memory reference and the mem ref is a singleton

#f"{x}=>{y}"
#key is the position str and the value is the hexID, and then from ID use the FlyWeight class to return/reference the car instance

""" class FlyWeight(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        # print("here are the kwargs ", kwargs)
        # print("here are the args ", args)
        if kwargs["id"] not in cls._instances:
            cls._instances[kwargs["id"]] = super(FlyWeight, cls).__call__(*args, **kwargs)
        return cls._instances[kwargs["id"]]


class Car(metaclass=FlyWeight):

    def __init__(self, id: int) -> None:
        self.id = id
        self.value = 1 """


#if __name__ == '__main__':
