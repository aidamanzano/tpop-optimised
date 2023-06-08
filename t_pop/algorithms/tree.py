import random
from typing import Optional
from t_pop.collections.adapters.location_cache import LocationCacheType, LocationCache


def get_neighbours(node, locations: LocationCache) -> list:
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

    def __init__(self, prover, depth, number_of_witnesses, locations):
        #prover is the root of the tree, and the agent calling this function
        self.prover = prover
        #all nodes in the tree, indexed by depth level
        self.nodes = [[self.prover]]
        self.depth = depth
        self.locations = locations
        self.number_of_witnesses = number_of_witnesses



    def build_tree(self):
        #TODO: each node should have as attribute its neighbours!!
        for d in range(self.depth):
            
            s = []
            #for all nodes in the given depth level
            for node in self.nodes[d]:
                #the node names some witnesses
                #TODO: need to add this function to the car class
                #need to add the name witness function
                neighbours = get_neighbours(node, self.locations)
                witnesses = name_witness(self.number_of_witnesses[d], neighbours)
                if witnesses is not None:

                    for witness in witnesses:
                        #we set the parent of that witness to be the node naming them
                        witness.parent = node
                        s.append(witness)
                #and set the children of the nodes to be the named witnesses    
                node.children = s
            self.nodes.append(s)
        


