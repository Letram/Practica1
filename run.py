# coding=utf-8
# Search methods

import search
                    #hasta y desde
ab = search.GPSProblem('O', 'S', search.romania)

print "------------------------------anchura---------------------------------"
#print search.breadth_first_graph_search(ab).path()
print "----------------------------profundidad-------------------------------"
#print search.depth_first_graph_search(ab).path()
print "--------------------------------poda----------------------------------"
#print search.branch_bound_graph_search(ab).path()
print "-----------------Branch&Bound subestimada-----------------------------"
print search.branch_bound_subcosts_graph_search(ab).path()
#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
