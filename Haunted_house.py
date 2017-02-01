def checkio(house, stephan, ghost):
    coords_of_map = get_coords(house)
    paths = find_all_paths(coords_of_map, stephan, 1)
    print "Stephan is at: " + str(stephan)
    print "The Ghost is at: " + str(ghost)
    print coords_of_map
    move = moving(paths, stephan, ghost, coords_of_map)
    return move


def moving(paths, stephan, ghost, coords_of_map):
    for path in paths:
    	if ghost in path:
    		paths.remove(path)
	if paths:
		for path in sorted(paths):
			if path[-1] == 1:
				print path
				move = path[1]
				if (path[0] - move) == 1:
					direction = ''.join('W')
				elif (path[0] - move) == -1:
					direction = ''.join('E')
				elif (path[0] - move) == -4:
					direction = ''.join('S')
				elif (path[0] - move) == 4:
					direction = ''.join('N')
				print direction
				return direction
	else:
		nodes = coords_of_map[stephan]
		for move in nodes:
			move = path[1]
			if (path[0] - move) == -1:
				direction = ''.join('W')
			elif (path[0] - move) == 1:
				direction = ''.join('E')
			elif (path[0] - move) == -4:
				direction = ''.join('S')
			elif (path[0] - move) == 4:
				direction = ''.join('N')
			print direction
			return direction

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
    for room, doors in enumerate(house):
        theroom = room + 1
        N = (room-3)
        E = (room+2)
        S = (room+5)
        W = (room)
        # If there are no doors
        if doors == '':
            #Left edge and top edge
            if theroom % 4 == 1 and (room-4) < 0:
                Map[theroom] = [E, S]
            #Left edge and bottom edge
            elif theroom % 4 == 1 and S > 16:
                Map[theroom] = [E, N]
            #Left edge
            elif theroom % 4 == 1:
                Map[theroom] = [E, S, N]
            #Right edge and top edge
            elif theroom % 4 == 0 and (room-4) < 0:
                Map[theroom] = [W, S]
            #right edge and bottom edge
            elif theroom % 4 == 0 and S > 16:
                Map[theroom] = [W, N]
            #right edge
            elif theroom % 4 == 0:
                Map[theroom] = [W, S, N]
            #Top edge
            elif (room-4) < 0:
                Map[theroom] = [E, W, S]
            #Bottom edge
            elif S > 16:
                Map[theroom] = [E, W, N]
            #Middle
            else:
                Map[theroom] = [E, W, N, S]
        #If there are doors
        elif doors != '':
            #If door to South
            if doors == 'S':
                #Left edge and top edge
                if theroom % 4 == 1 and (room-4) < 0:
                    Map[theroom] = [E]
                #Left edge and bottom edge
                elif theroom % 4 == 1 and S > 16:
                    Map[theroom] = [E, N]
                #Left edge
                elif theroom % 4 == 1:
                    Map[theroom] = [E, N]
                #Right edge and top edge
                elif theroom % 4 == 0 and (room-4) < 0:
                    Map[theroom] = [W]
                #right edge and bottom edge
                elif theroom % 4 == 0 and S > 16:
                    Map[theroom] = [W, N]
                #right edge
                elif theroom % 4 == 0:
                    Map[theroom] = [W, N]
                #Top edge
                elif (room-4) < 0:
                    Map[theroom] = [E, W]
                #Middle
                else:
                    Map[theroom] = [E, W, N]
            #If door to North
            if doors == 'N':
                #Left edge and top edge
                if theroom % 4 == 1 and (room-4) < 0:
                    Map[theroom] = [E, S]
                #Left edge and bottom edge
                elif theroom % 4 == 1 and S > 16:
                    Map[theroom] = [E]
                #Left edge
                elif theroom % 4 == 1:
                    Map[theroom] = [E, S]
                #Right edge and top edge
                elif theroom % 4 == 0 and (room-4) < 0:
                    Map[theroom] = [W, S]
                #right edge and bottom edge
                elif theroom % 4 == 0 and S > 16:
                    Map[theroom] = [W]
                #right edge
                elif theroom % 4 == 0:
                    Map[theroom] = [W, S]
                #Bottom edge
                elif S > 16:
                    Map[theroom] = [E, W]
                #Middle
                else:
                    Map[theroom] = [E, W, S]
            #If door to East
            if doors == 'E':
                #Left edge and top edge
                if theroom % 4 == 1 and (room-4) < 0:
                    Map[theroom] = [S]
                #Left edge and bottom edge
                elif theroom % 4 == 1 and S > 16:
                    Map[theroom] = [N]
                #Left edge
                elif theroom % 4 == 1:
                    Map[theroom] = [S, N]
                #Right edge and top edge
                elif theroom % 4 == 0 and (room-4) < 0:
                    Map[theroom] = [W, S]
                #right edge and bottom edge
                elif theroom % 4 == 0 and S > 16:
                    Map[theroom] = [W, N]
                #right edge
                elif theroom % 4 == 0:
                    Map[theroom] = [W, S, N]
                #Top edge
                elif (room-4) < 0:
                    Map[theroom] = [W, S]
                #Bottom edge
                elif S > 16:
                    Map[theroom] = [W, N]
                #Middle
                else:
                    Map[theroom] = [W, N, S]
            #if door to West
            if doors == 'W':
                #Left edge and top edge
                if theroom % 4 == 1 and (room-4) < 0:
                    Map[theroom] = [E, S]
                #Left edge and bottom edge
                elif theroom % 4 == 1 and S > 16:
                    Map[theroom] = [E, N]
                #Left edge
                elif theroom % 4 == 1:
                    Map[theroom] = [E, S, N]
                #Right edge and top edge
                elif theroom % 4 == 0 and (room-4) < 0:
                    Map[theroom] = [S]
                #right edge and bottom edge
                elif theroom % 4 == 0 and S > 16:
                    Map[theroom] = [N]
                #right edge
                elif theroom % 4 == 0:
                    Map[theroom] = [S, N]
                #Top edge
                elif (room-4) < 0:
                    Map[theroom] = [E, S]
                #Bottom edge
                elif S > 16:
                    Map[theroom] = [E, N]
                #Middle
                else:
                    Map[theroom] = [E, N, S]
            #If door to SouthEast
            if doors == 'SE':
                #Left edge and bottom edge
                if theroom % 4 == 1 and S > 16:
                    Map[theroom] = [N]
                #Left edge
                elif theroom % 4 == 1:
                    Map[theroom] = [N]
                #Right edge and top edge
                elif theroom % 4 == 0 and (room-4) < 0:
                    Map[theroom] = [W]
                #right edge and bottom edge
                elif theroom % 4 == 0 and S > 16:
                    Map[theroom] = [W, N]
                #right edge
                elif theroom % 4 == 0:
                    Map[theroom] = [W, N]
                #Top edge
                elif (room-4) < 0:
                    Map[theroom] = [W]
                #Middle
                else:
                    Map[theroom] = [W, N]
            #If door to SouthWest
            if doors == 'SW':
                #Left edge and top edge
                if theroom % 4 == 1 and (room-4) < 0:
                    Map[theroom] = [E]
                #Left edge and bottom edge
                elif theroom % 4 == 1 and S > 16:
                    Map[theroom] = [E, N]
                #Left edge
                elif theroom % 4 == 1:
                    Map[theroom] = [E, N]
                #right edge and bottom edge
                elif theroom % 4 == 0 and S > 16:
                    Map[theroom] = [N]
                #right edge
                elif theroom % 4 == 0:
                    Map[theroom] = [N]
                #Top edge
                elif (room-4) < 0:
                    Map[theroom] = [E]
                #Bottom edge
                elif S > 16:
                    Map[theroom] = [E, N]
                #Middle
                else:
                    Map[theroom] = [E, N]
            #If door to NorthEast
            if doors == 'NE':
                #Left edge and top edge
                if theroom % 4 == 1 and (room-4) < 0:
                    Map[theroom] = [S]
                #Left edge
                elif theroom % 4 == 1:
                    Map[theroom] = [S]
                #Right edge and top edge
                elif theroom % 4 == 0 and (room-4) < 0:
                    Map[theroom] = [W, S]
                #right edge and bottom edge
                elif theroom % 4 == 0 and S > 16:
                    Map[theroom] = [W]
                #right edge
                elif theroom % 4 == 0:
                    Map[theroom] = [W, S]
                #Top edge
                elif (room-4) < 0:
                    Map[theroom] = [W, S]
                #Bottom edge
                elif S > 16:
                    Map[theroom] = [W]
                #Middle
                else:
                    Map[theroom] = [W, S]
            #if door to NorthWest
            if doors == 'NW':
                #Left edge and top edge
                if theroom % 4 == 1 and (room-4) < 0:
                    Map[theroom] = [E, S]
                #Left edge and bottom edge
                elif theroom % 4 == 1 and S > 16:
                    Map[theroom] = [E]
                #Left edge
                elif theroom % 4 == 1:
                    Map[theroom] = [E, S]
                #Right edge and top edge
                elif theroom % 4 == 0 and (room-4) < 0:
                    Map[theroom] = [W, S]
                #right edge
                elif theroom % 4 == 0:
                    Map[theroom] = [S]
                #Top edge
                elif (room-4) < 0:
                    Map[theroom] = [E, S]
                #Bottom edge
                elif S > 16:
                    Map[theroom] = [E]
                #Middle
                else:
                    Map[theroom] = [E, S]        
            #if door to North South
            if doors == 'NS':
                #Left edge and top edge
                if theroom % 4 == 1 and (room-4) < 0:
                    Map[theroom] = [E]
                #Left edge and bottom edge
                elif theroom % 4 == 1 and S > 16:
                    Map[theroom] = [E]
                #Left edge
                elif theroom % 4 == 1:
                    Map[theroom] = [E]
                #Right edge and top edge
                elif theroom % 4 == 0 and (room-4) < 0:
                    Map[theroom] = [W]
                #right edge and bottom edge
                elif theroom % 4 == 0 and S > 16:
                    Map[theroom] = [W]
                #right edge
                elif theroom % 4 == 0:
                    Map[theroom] = [W]
                #Top edge
                elif (room-4) < 0:
                    Map[theroom] = [E, W]
                #Bottom edge
                elif S > 16:
                    Map[theroom] = [E, W]
                #Middle
                else:
                    Map[theroom] = [E, W]
            #if door to West East
            if doors == 'WE':
                #Left edge and top edge
                if theroom % 4 == 1 and (room-4) < 0:
                    Map[theroom] = [S]
                #Left edge and bottom edge
                elif theroom % 4 == 1 and S > 16:
                    Map[theroom] = [N]
                #Left edge
                elif theroom % 4 == 1:
                    Map[theroom] = [S, N]
                #Right edge and top edge
                elif theroom % 4 == 0 and (room-4) < 0:
                    Map[theroom] = [S]
                #right edge and bottom edge
                elif theroom % 4 == 0 and S > 16:
                    Map[theroom] = [N]
                #right edge
                elif theroom % 4 == 0:
                    Map[theroom] = [S, N]
                #Top edge
                elif (room-4) < 0:
                    Map[theroom] = [S]
                #Bottom edge
                elif S > 16:
                    Map[theroom] = [W, N]
                #Middle
                else:
                    Map[theroom] = [N, S]


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
