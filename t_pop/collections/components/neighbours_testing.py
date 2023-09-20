
from t_pop.collections.components.location_cache import LocationCache, LocationCacheType
from typing import List, Optional

from scipy.spatial import KDTree

class Car():
    def __init__(self, coerced:bool, honest:bool, true_position:list, fake_position: Optional[list]):
        self.honest = honest
        self.coerced = coerced
        self.true_position = true_position
        self.fake_position = fake_position


def get_cars_in_range(car: Car, location_cache:LocationCache) -> List[int]:
    """
    Returns a list of the indices of the cars in range_of_sight of the given car.

    Can be used to get the fake car positions from the fake position of the car
    Can be used to get the true car positions from the true position of the car

    :param car: the car whose range of sight is to be checked
    :return: a list of the indices of the cars in range_of_sight of the given car
    """
    print('self', location_cache.cache_type)

    kdtree = KDTree(location_cache)
    #print(kdtree.data)

    if location_cache.cache_type == LocationCacheType.FAKE:
        return kdtree.query_ball_point((car.fake_x, car.fake_y), car.range_of_sight)
        #get the car instance, not return the position ID
    else:
        return kdtree.query_ball_point((car.true_x, car.true_y), car.range_of_sight)

def add_neighbours(parent, location_cache):
    neighbours = [] #make this a location cache with.True and .Fake
    if parent.honest is True and parent.coerced is True:

        cache = location_cache.true_cache
        #LocationCacheType.TRUE

        for car in cache:
            #if car in range of sight

            if car.honest is True and car.coerced is True:
                neighbours.append(car.true_position)
            elif car.honest is True and car.coerced is False:
                neighbours.append(car.true_position)
            elif car.honest is False and car.coerced is True:
                neighbours.append(car.fake_position)
            elif car.honest is False and car.coerced is False:
                neighbours.append(car.fake_position)
        #do the KD Tree query here. First we add all the cars to a list based on their honesty+coercion
        #then we shrink that list to only the cars that are in the range of sight. 
        #we make a new cache of just the neighbours for each car.


    if parent.honest is True and parent.coerced is False:

        cache = location_cache.true_cache
        #LocationCacheType.TRUE

        for car in cache:

            #I know this is spaguetti code but I want to go case by case and make sure Im not missing anything
            if car.honest is True and car.coerced is True:
                neighbours.append(car.true_position)
            elif car.honest is True and car.coerced is False:
                neighbours.append(car.true_position)
            elif car.honest is False and car.coerced is True:
                neighbours.append(car.true_position)
            elif car.honest is False and car.coerced is False:
                neighbours.append(car.true_position)

    if parent.honest is False and parent.coerced is True:

        cache = location_cache.fake_cache
        #LocationCacheType.FAKE

        for car in cache:

            if car.honest is True and car.coerced is True:
                neighbours.append(car.true_position)
            elif car.honest is True and car.coerced is False:
                neighbours.append(car.true_position)
            elif car.honest is False and car.coerced is True:
                neighbours.append(car.fake_position)
            elif car.honest is False and car.coerced is False:
                neighbours.append(car.fake_position)


    if parent.honest is False and parent.coerced is False:

        cache = location_cache.fake_cache
        #LocationCacheType.FAKE

        for car in cache:

            if car.honest is True and car.coerced is True:
                neighbours.append(car.true_position)
            elif car.honest is True and car.coerced is False:
                neighbours.append(car.true_position)
            elif car.honest is False and car.coerced is True:
                neighbours.append(car.true_position)
            elif car.honest is False and car.coerced is False:
                neighbours.append(car.true_position)

    return neighbours




"""We have a two location caches, one of the true positions and one of the fake positions
We have a function that returns all the cars within a range of sight of CAR X given a location cache and a range of sight
"""

prelim_neighbours_list = add_neighbours(car, location_cache_type)
