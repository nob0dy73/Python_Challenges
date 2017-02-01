routes = [['1', '2', '3', '2', '4', '7', '8', '5', '6', '1'], 
    ['1', '7', '4', '2', '8', '6', '5', '1']]

for route in routes:
    if len(route) > 2:
        for i in range(len(route) - 1):
            if route[i] == route[i - 2]:
                routes.remove(route)

print routes