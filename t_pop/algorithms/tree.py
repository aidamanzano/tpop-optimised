import random
from typing import Optional
from t_pop.collections.adapters.location_cache import LocationCacheType, LocationCache



def get_neighbour_list(node, locations: LocationCache) -> list:

    neighbours_dict = locations.location_cache.get_neighbours(node)
    
    if node.honest is False:    
        neighbours = neighbours_dict[LocationCacheType.FAKE]
    else:
        neighbours = neighbours_dict[LocationCacheType.TRUE]
    return neighbours


def name_witness(number: int, neighbours: list) -> Optional[list]:

    if len(neighbours) >= number:
        witnesses = random.sample(neighbours, number)
        return witnesses
    else:
        return None
    

class Tree:

    def __init__(self, prover, depth:int, number_of_witnesses:list, locations, containers):
        #prover is the root of the tree, and the agent calling this function
        self.prover = prover
        #all nodes in the tree, indexed by depth level
        self.nodes = [[self.prover]]
        self.depth = depth
        self.locations = locations
        self.number_of_witnesses = number_of_witnesses
        
        for d in range(depth):
            
            s = []
            #for all nodes in the given depth level
            for node in self.nodes[d]:
                l = []

                neighbours = get_neighbour_list(node, self.locations)

                dictionary = containers.get_container_dictionary(node)

                witnesses_ids = name_witness(self.number_of_witnesses[d], neighbours)

                if witnesses_ids is not None:
                    for witness_id in witnesses_ids:
                        witness = containers.get_car_from_position_index(witness_id, dictionary)
                        witness.parent = node
                        s.append(witness)
                        l.append(witness)

                #and set the children of the nodes to be the named witnesses    
                node.children = l
            self.nodes.append(s)
