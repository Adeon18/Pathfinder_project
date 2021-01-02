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
   
        # Initilaize minimum distance for next node 
        min_dist = sys.maxsize

        for v in range(vertices): 
            if dist_lst[v] < min_dist and bool_lst[v] == False: 
                min_dist = dist_lst[v] 
                min_index = v 
   
        return min_index



def dijkstra_search(src): 
   
        dist_lst = [sys.maxsize] * vertices
        dist_lst[src] = 0
        bool_lst = [False] * vertices
   
        for _ in range(vertices): 
   
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            u = find_min_dist(dist_lst, bool_lst) 
   
            # Put the minimum distance vertex in the  
            # shotest path tree 
            bool_lst[u] = True
        
            for v in range(vertices): 
                if graph[u][v] > 0 and bool_lst[v] == False\
                        and dist_lst[v] > (dist_lst[u] + graph[u][v]): 
                    dist_lst[v] = dist_lst[u] + graph[u][v] 
        
        return dist_lst



if __name__ == '__main__':
    print(dijkstra_search(0))
