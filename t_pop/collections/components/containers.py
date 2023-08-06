from t_pop.collections.components.car import Car

class Containers:

    def __init__(self, true_car_container:dict, fake_car_container:dict) -> None:
        self.fake_car_container_dictionary = fake_car_container
        self.true_car_container_dictionary = true_car_container
        
    def get_container_dictionary(self, node):
        
        if node.honest is False:
            return self.fake_car_container_dictionary
        else:
            return self.true_car_container_dictionary
        
    def get_car_from_position_index(self, id:int, dictionary:dict) -> Car:

        car = dictionary.get(id)
        return car
