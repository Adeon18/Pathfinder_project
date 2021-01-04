'''
The module contains all the functions of the program, as:
    read_csv
    get_min
    get_dist
    get_neighbours
    search
    get_path
'''
from math import sqrt


def read_csv(path):

    '''
    The function reads the file and converts the content into the list

    Args:
        path - path to the file
    Return:
        return all the required arguments for the program execution
    '''

    with open(path, "r", encoding=" utf-8 ") as file:

        lst = []

        line1 = file.readline()
        wid, step = line1.split(' ')
        wid = int(wid)
        step = int(step.strip('\n'))

        x1, y1 = file.readline().strip('\n').split(' ')

        x1 = int(x1)
        y1 = int(y1)

        x2, y2 = file.readline().strip('\n').split(' ')

        x2 = int(x2)
        y2 = int(y2)

        for line in file:
            line = line.split(" ")
            lst.append(line)

    return (wid, step, x1, y1, x2, y2, lst)


tupl = read_csv("example1.csv")

wid = tupl[0]
h = wid
step = tupl[1]

x_1, y_1 = tupl[2], tupl[3]
x_2, y_2 = tupl[4], tupl[5]

lst = tupl[6]

start = x_1 * wid + y_1
end = x_2 * wid + y_2
step = 5

parent_lst = [start for _ in range(h * wid)]
visited_lst = [0 for x in range(h * wid)]
dist_lst = [float('inf') for x in range(wid * h)]


def get_min(lst, bool_lst):
    
    '''
    The function returns an index of a minmal element in the 
    list of the distances to the dots from the distinct dot

    Args:
        lst - a list of distances
        bool_lst - a list of booleans, which contains stable dots
    Return:
        minimal index of argument
    '''

    min_val = float('inf')
    idex = -1

    for idx1 in range(len(lst)): 
        if lst[idx1] < min_val and bool_lst[idx1] == False: 
            min_val = lst[idx1] 
            idex = idx1

    return idex


def get_dist(h1, h2, step):

    '''
    The function calculates a distance between the two dots
    Args:
        h1 - dot 1 height
        h2 - dot 2 height
        step - step
    Return:
        a distance between the two dots
    '''

    h_diff = abs(h1 - h2)
    dist = sqrt(h_diff ** 2 + step ** 2)

    return dist


def get_neighbours(point_idx, visited_lst=visited_lst):

    '''
    The function forms a list of tuples of 
    neighbour dots, each contains index of the element and the distance 
    between a particular dot and the others
    Args:
        point_idx - an index of a dot
        visited_lst - a list, which represents the visited dots
    Return:
        a list of tupples with the indexes and distances
    '''

    n_h = point_idx // wid
    n_wid = point_idx % wid

    height1 = lst[n_h][n_wid]
    neighbours = []

    if n_h > 0:
        n1 = lst[n_h - 1][n_wid]
        num = wid * (n_h - 1) + n_wid

        if visited_lst[num] == 0:
            neighbours.append((n1, num))

    if n_h < h - 1:
        n2 = lst[n_h + 1][n_wid]
        num = wid * (n_h + 1) + n_wid

        if visited_lst[num] == 0:
            neighbours.append((n2, num))

    if n_wid > 0:
        n3 = lst[n_h][n_wid - 1]
        num = wid * n_h + n_wid - 1

        if visited_lst[num] == 0:
            neighbours.append((n3, num))

    if n_wid < wid - 1:
        n4 = lst[n_h][n_wid + 1]
        num = wid * n_h + n_wid + 1

        if visited_lst[num] == 0:
            neighbours.append((n4, num))

    for idx, val in enumerate(neighbours):
        neighbours[idx] = (val[1], get_dist(float(height1), float(val[0]), step))

    return neighbours


def search(start_index, end_index, wid, h, end_early=False):

    '''
    The function creates a parent list 
    (a list of parents nodes for each node)
    Args:
        start_index - starting element 
        end_index - the last element
        wid - width
        h - height
        end_early - an argument which allows a user to stop 
        executing when the path to a required dot
    Return:
        None
    '''

    dist_lst[start_index] = 0
    parent_lst[start_index] = start_index

    while 0 in visited_lst:
        idx_n = get_min(dist_lst, visited_lst)

        if end_early:
            
            if idx_n == end_index:
                break
        neighs = get_neighbours(idx_n)

        for idx_x, dist in neighs:

            if visited_lst[idx_x] == 0:

                if dist_lst[idx_n] + dist < dist_lst[idx_x]:
                    dist_lst[idx_x] = dist_lst[idx_n] + dist
                    parent_lst[idx_x] = idx_n

        visited_lst[idx_n] = 1


path_lst = []


def get_path(point_idx):

    '''
    The function returns a shortest path to the dot
    Args:
        point_idx - an index of a pivot dot 
    Return:
        a list, which contains path
    '''

    parent = parent_lst[point_idx]
    path_lst.append(parent)

    if parent != point_idx:
        return get_path(parent)
    else:
        return None

try:
    search(start, end, wid=wid, h=h, end_early=True)
except KeyboardInterrupt:
    exit()

get_path(end)
path_lst.reverse()
path_lst.pop(0)

print(path_lst)
