"""
This file defines the Car class which is responsible for representing a car in the simulation.
"""
import random
import string
from typing import Optional, List, Tuple

import numpy as np


class Car:
    """
    This class is responsible for representing a car in the simulation.

    Attributes:
        car_id (str): the unique identifier of the car
        coerced (bool): whether the car is coerced or not
        parent (Optional[Car]): the parent car
        true_x (int): the real x coordinate of the car. 
        true_y (int): the real y coordinate of the car

        If x and y are not given, true_x and true_y are randomly generated within the bounds of the location.

        
        bounds Optional[(x_min:int, x_max: int), (y_min: int, y_max:int)]: 2D bounds of the environment of the car.
        

        fake_x (Optional[int]): the fake x coordinate of the car
        fake_y (Optional[int]): the fake y coordinate of the car
        velocity (int): the velocity of the car
        range_of_sight (float): the range of sight of the car
        position_history (List[Tuple[int, int]]): the history of the car's position
        honest (bool): whether the car is honest or not
        true_position_index (Optional[int]): the index of the car's true position in the position cache
        fake_position_index (Optional[int]): the index of the car's fake position in the position cache
    """
    def __init__(self, coerced: bool, x: Optional[int] = None, y: Optional[int] = None, 
                bounds: Optional[list] = None,
                parent: Optional["Car"] = None) -> None:
        """
        The constructor for the Car class.

        :param x: the real x coordinate of the car
        :param y: the real y coordinate of the car
        :param coerced: whether the car is coerced or not
        :param position_index: the index of the car's position in the position cache
        :param parent: the parent car
        """
        self.car_id: str = self._generate_hex_string(length=5)
        self.coerced: bool = coerced
        self.parent: Optional["BaseCar"] = parent
        
        self.fake_x: Optional[int] = None
        self.fake_y: Optional[int] = None
        self.velocity: np.array = self._generate_velocity()
        self.range_of_sight: float = 1
        self.position_history: List[Tuple[int, int]]  = []
        self.honest: bool = True
        self.true_position_index: Optional[int] = None
        self.fake_position_index: Optional[int] = None
        
        
        if bounds is not None:
            self.x_min = bounds[0][0]
            self.x_max = bounds[0][1]
            self.y_min = bounds[1][0]
            self.y_max = bounds[1][1]

        if x is None and y is None:
            self.true_x = self._generate_position(self.x_min, self.x_max)
            self.true_y: int = self._generate_position(self.y_min, self.y_max)
        else:
            self.true_x: int = x
            self.true_y: int = y


    @staticmethod
    def _generate_velocity() -> np.array:
        """
        Generates a random velocity for the car.

        :return: the velocity of the car
        """
        return ((np.random.rand(2)*2)-1)

    @staticmethod
    def _generate_hex_string(length: int) -> str:
        """
        Generates a random hex string of a given length.

        :param length: the length of the hex string
        :return: the hex string
        """
        hex_characters = string.hexdigits[:-6]
        return ''.join(random.choice(hex_characters) for _ in range(length))
    
    @staticmethod
    def _generate_position(min, max) -> int:
        """
        Generates a position integer within the bounds of the environment.

        :return: position of the car
        """
        return int(np.random.uniform(low=min, high=max, size=1))

    def set_as_fake(self, bounds: Optional[list] = None, 
                fake_x: Optional[int] = None, fake_y: Optional[int] = None) -> None:
        """
        Sets the car as a fake car. Can take either a specific fake position or 
        generates the fake position randomly.

        :param fake_x: the fake x coordinate of the car
        :param fake_y: the fake y coordinate of the car
        :return: None
        """
        

        if fake_x is None and fake_y is None:
            assert bounds != None, 'bounds should be given if no fake_x and fake_y have been provided'
            self.fake_x = self._generate_position(self.x_min, self.x_max)
            self.fake_y = self._generate_position(self.y_min, self.y_max)
        else:
            self.fake_x = fake_x
            self.fake_y = fake_y

        self.honest = False

    def move_position(self, time: float, x_min: int, x_max: int, y_min: int, y_max: int) -> None:
        """
        Moves the car real coordinates based on the self.velocity.

        :param time: the duration of the move
        :return: None
        """
        inverse = False

        provisional_x = (self.velocity[0] * time) * self.true_x
        provisional_y = (self.velocity[1] * time) * self.true_y

        if provisional_x > x_max or provisional_x < x_min:
            inverse = True
        if provisional_y > y_max or provisional_y < y_min:
            inverse = True

        if inverse is True:
            time = time * -1
            self.true_x += (self.velocity[0] * time)
            self.true_y += (self.velocity[1] * time)
        else:
            self.true_x = provisional_x
            self.true_y = provisional_y

    def move_fake_position(self, time: float, x_min: int, x_max: int, y_min: int, y_max: int) -> None:

        inverse = False

        provisional_x = (self.velocity[0] * time) * self.fake_x
        provisional_y = (self.velocity[1] * time) * self.fake_y

        if provisional_x > x_max or provisional_x < x_min:
            inverse = True
        if provisional_y > y_max or provisional_y < y_min:
            inverse = True

        if inverse is True:
            time = time * -1
            self.fake_x += (self.velocity[0] * time)
            self.fake_y += (self.velocity[1] * time)
        else:
            self.fake_x = provisional_x
            self.fake_y = provisional_y

    @property
    def x(self) -> int:
        if self.honest is False:
            return self.fake_x
        return self.true_x

    @property
    def y(self) -> int:
        if self.honest is False:
            return self.fake_y
        return self.true_y
    
        
    
