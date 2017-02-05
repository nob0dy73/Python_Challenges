def checkio(house, stephan, ghost):
    coords_of_map = get_coords(house)
    print "Stephan is at: " + str(stephan)
    print "The Ghost is at: " + str(ghost)
    if stephan == 1:
        return 'N'
    else:
        move = step(stephan, ghost, coords_of_map)

    return move


def direction(paths_direction):
    shortest_path = paths_direction[0]

    for path in paths_direction:
        if len(path) < len(shortest_path):
            shortest_path = path

    move = shortest_path[1]
    if (shortest_path[0] - move) == 1:
        direction = ''.join('W')
    elif (shortest_path[0] - move) == -1:
        direction = ''.join('E')
    elif (shortest_path[0] - move) == -4:
        direction = ''.join('S')
    elif (shortest_path[0] - move) == 4:
        direction = ''.join('N')
    return direction


def step(stephan, ghost, coords_of_map):
    paths = find_all_paths(coords_of_map, stephan, 1)
    paths_to_ghost = find_all_paths(coords_of_map, ghost, stephan)
    shortest_path_to_ghost = paths_to_ghost[0]
    for path in paths_to_ghost:
        if len(path) < len(shortest_path_to_ghost):
            shortest_path_to_ghost = path

    avoidance_paths = []
    if len(shortest_path_to_ghost) <= 3:
        for path in paths:
            if ghost not in path:
                avoidance_paths.append(path)
    if avoidance_paths:
        print('avoidance_paths')
        return direction(avoidance_paths)

    else:
        print('clear_path')
        return direction(paths)


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def get_coords(house):
    Map = {}

    def make_room(directions, doors=None):
        list(doors)
        newdir = []
        cardnialdir = {'N' : (room-3),
                       'E' : (room+2),
                       'S' : (room+5),
                       'W' : (room),}
        if doors:
            for door in doors:
                if door in directions:
                    directions.remove(door)
        for key, value in cardnialdir.iteritems():
            if key in directions:
                newdir.append(value)
        return newdir

    for room, doors in enumerate(house):
        theroom = room + 1
        N = (room-3)
        E = (room+2)
        S = (room+5)
        W = (room)


        #Left edge and top edge
        if theroom % 4 == 1 and (room-4) < 0:
            Map[theroom] = make_room(['E', 'S'], doors)
        #Right edge and top edge
        elif theroom % 4 == 0 and (room-4) < 0:
            Map[theroom] = make_room(['W', 'S'], doors,)
        #Left edge and bottom edge
        elif theroom % 4 == 1 and S > 16:
            Map[theroom] = make_room(['E', 'N'], doors)
        #right edge and bottom edge
        elif theroom % 4 == 0 and S > 16:
            Map[theroom] = make_room(['W', 'N'], doors,)
        #Top edge
        elif (room-4) < 0:
            Map[theroom] = make_room(['E', 'W', 'S'], doors,)
        #Left edge
        elif theroom % 4 == 1:
            Map[theroom] = make_room(['E', 'S', 'N'], doors,)
        #right edge
        elif theroom % 4 == 0:
            Map[theroom] = make_room(['W', 'S', 'N'], doors,)
        #Bottom edge
        elif S > 16:
            Map[theroom] = make_room(['E', 'W', 'N'], doors,)
        #Middle
        else:
            Map[theroom] = make_room(['E', 'W', 'N', 'S'], doors,)

    return Map







if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    from random import choice

    DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}

    def check_solution(func, house):
        stephan = 16
        ghost = 1
        for step in range(30):
            direction = func(house[:], stephan, ghost)
            if direction in house[stephan - 1]:
                print('Stefan ran into a closed door. It was hurt.')
                return False
            if stephan == 1 and direction == "N":
                print('Stefan has escaped.')
                return True
            stephan += DIRS[direction]
            if ((direction == "W" and stephan % 4 == 0) or (direction == "E" and stephan % 4 == 1) or
                    (stephan < 1) or (stephan > 16)):
                print('Stefan has gone out into the darkness.')
                return False
            sx, sy = (stephan - 1) % 4, (stephan - 1) // 4
            ghost_dirs = [ch for ch in "NWES" if ch not in house[ghost - 1]]
            if ghost % 4 == 1 and "W" in ghost_dirs:
                ghost_dirs.remove("W")
            if not ghost % 4 and "E" in ghost_dirs:
                ghost_dirs.remove("E")
            if ghost <= 4 and "N" in ghost_dirs:
                ghost_dirs.remove("N")
            if ghost > 12 and "S" in ghost_dirs:
                ghost_dirs.remove("S")

            ghost_dir, ghost_dist = "", 1000
            for d in ghost_dirs:
                new_ghost = ghost + DIRS[d]
                gx, gy = (new_ghost - 1) % 4, (new_ghost - 1) // 4
                dist = (gx - sx) ** 2 + (gy - sy) ** 2
                if ghost_dist > dist:
                    ghost_dir, ghost_dist = d, dist
                elif ghost_dist == dist:
                    ghost_dir += d
            ghost_move = choice(ghost_dir)
            ghost += DIRS[ghost_move]
            if ghost == stephan:
                print('The ghost caught Stephan.')
                return False
        print("Too many moves.")
        return False

    assert check_solution(checkio,
                          ["", "S", "S", "",
                           "E", "NW", "NS", "",
                           "E", "WS", "NS", "",
                           "", "N", "N", ""]), "1st example"
    assert check_solution(checkio,
                          ["", "", "", "",
                           "E", "ESW", "ESW", "W",
                           "E", "ENW", "ENW", "W",
                           "", "", "", ""]), "2nd example"
    assert check_solution(checkio,
                            ["","","","",
                            "E","ESW","ESW","W",
                            "E","ENW","ENW","W",
                            "","","",""]), "pycheckio example"
