import copy


def checkio(teleports_string):
    #return any route from 1 to 1 over all points

    mylist = parse_string(teleports_string)
    graph = get_nodes(mylist)
    paths = find_paths(graph)
    return(paths[0])

def parse_string(teleports_string):
    tele_routes = teleports_string.split(",")
    a = sorted(tele_routes).pop()
    b = list(a)
    tele_number = int(b[0])
    mylist = []

    for i in range(len(tele_routes)):
        c = tele_routes.pop()
        d = list(c)
        mylist.append(d)
    mylist = mylist[::-1]
    return mylist

def get_nodes(mylist):
    graph = {}
    for items in mylist:
        if graph.has_key(items[0]) and graph.has_key(items[1]):
            graph[items[0]].append(items[1])
            graph[items[1]].append(items[0])
        elif graph.has_key(items[1]):
            graph[items[1]].append(items[0])
            graph[items[0]] = [items[1]]
        elif graph.has_key(items[0]):
            graph[items[0]].append(items[1])
            graph[items[1]] = [items[0]]
        elif graph.has_key(items[0]) == False:
            graph[items[0]] = [items[1]]
            graph[items[1]] = [items[0]]
    return graph

def find_all_paths(graph, start, end, path):
    if start == end and set(['1', '2', '3', '4', '5', '6', '7', '8']) <= set(path):
        return [path]
    paths = []
    for node in graph[start]:
        wk_graph = copy.deepcopy(graph)
        wk_graph[start].remove(node)
        wk_graph[node].remove(start)
        newpaths = find_all_paths(wk_graph, node, end, path+[node])
        if newpaths:
            for newpath in newpaths:
                paths.append(newpath)
            break
    return paths
    
def find_paths(graph):
    return find_all_paths(graph, '1', '1', ['1'])


#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    #assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"
