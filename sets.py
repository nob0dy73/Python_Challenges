routes = [['1', '4', '6', '5', '4', '3', '1'], ['1', '2', '8', '2', '1'], ['1', '2', '8', '7', '1'], ['1', '2', '8', '7', '1'], 
        ['1', '2', '8', '2', '1'], ['1', '2', '8', '7', '1'], ['1', '2', '8', '7', '1'], ['1', '7', '8', '2', '1'], ['1', '7', '8', '2', '1'], 
        ['1', '7', '8', '7', '1'], ['1', '7', '8', '2', '1'], ['1', '7', '8','2', '1'], ['1', '7', '8', '7', '1'], ['1', '7', '8', '2', '1', '4', '6', '5', '4', '3', '1']]

tele_route = []

for i in range(len(routes)):
    route1set = set(routes[i])
    values = set(['1', '2', '3', '4', '5', '6', '7', '8'])
    if route1set != values:       
        for route in routes:
            routeset = set(route)
            unionset = (route1set | routeset)
            if values == unionset:
                tele_route = routes[i] + route[1:]
    else:
        print routes[i]
print tele_route