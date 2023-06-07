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

def car_generator(p:float, q:float):
    'p = probability of honest and q probability of coerced'
    h = honest(p)
    c = coerced(q)

    if h is True:
        car = t_pop.collections.components.car.Car(x_min=0, x_max=10, y_min=0, y_max=10, coerced=c)
    else:
        car = t_pop.collections.components.car.Car(x_min=0, x_max=10, y_min=0, y_max=10, coerced=c).set_as_fake(x_min=0, x_max=10, y_min=0, y_max=10)
    
    return car
