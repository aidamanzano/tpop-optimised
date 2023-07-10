from tree import Tree
def checks(child, named_cars, number_of_witnesses_needed, threshold):
    """checks called from the child with respect to the parent node, to ensure that 
    all criteria for T-PoP are met."""
    counter = 0
    parent = child.parent
    parent_position = parent.claim_position()

    
    if (
    #checking the parent is a neighbour of the child

    #TODO: add this function to car class and do only one of the checks because if it is in range of sight it will be a neighbour
    #
    child.is_car_a_neighbour(parent) is True and
    


    #checking the child has not been named before
    child.ID not in named_cars and 
    #checking the parent has named enough witnesses (ie children)
    len(parent.children) >= int(number_of_witnesses_needed * threshold) and
    #checking that there is no repeats in the named witnesses (ie children) 
    len(parent.children) == len(set(parent.children))
    ):
        named_cars.add(child.ID)
        return True
    else:
        return False
    

def TPoP(tree:Tree, threshold:float, witness_number_per_depth:int) -> bool:
    named_cars = set()
    root = tree.prover
    for level in range(tree.depth - 1, -1, -1):
        number_of_witnesses_needed = witness_number_per_depth[level]
        counterDepth = 0
        for parent in tree.nodes[level]:
                counterChildren = 0
                for child in parent.children:
                    
                    if child.verified and checks(child, named_cars, number_of_witnesses_needed, threshold):

                        counterChildren += 1
                        counterDepth += 1

                if counterChildren < threshold*len(parent.children):
                    parent.verified = False
                
        if counterDepth < threshold*len(tree.nodes[level+1]):
            parent.algorithm_honesty_output = False
        else:
            parent.algorithm_honesty_output = True
        
    return root.algorithm_honesty_output


def check_no_cross_referencing(car, witnesses):
    if car.honest is True:
        if car.true_position_index in set(witnesses):
            return False
        else:
            return True
    else:
        if car.fake_position_index in set(witnesses):
            return False
        else:
            return True