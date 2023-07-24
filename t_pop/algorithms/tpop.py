
from t_pop.algorithms.tree import Tree, get_neighbour_list
from t_pop.collections.adapters.location_cache import LocationCacheAdapter


def is_car_a_neighbour(node, neighbours):
    if node.honest is True:
        if node.true_position_index in neighbours:
            return True
        else:
            return False

    elif node.honest is False:
        if node.fake_position_index in neighbours:
            return True
        else:
            return False


def checks(child, named_cars:set, number_of_witnesses_needed:int, threshold:float, locations:LocationCacheAdapter) -> bool:
    """checks called from the child with respect to the parent node, to ensure that 
    all criteria for T-PoP are met."""

    parent = child.parent

    parent_neighbours = get_neighbour_list(parent, locations)
    
    if (
    #checking the parent is a neighbour of the child
    is_car_a_neighbour(child, parent_neighbours) and
    
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
    
def TPoP(tree:Tree, threshold:float, witness_number_per_depth:list, locations:LocationCacheAdapter) -> bool:
    named_cars = set()

    verifiedCars = [[True for car in l] for l in tree.nodes]
    
    for level in range(tree.depth - 1, -1, -1):
        number_of_witnesses_needed = witness_number_per_depth[level]
        counterDepth = 0
        indexChild = 0
        for indexParent, parent in enumerate(tree.nodes[level]):
                counterChildren = 0
            
                for child in parent.children:
                    
                    if checks(child, named_cars, number_of_witnesses_needed, threshold, locations) and verifiedCars[level + 1][indexChild]:
                        counterChildren += 1
                        counterDepth += 1
                    indexChild += 1

                if counterChildren < threshold*witness_number_per_depth[level+1]:
                    verifiedCars[level][indexParent] = False
                
        if counterDepth < threshold*witness_number_per_depth[level+1]:
            
            return False
    
    return True

