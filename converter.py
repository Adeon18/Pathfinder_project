'''
This module contains a function graph_converter, which
converts given matrix with high of these points into
adjacency matrix.
Functions:
    graph_converter: convert matrix into another one.
'''


def graph_converter(graph: list, step: int) -> list:
    '''
    A function that transforms given matrix into a new one
    for dijkstra algoritm.
    Args:
        graph: list of lists, where every element represents
        high of this point.
        step: projection of the distance between points on the
        plane.
    Returns:
        A new adjacency matrix for dijkstra algoritm.
    '''
    lst = []
    count = len(graph)*len(graph[0])
    lenght = len(graph[0])
    ele = []
    for i in range(len(graph)):
        for j in range(lenght):
            ele.append(graph[i][j])
    # ele = [graph[i][j] for i in range(len(graph)) for j in range(lenght)]
    lst.append(ele)
    for i in range(1, len(graph)*len(graph[0])):
        lst.append([ele[i]]+[0]*(count-1))
    for i in range(1, len(lst)):
        for j in range(1, len(lst)):
            if i != j and (abs(i % lenght - j % lenght) == 0 and
            abs(i // lenght - j // lenght) == 1) or (abs(i % lenght -
            j % lenght) == 1 and abs(i // lenght - j // lenght) == 0):
                lst[i][j] = (abs(lst[0][j]-lst[i][0])**2 + step**2)**0.5
                lst[i][j] = int('{:.0f}'.format(lst[i][j]))
    len_1_2 = (abs(lst[0][1]-lst[0][0])**2 + step**2)**0.5
    len_1_2 = int('{:.0f}'.format(len_1_2))
    len_1_x = (abs(lst[0][0]-lst[0][lenght])**2 + step**2)**0.5
    len_1_x = int('{:.0f}'.format(len_1_x))
    lst[0] = [0]+[len_1_2]+[0]*(lenght-2)+[len_1_x]+[0]*(len(ele)-lenght-1)
    for i in range(1, len(lst)):
        lst[i][0] = lst[0][i]
    return lst