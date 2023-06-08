import numpy as np
import t_pop.collections.components.car

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

def car_generator(p:float, q:float, x_min: int, x_max: int, y_min: int, y_max: int):
    'p = probability of honest and q probability of coerced'
    h = honest(p)
    c = coerced(q)

    if h is True:
        car = t_pop.collections.components.car.Car(x_min, x_max, y_min, y_max, coerced=c)
    else:
        car = t_pop.collections.components.car.Car(x_min, x_max, y_min, y_max, coerced=c).set_as_fake(x_min, x_max, y_min, y_max)
    
    return car
