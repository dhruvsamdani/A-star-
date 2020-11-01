import math
import heapq

def shortest_path(M,start,goal):
    print("shortest path called")
    
    heuristic = {}
    dist_nodes = {}
    seen = set()
    path = []
    
    next_path_heap = []
    
#     Adding the node to the heap
    
    heapq.heappush(next_path_heap, [0, start, None])
    
    for item in (M.intersections):
        
#         Heuristic results for each intersection
        
        heuristic[item] = distance(M.intersections[item], M.intersections[goal])
        dist_nodes[item] = math.inf, None
        
    dist_nodes[start] = distance(M.intersections[start], M.intersections[goal]), None
        

    while len(next_path_heap) != 0:
        
        dist, curr_node, cn = heapq.heappop(next_path_heap)
        
        if curr_node not in seen:

            seen.add(curr_node)
            
            for elem in M.roads[curr_node]:
                
                    val = distance(M.intersections[curr_node], M.intersections[elem]) + dist_nodes[curr_node][0]
                    
#                     Inspiration/Help for this if from https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
                    
                    if val < dist_nodes[elem][0]:

                        dist_nodes[elem] = (val, curr_node)

                        sub_dist = val + heuristic[elem]

                        if elem not in next_path_heap:

                            heapq.heappush(next_path_heap, [sub_dist, elem, curr_node])
   

        if curr_node == goal:
            
            while curr_node != None:
                
                path.append(curr_node)
                curr_node = dist_nodes[curr_node][1]
            print(path[::-1])
            return path[::-1]


def distance(intersection1, intersection2):
    
    diff1 = (intersection1[0] - intersection2[0]) **2
    diff2 = (intersection1[1] - intersection2[1]) **2
    
    return math.sqrt(diff1 + diff2)