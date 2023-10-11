import random
from typing import Optional
from t_pop.collections.adapters.location_cache import LocationCacheAdapter
from t_pop.collections.components.containers import Containers
from t_pop.collections.components.car import Car
from t_pop.collections.components.neighbours_testing import get_neighbours_cache_and_dict, neighbour_cars


def name_witnesses(number: int, neighbours: list) -> Optional[list]:
    """Function to sample a given number of witnesses from a list of neighbours.
    
    params: number: int, number of witnesses to sample.
            neighbours: the list of car class instances from which to sample witnesses.
            
    returns: None if not enough neighbours are available, and a list of n witness cars otherwise."""
    
    if len(neighbours) >= number:
        witnesses = random.sample(neighbours, number)
        return witnesses
    else:
        return None
    

class Tree:
    #TODO: NEEDS MORE COMMENTS, WHAT IS HAPPENING
    def __init__(self, prover:Car, depth:int, number_of_witnesses:list, locations:LocationCacheAdapter, containers:Containers):

        #prover is the root of the tree, and the agent calling this function
        self.prover = prover
        #all nodes in the tree, indexed by depth level
        self.nodes = [[self.prover]]
        self.depth = depth
        self.number_of_witnesses = number_of_witnesses
        
        for d in range(depth):
            
            s = []
            #for all nodes in the given depth level
            for node in self.nodes[d]:
                l = []

                neighbours_cache, true_car_neighbours_dict, fake_car_neighbours_dict = get_neighbours_cache_and_dict(node, locations.location_cache, containers)
                node_container = Containers(true_car_neighbours_dict, fake_car_neighbours_dict)
                neighbour_cars_list = neighbour_cars(node_container, neighbours_cache)

                witnesses = name_witnesses(self.number_of_witnesses[d], neighbour_cars_list)
                if witnesses is not None:    
                    for witness in witnesses:
                        #TODO: is this next line redundant:
                        if witness is not None:    
                            witness.parent = node
                            s.append(witness)
                            l.append(witness)

                #and set the children of the nodes to be the named witnesses    
                node.children = l

            self.nodes.append(s)

