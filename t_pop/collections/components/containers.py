from t_pop.collections.components.car import Car

class Containers:

    def __init__(self, true_car_container:dict, fake_car_container:dict) -> None:
        """This class is for keeping track of the car class instance given its position ID in a location cache.:

            Attributes:
            true_car_container (dictionary) = { (Car.true_position_index) : Car} dictionary with true position index as key and car class instance as value
            fake_car_container (dictionary) = { (Car.fake_position_index) : Car} dictionary with fake position index as key and car class instance as value 
        """
        self.fake_car_container_dictionary = fake_car_container
        self.true_car_container_dictionary = true_car_container
        
    def get_container_dictionary(self, node:Car):
        """Given the honesty of a car, return the correct corresponding dictionary.

        :param car: the car that we need to get a dictionary from
        :return: the dictionary of the car"""

        if node.honest is False:
            return self.fake_car_container_dictionary
        else:
            return self.true_car_container_dictionary
        
    def get_car_from_position_index(self, position_id:int, dictionary:dict) -> Car:
        """Function to get the car instance given a position ID and its dictionary.
        
        param: position_id: the true or fake position ID of a car in a location cache
            dictionary: the dictionary containing the true or the fake car position ids
            
        return: car class instance corresponding to that position id"""
        car = dictionary.get(position_id)
        return car
