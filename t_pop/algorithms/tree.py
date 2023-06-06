class Tree:

    def __init__(self, prover, depth, n):
        #prover is the root of the tree, and the agent calling this function
        self.prover = prover
        #all nodes in the tree, indexed by depth level
        self.nodes = [[self.prover]]
        self.depth = depth
        
        for d in range(depth):
            
            s = []
            #for all nodes in the given depth level
            for node in self.nodes[d]:
                #the node names some witnesses
                #TODO: need to add this function to the car class
                witnesses = node.name_witness(n[d])
                if witnesses is not None:

                    for witness in witnesses:
                        #we set the parent of that witness to be the node naming them
                        witness.parent = node
                        s.append(witness)
                #and set the children of the nodes to be the named witnesses    
                node.children = s
            self.nodes.append(s)
