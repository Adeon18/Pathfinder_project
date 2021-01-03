'''
A module that contains all the functions needed for the dijkstra search
algoritm.

Functions:
    find_min_dist: Finds the future stable node, is called in dijkstra_search.
    dijkstra_search: The whole dijkstra algoritm.
'''
import sys

graph = [[0, 4, 0, 0, 0, 0, 0, 8 , 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0,  2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]

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



def dijkstra_search(start: int) -> list: 
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
    dist_lst[start] = 0
    # No node is yet stable.
    bool_lst = [False] * vertices

    for _ in range(vertices): 

        # Pick the unstable node with a minimum distance from the start one
        u = find_min_dist(dist_lst, bool_lst) 

        # That node becomes stable now
        bool_lst[u] = True
        # Find if there is a shorter path between nodes
        for v in range(vertices): 
            if graph[u][v] > 0 and bool_lst[v] == False\
                    and dist_lst[v] > (dist_lst[u] + graph[u][v]): 
                dist_lst[v] = dist_lst[u] + graph[u][v] 
    
    return dist_lst



if __name__ == '__main__':
    print(dijkstra_search(0))
