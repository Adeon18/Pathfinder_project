'''
A module that contains all the functions needed for the dijkstra search
algoritm.

Functions:
    find_min_dist: Finds the future stable node, is called in dijkstra_search.
    dijkstra_search: The whole dijkstra algoritm.
'''
import sys
import random
from converter import graph_converter
from test import main

input_data = main()

lst_0 = input_data[0]

index_start = input_data[2][0]*len(lst_0[0]) + input_data[2][1]
index_end = input_data[3][0]*len(lst_0[0]) + input_data[3][1]
print(index_start, index_end)

graph = graph_converter(lst_0, main()[1])

# graph =   [[0, 3, 2, 0, 0, 0],
#            [3, 0, 0, 1, 0, 0],
#            [2, 0, 0, 4, 8, 0],
#            [0, 1, 4, 0, 0, 2],
#            [0, 0, 8, 0, 0, 2],
#            [0, 0, 0, 2, 2, 0]]
           

vertices = len(graph)


def find_min_dist(dist_lst: list, bool_lst: list) -> int: 
    '''
    A function that finds a node that can be turned into a stable one but
    is not yet stable

    Args:
        dist_lst: The list of all node distances.
        bool_lst: The list of bools, each one representing if an appropriate
          node is stable
    
    Returns:
        The index of that node in dist_lst.
    '''
    min_dist = sys.maxsize

    for v in range(vertices): 
        if dist_lst[v] < min_dist and bool_lst[v] == False: 
            min_dist = dist_lst[v] 
            min_index = v 

    return min_index


def printPath(parent, j): 
          
        #Base Case : If j is source 
        if parent[j] == -1:  
            print(j, end=' ')
            return
        printPath(parent , parent[j]) 
        print(j, end=' ') 
          
  
    # A utility function to print 
    # the constructed distance 
    # array 
def printSolution(dist, parent): 
    src = 0
    print("Vertex \t\tDistance from Source\tPath")

    print("\n%d --> %d \t\t%d \t\t" % (src, index_end, dist[index_end]), end='')
    printPath(parent,index_end)

    print()


def dijkstra_search(start: int, end: int) -> list: 
    '''
    The main dijkstra search algoritm, which works from a certain node.

    Args:
        start: The index of a start node in dist_list.
    
    Returns:
        Modified dist list with all nodes and their distances from the start
          one.
    '''
    # Create a list of infinites
    dist_lst = [sys.maxsize] * vertices
    # Start from a start node
        
    queue = [] 
    for i in range(vertices): 
        queue.append(i)
    
    parent = [-1] * vertices 
    dist_lst[start] = 0
    # No node is yet stable.
    bool_lst = [False] * vertices

    while queue:

        # Pick the unstable node with a minimum distance from the start one
        u = find_min_dist(dist_lst, bool_lst) 

        # That node becomes stable now
        bool_lst[u] = True

        queue.remove(u) 
        
        # Find if there is a shorter path between nodes
        for v in range(vertices): 
            if graph[u][v] and v in queue: 
                if dist_lst[v] > (dist_lst[u] + graph[u][v]):
                    dist_lst[v] = dist_lst[u] + graph[u][v]
                    parent[v] = u

    
    printSolution(dist_lst, parent) 



if __name__ == '__main__':
    print(dijkstra_search(index_start, index_end))
    pass
