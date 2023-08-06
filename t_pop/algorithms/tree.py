import random
from typing import Optional
from t_pop.collections.adapters.location_cache import LocationCacheType, LocationCache
from t_pop.collections.components.containers import Containers

def get_neighbours_dict(node, locations: LocationCache) -> list:

    neighbours_dict = locations.location_cache.get_neighbours(node)
    return neighbours_dict


def name_witness(number: int, neighbours: list) -> Optional[list]:

    if len(neighbours) >= number:
        witnesses = random.sample(neighbours, number)
        return witnesses
    else:
        return None
    
def witness_dictionary_gen(neighbours_dictionary:dict, number_of_witnesses:int) -> dict:
    """
    Returns a dictionary of witnesses, with the witness ID as key and its location cache as value

    If there is only a true location cache, sample both your witnesses from true location cache
    if there is only fake location cache, sample both your witnesses from your fake location cache
    If you have both true and fake location cache: samples from both and then again to get to the right size

    :param neighbours dictionary: the car whose range of sight is to be checked
    :return: witness dictionary
    """
    witnesses_dictionary = {}
    # each key is either a TRUE location cache or FAKE location cache
    for key in neighbours_dictionary:

        #values are the car position IDs in that cache, ie the neighbours IDs' available 
        values = neighbours_dictionary[key]
        
        #if there are enough cars in that cache:
        if len(values) >= number_of_witnesses:

            #sample witnesses from the set of neighbours
            witnesses_ids = random.sample(values, number_of_witnesses)
            for witness_id in witnesses_ids:
                #we need to save the cache that the witness was sampled from, 
                #so we create a dictionary with the witness ID as the key, and its cache as the value
                witnesses_dictionary.update( {witness_id: key} )

        else:
            witnesses_dictionary == None
    #if the neighbours_dictionary has both TRUE and FAKE caches, the size of the witness_dict will be 2xnumber_of_witnesses
    #so:
    #if the witness dictionary has too many items, sample to get it to the size of number_of_witnesses
    if (len(list(witnesses_dictionary.items())) > number_of_witnesses) and (len(list(witnesses_dictionary.items())) > 0):
        witnesses_dictionary = dict(random.sample(list(witnesses_dictionary.items()), number_of_witnesses))

    return witnesses_dictionary

def get_car_from_dict(witnesses_dictionary:dict, containers:Containers):
    witnesses = []
    for id in witnesses_dictionary:
        #print(id, witnesses_dictionary[id])
        if witnesses_dictionary[id] == LocationCacheType.TRUE:
            witness = containers.get_car_from_position_index(id, containers.true_car_container_dictionary)

        else:
            witness = containers.get_car_from_position_index(id, containers.fake_car_container_dictionary)
        witnesses.append(witness)
    return witnesses
    

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

                neighbours_dictionary = get_neighbours_dict(node, self.locations)
                witness_dictionary = witness_dictionary_gen(neighbours_dictionary, self.number_of_witnesses[d])

                if witness_dictionary is not None:
                    witnesses = get_car_from_dict(witness_dictionary, containers)
                    for witness in witnesses:    
                        witness.parent = node
                        s.append(witness)
                        l.append(witness)

                #and set the children of the nodes to be the named witnesses    
                node.children = l
            self.nodes.append(s)
