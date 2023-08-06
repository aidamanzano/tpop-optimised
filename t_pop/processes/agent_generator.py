import numpy as np
from t_pop.collections.components.car import Car

def coerced(q):
    coin_toss = np.random.rand()
        
    if coin_toss < q:
        return True
    else:
        return False

def honest(p):
    coin_toss = np.random.rand()
    if coin_toss < p:
        return True
    else:
        return False

def car_generator(p:float, q:float, environment_size, number_of_cars):
    'p = probability of honest and q probability of coerced'
    car_list = [Car(coerced=coerced(p), honest = honest(q), bounds = environment_size) for _ in range(number_of_cars)]
    
    return car_list
