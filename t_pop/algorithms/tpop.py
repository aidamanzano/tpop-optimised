
from t_pop.algorithms.tree import Tree
from t_pop.collections.adapters.location_cache import LocationCacheAdapter
from t_pop.collections.components.car import Car
from t_pop.collections.components.neighbours_testing import get_neighbours_cache_and_dict, neighbour_cars
from t_pop.collections.components.containers import Containers


def get_neighbourhood_set(parent:Car, parent_neighbours:list[Car]) -> None:
    """Function to compute the set of neighbour unique IDs of an agent.
    
    params: parent: Car class instance who's neighbourhood set is being computed.
    parent neighbours: list of car class instances containing the parent's neighbours.
    
    returns: None. Sets the parent.neighbourhood_set attribute."""
    #initialise a set to contain the unique IDs of the parent neighbours
    
    neighbour_set = set()
    
    for neighbour in parent_neighbours:
        if neighbour is not None:
            #print(neighbour)
            #add the car ID of each neighbour into the set
            neighbour_set.add(neighbour.car_id)
            parent.neighbourhood_set = neighbour_set
            #TODO; uncomment and figure out what is happening here, why is it not re setting
            #print(parent.neighbourhood_set)
    neighbour_set.clear()

def is_car_neighbour(parent:Car, parent_neighbours:list[Car], child:Car):
    """Function to check if a child is a neghbour of a parent.

    params: parent_neghbours: list of car class instances of the parent's neighbours
    child: Car instance of the child being checked
    parent: Car instance of the car whose neighbours are being checked

    returns: True if child is a neighbour of the parent and False otherwise.
    """
    #initialise a set to contain the unique IDs of the parent neighbours
    get_neighbourhood_set(parent, parent_neighbours)
    
    if child.car_id in parent.neighbourhood_set:
        return True
    else:
        #raise Exception('child is not in neighbourhood set')
        return False

def checks(child, named_cars:set, number_of_witnesses_needed:int, threshold:float, locations:LocationCacheAdapter, containers:Containers) -> bool:
    """checks called from the child with respect to the parent node, to ensure that 
    all criteria for T-PoP are met."""

    parent = child.parent
    
    parent_neighbours_cache, true_car_dictionary, fake_car_dictionary = get_neighbours_cache_and_dict(parent, locations.location_cache, containers)
    parent_container = Containers(true_car_dictionary, fake_car_dictionary)
    parent_neighbours = neighbour_cars(parent_container, parent_neighbours_cache)
    
    if (
    #checking the parent is a neighbour of the child
    is_car_neighbour(parent, parent_neighbours, child) and
    
    #checking the child has not been named before
    child.car_id not in named_cars and
    
    #checking the parent has named enough witnesses (ie children)
    len(parent.children) >= int(number_of_witnesses_needed * threshold) and

    #checking that there is no repeats in the named witnesses (ie children) 
    len(parent.children) == len(set(parent.children))
    ):
        named_cars.add(child.car_id)
        return True
    else:
        
        return False
    
def TPoP(tree:Tree, threshold:float, witness_number_per_depth:list, locations:LocationCacheAdapter, containers:Containers) -> bool:
    
    named_cars = set()

    verifiedCars = [[True for car in l] for l in tree.nodes]
    
    for level in range(tree.depth - 1, -1, -1):
        number_of_witnesses_needed = witness_number_per_depth[level]
        counterDepth = 0
        indexChild = 0
        for indexParent, parent in enumerate(tree.nodes[level]):
                counterChildren = 0
            
                for child in parent.children:
                    
                    if checks(child, named_cars, number_of_witnesses_needed, threshold, locations, containers) and verifiedCars[level + 1][indexChild]:
                        counterChildren += 1
                        counterDepth += 1
                    #else:
                        #raise Exception('checks did not pass')
                    indexChild += 1
                    
                if counterChildren < threshold*witness_number_per_depth[level+1]:
                    verifiedCars[level][indexParent] = False
                
        if counterDepth < threshold*witness_number_per_depth[level+1]:
            tree.prover.algorithm_honesty_output = False
            #raise Exception('not enough verifications at that depth level')
        else:
            tree.prover.algorithm_honesty_output = True
            
    
