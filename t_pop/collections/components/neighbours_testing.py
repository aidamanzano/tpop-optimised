
from t_pop.collections.components.location_cache import LocationCache
from t_pop.collections.adapters.location_cache import LocationCacheAdapter
from t_pop.collections.components.car import Car
from t_pop.collections.components.containers import Containers


def get_neighbours_cache_and_dict(parent: Car, location_cache:LocationCacheAdapter, containers:Containers) -> LocationCache:
    """Need to write a better docstring here later"""
    neighbours_cache = LocationCacheAdapter()

    true_car_dictionary = {}
    fake_car_dictionary = {}

    true_cache = location_cache.true_cache
    fake_cache = location_cache.fake_cache
    
    if parent.honest is True and parent.coerced is True:
    #If the parent is honest and coerced, it adds neighbours from its TRUE position

        #true_cache contains the true positions of the cars being checked. 
        for car_position_id, car_position in enumerate(true_cache):

            dictionary = containers.true_car_container_dictionary
            car = containers.get_car_from_position_index(car_position_id, dictionary)
            assert car_position == (car.true_x, car.true_y)

            #if the car's True position is within the range of sight of the parent's true position
            if parent.is_in_true_range_of_sight(car.true_x, car.true_y):

                if car.honest is True and car.coerced is True:
                    
                    true_car_dictionary.update({ car_position_id: car})
                    #can just append car_position here, it doesnt really matter
                    neighbours_cache.true_cache.append((car.true_x, car.true_y)) 
                    
                elif car.honest is True and car.coerced is False:                    
                    #neighbours_cache.add_car(car)
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))

        for car_position_id, car_position in enumerate(fake_cache):

            dictionary = containers.fake_car_container_dictionary
            car = containers.get_car_from_position_index(car_position_id, dictionary)
            assert car_position == (car.fake_x, car.fake_y)

            #if the car's Fake position is within the range of sight of the parent's true position
            if parent.is_in_true_range_of_sight(car.fake_x, car.fake_y):

                if car.honest is False and car.coerced is True:                   
                    #neighbours_cache.add_car(car)
                    neighbours_cache.fake_cache.append((car.fake_x, car.fake_y))
                    fake_car_dictionary.update({ car_position_id: car})

                if car.honest is False and car.coerced is False:
                    fake_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.fake_cache.append((car.fake_x, car.fake_y))

    
    if parent.honest is True and parent.coerced is False:
        #If the parent is honest and not coerced, it adds neighbours from its TRUE position
        for car_position_id, car_position in enumerate(true_cache):

            dictionary = containers.true_car_container_dictionary
            car = containers.get_car_from_position_index(car_position_id, dictionary)
            assert car_position == (car.true_x, car.true_y)

            #if the car's True position is within the range of sight of the parent's true position
            if parent.is_in_true_range_of_sight(car.true_x, car.true_y):

                #I know this is spaguetti code but I want to go case by case and make sure Im not missing anything
                if car.honest is True and car.coerced is True:                    
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))

                elif car.honest is True and car.coerced is False:
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))

                elif car.honest is False and car.coerced is True:                    
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))

                elif car.honest is False and car.coerced is False:                    
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))

    if parent.honest is False and parent.coerced is True:

        for car_position_id, car_position in enumerate(true_cache):

            dictionary = containers.true_car_container_dictionary
            car = containers.get_car_from_position_index(car_position_id, dictionary)
            assert car_position == (car.true_x, car.true_y)

            #if the car's True position is within the range of sight of the parent's Fake position
            if parent.is_in_fake_range_of_sight(car.true_x, car.true_y):

                if car.honest is True and car.coerced is True:                    
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))

                elif car.honest is True and car.coerced is False:                    
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))

        for car_position_id, car_position in enumerate(fake_cache):
            dictionary = containers.fake_car_container_dictionary
            car = containers.get_car_from_position_index(car_position_id, dictionary)
            assert car_position == (car.fake_x, car.fake_y)

            #if the car's fake position is within the range of sight of the parent's fake position
            if parent.is_in_fake_range_of_sight(car.fake_x, car.fake_y):

                if car.honest is False and car.coerced is True:
                    fake_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.fake_cache.append((car.fake_x, car.fake_y))

                if car.honest is False and car.coerced is False:
                    fake_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.fake_cache.append((car.fake_x, car.fake_y))

    if parent.honest is False and parent.coerced is False:
        
        for car_position_id, car_position in enumerate(true_cache):

            dictionary = containers.true_car_container_dictionary
            car = containers.get_car_from_position_index(car_position_id, dictionary)
            assert car_position == (car.true_x, car.true_y)

            if parent.is_in_fake_range_of_sight(car.true_x, car.true_y):

                if car.honest is True and car.coerced is True:                    
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))

                elif car.honest is True and car.coerced is False:                    
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))

        for car_position_id, car_position in enumerate(fake_cache):

            dictionary = containers.fake_car_container_dictionary
            car = containers.get_car_from_position_index(car_position_id, dictionary)
            assert car_position == (car.fake_x, car.fake_y)

            if parent.is_in_fake_range_of_sight(car.true_x, car.true_y):

                if car.honest is False and car.coerced is True:
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))

                elif car.honest is False and car.coerced is False:                    
                    true_car_dictionary.update({ car_position_id: car})
                    neighbours_cache.true_cache.append((car.true_x, car.true_y))


    return neighbours_cache, true_car_dictionary, fake_car_dictionary


#TODO: remember to actually make the car container first!! by doing: 
#car0_containers = Containers(true_car_neighbours_dict, fake_car_neighbours_dict)

def neighbour_cars(car_container:Containers, car_neighbour_cache:LocationCacheAdapter) -> list[Car]:
    """Function to construct the list of neighbours (car instance objects)
    
    params: car_container: Containers with the car's dictionaries of the true neighbours position and fake neighbours position
    car_neighbour_cache: LocationCacheAdapter with the true position ID and true position of the neighbours, and same with fake position IDs and positions
    
    returns: neighbour_cars: list with Car class instances of the neighbours"""
    neighbour_cars = []

    for car_position_id, car_position in enumerate(car_neighbour_cache.fake_cache):
        #we get the dictionary that contains the fake car positions and the fake car class instance
        dictionary = car_container.fake_car_container_dictionary
        #if dictionary is not empty
        if bool(dictionary):
            dictionary_indecies = list(dictionary.keys())

            #retrieve the car class instance from the dictionary using the container class
            car = car_container.get_car_from_position_index(dictionary_indecies[car_position_id], dictionary)
            assert car is not None

            print(car.fake_x, car.fake_y, car_position)
            #assert car_position == (car.fake_x, car.fake_y)

            #add the car to the list of neighbours
            neighbour_cars.append(car)

    for car_position_id, car_position in enumerate(car_neighbour_cache.true_cache):
        
        #we get the dictionary that contains the true car positions and the true car class instance
        dictionary = car_container.true_car_container_dictionary
        print(car_position_id)
        if bool(dictionary):
            dictionary_indecies = list(dictionary.keys()) #TODO: this is not the same size as the locaction cache and that is an error?
            print(dictionary_indecies)
            #retrieve the car class instance from the dictionary using the container class
            car = car_container.get_car_from_position_index(dictionary_indecies[car_position_id], dictionary)

            assert car is not None

            print(car.true_x, car.true_y, car_position, car.fake_x, car.fake_y)
            #assert car_position == (car.true_x, car.true_y) #TODO: assertion failing when there are dihonest cars and not sure why?
            #add the car to the list of neighbours
            neighbour_cars.append(car)

    return neighbour_cars